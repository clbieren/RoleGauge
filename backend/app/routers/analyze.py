"""
Analyze Router.
POST /api/analyze — Main analysis pipeline endpoint.
Orchestrates:
- GitHub profile fetch & analysis (optional)
- CV upload & rule-based parsing (optional)
- Multi-source Evidence Engine fusion
- Dynamic scoring engine calculation
- Database persistence & response generation.
"""

import logging
import os
import tempfile
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db
from app.dependencies.auth import get_optional_user
from app.exceptions import RoleGaugeException, RoleNotFoundError
from app.models.db_models import Analysis, RepoData, SkillResult, SubskillResult, User
from app.models.schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    RepoInfo,
    SkillScore,
    SubskillEvidence,
)
from app.services.ai_provider import get_ai_provider
from app.services.cv_certification_matcher import CertificationMatcher, get_certification_index
from app.services.cv_parser import parse_cv
from app.services.cv_skill_matcher import CVSkillMatcher
from app.services.evidence_detector import EvidenceDetector, SubskillEvidenceResult
from app.services.evidence_engine import EvidenceEngine, UnifiedSubskillEvidence
from app.services.github_fetcher import GitHubFetcher, extract_username
from app.services.kb_loader import kb
from app.services.linkedin_skill_matcher import LinkedInSkillMatcher
from app.services.role_filter import FilteredRepo, RoleFilter
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_profile(
    http_request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user),
) -> AnalyzeResponse:
    """
    Analyze a candidate's profile for a specific role and level.
    Supports:
    - JSON payload (`application/json`) with `github_username`, `role_id`, `level`
    - Multipart payload (`multipart/form-data`) with `file` (CV), `github_username`, `role_id`, `level`

    At least one of `github_username` or `file` is required.
    """
    content_type = http_request.headers.get("content-type", "").lower()
    github_username: Optional[str] = None
    role_id: str = ""
    level: str = "mid"
    github_token: Optional[str] = None
    use_ai: bool = False
    cv_file: Optional[UploadFile] = None
    cv_bytes: Optional[bytes] = None
    cv_filename: Optional[str] = None
    linkedin_file: Optional[UploadFile] = None
    linkedin_bytes: Optional[bytes] = None
    linkedin_filename: Optional[str] = None

    # Step 1: Parse request based on content-type
    if "multipart/form-data" in content_type:
        form = await http_request.form()
        github_username = form.get("github_username")  # type: ignore
        role_id = form.get("role_id", "")  # type: ignore
        level = form.get("level", "mid")  # type: ignore
        github_token = form.get("github_token")  # type: ignore
        use_ai_raw = form.get("use_ai", "false")  # type: ignore
        use_ai = str(use_ai_raw).lower() in ("true", "1")
        
        file_obj = form.get("file")
        if file_obj and hasattr(file_obj, "filename") and file_obj.filename:
            cv_file = file_obj  # type: ignore
            cv_filename = cv_file.filename
            cv_bytes = await cv_file.read()

        li_file_obj = form.get("linkedin_file")
        if li_file_obj and hasattr(li_file_obj, "filename") and li_file_obj.filename:
            linkedin_file = li_file_obj  # type: ignore
            linkedin_filename = linkedin_file.filename
            linkedin_bytes = await linkedin_file.read()
    else:
        # JSON body
        try:
            body = await http_request.json()
            req = AnalyzeRequest(**body)
            github_username = req.github_username
            role_id = req.role_id
            level = req.level
            github_token = req.github_token
            use_ai = req.use_ai
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid request body: {e}")

    # Step 2: Validate inputs
    if not github_username and not cv_bytes and not linkedin_bytes:
        raise HTTPException(
            status_code=400,
            detail="At least one evidence source ('github_username', CV file, or LinkedIn file) is required for analysis.",
        )

    if role_id not in kb.role_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown role: '{role_id}'. Available roles: {kb.role_categories}",
        )

    role_def = kb.get_role(role_id, level)
    if not role_def:
        raise HTTPException(
            status_code=400,
            detail=f"Level '{level}' not found for role '{role_id}'",
        )

    # ── Pipeline Execution ──
    github_evidence: Optional[dict[str, SubskillEvidenceResult]] = None
    filtered_repos: list[FilteredRepo] = []
    username_clean: str = ""

    cv_skills_evidence: Optional[dict[str, SubskillEvidenceResult]] = None
    cv_cert_matches: Optional[list[dict[str, Any]]] = None

    linkedin_evidence: Optional[dict[str, SubskillEvidenceResult]] = None
    linkedin_cert_matches: Optional[list[dict[str, Any]]] = None

    try:
        # Step 3: Run GitHub pipeline if username provided
        if github_username and github_username.strip():
            try:
                username_clean = extract_username(github_username.strip())
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

            logger.info(f"Starting GitHub analysis for {username_clean} as {role_id}/{level}")
            fetcher = GitHubFetcher(token=github_token)
            repos = await fetcher.fetch_user_repos(username_clean)

            if not repos and not cv_bytes and not linkedin_bytes:
                raise HTTPException(status_code=404, detail=f"No public repositories found for user '{username_clean}'")

            if repos:
                role_filter = RoleFilter(kb, role_id)
                filtered_repos = role_filter.filter_repos(repos)

                files_to_fetch = role_filter.get_files_to_fetch_content(filtered_repos)
                for repo_full_name, file_paths in files_to_fetch.items():
                    contents = await fetcher.fetch_specific_files(repo_full_name, file_paths)
                    for f_repo in filtered_repos:
                        if f_repo.full_name == repo_full_name:
                            f_repo.file_contents = contents
                            break

                detector = EvidenceDetector(kb, role_id)
                github_evidence = detector.detect_all(filtered_repos)

                # Optional: AI enrichment for GitHub evidence
                if use_ai:
                    ai_provider = get_ai_provider()
                    unevidenced = [
                        key for key, result in github_evidence.items()
                        if result.status == "not_yet_evidenced"
                    ]
                    if unevidenced:
                        ai_data = _prepare_ai_data(filtered_repos)
                        ai_results = await ai_provider.analyze_evidence(
                            role_id, level, unevidenced, ai_data
                        )
                        _merge_ai_results(github_evidence, ai_results)

        # Step 4: Run CV pipeline if file provided
        if cv_bytes and cv_filename:
            file_ext = os.path.splitext(cv_filename)[1].lower()
            if file_ext not in settings.CV_ALLOWED_EXTENSIONS:
                raise HTTPException(
                    status_code=400,
                    detail=f"Unsupported CV format: '{file_ext}'. Only PDF and DOCX are accepted.",
                )
            if len(cv_bytes) > settings.CV_MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=413,
                    detail=f"CV file too large: {len(cv_bytes)} bytes (max 10MB).",
                )

            temp_path = None
            try:
                with tempfile.NamedTemporaryFile(
                    suffix=file_ext, delete=False, prefix="rolegauge_cv_"
                ) as tmp:
                    tmp.write(cv_bytes)
                    temp_path = tmp.name

                parsed_cv = parse_cv(temp_path, source_type="cv")
            finally:
                if temp_path and os.path.exists(temp_path):
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass

            skill_matcher = CVSkillMatcher(kb, role_id)
            cv_skills_evidence = skill_matcher.match_all(parsed_cv)

            cert_index = get_certification_index()
            if not cert_index._built:
                cert_index.build(kb)
            cert_matcher = CertificationMatcher(kb, cert_index, role_id)
            cv_cert_matches = cert_matcher.match_certificates(parsed_cv.get("certificates", []))

        # Step 5: Run LinkedIn pipeline if LinkedIn file provided
        if linkedin_bytes and linkedin_filename:
            li_ext = os.path.splitext(linkedin_filename)[1].lower()
            if li_ext != ".pdf":
                raise HTTPException(
                    status_code=400,
                    detail=f"Unsupported LinkedIn format: '{li_ext}'. Only PDF is accepted.",
                )
            if len(linkedin_bytes) > settings.CV_MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=413,
                    detail=f"LinkedIn file too large: {len(linkedin_bytes)} bytes (max 10MB).",
                )

            temp_li_path = None
            try:
                with tempfile.NamedTemporaryFile(
                    suffix=li_ext, delete=False, prefix="rolegauge_li_"
                ) as tmp:
                    tmp.write(linkedin_bytes)
                    temp_li_path = tmp.name

                parsed_li = parse_cv(temp_li_path, source_type="linkedin")
            finally:
                if temp_li_path and os.path.exists(temp_li_path):
                    try:
                        os.unlink(temp_li_path)
                    except OSError:
                        pass

            li_matcher = LinkedInSkillMatcher(kb, role_id)
            linkedin_evidence = li_matcher.match_all(parsed_li)

            cert_index = get_certification_index()
            if not cert_index._built:
                cert_index.build(kb)
            cert_matcher = CertificationMatcher(kb, cert_index, role_id)
            linkedin_cert_matches = cert_matcher.match_certificates(parsed_li.get("certificates", []))

        # Step 6: Multi-source Fusion via Evidence Engine
        evidence_engine = EvidenceEngine(kb, role_id, level)
        unified_evidence = evidence_engine.merge_evidence(
            github_evidence=github_evidence,
            cv_skills_evidence=cv_skills_evidence,
            cv_cert_matches=cv_cert_matches,
            linkedin_evidence=linkedin_evidence,
            linkedin_cert_matches=linkedin_cert_matches,
        )

        # Step 7: Dynamic Scoring Engine
        scoring_evidence = {
            ck: u.to_subskill_evidence_result() for ck, u in unified_evidence.items()
        }
        scoring_engine = ScoringEngine(kb, role_id, level)
        scoring_result = scoring_engine.calculate_all(scoring_evidence)

        # Step 8: Save to Database
        user_id = current_user.id if current_user else None
        analysis = await _save_analysis(
            db=db,
            user_id=user_id,
            username=username_clean,
            role_id=role_id,
            level=level,
            use_ai=use_ai,
            scoring_result=scoring_result,
            filtered_repos=filtered_repos,
            scoring_evidence=scoring_evidence,
        )

        # Step 9: Return Structured Response
        role_title = role_def.get("title", f"{level.capitalize()} {role_id}")
        return _build_response(
            analysis_id=analysis.id,
            username=username_clean,
            role_id=role_id,
            role_title=role_title,
            level=level,
            has_cv=bool(cv_bytes),
            has_linkedin=bool(linkedin_bytes),
            scoring_result=scoring_result,
            filtered_repos=filtered_repos,
        )

    except RoleGaugeException as e:
        logger.warning(f"Analysis error for {github_username or 'CV'}: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Analysis failed unexpectedly for {github_username or 'CV'}")
        raise HTTPException(status_code=500, detail=f"Analysis pipeline failed: {str(e)}")


def _prepare_ai_data(filtered_repos: list) -> dict[str, Any]:
    """Prepare filtered data bundle for AI analysis."""
    all_contents: dict[str, str] = {}
    all_deps: dict[str, str] = {}
    readme_parts: list[str] = []

    for repo in filtered_repos:
        if not repo.is_relevant:
            continue
        for path, content in repo.file_contents.items():
            all_contents[f"{repo.repo_name}/{path}"] = content
        for path, content in repo.dependency_files.items():
            all_deps[f"{repo.repo_name}/{path}"] = content
        if repo.readme_content:
            readme_parts.append(f"# {repo.repo_name}\n{repo.readme_content[:1000]}")

    return {
        "file_contents": all_contents,
        "dependencies": all_deps,
        "readme": "\n\n---\n\n".join(readme_parts),
    }


def _merge_ai_results(evidence: dict, ai_results: dict):
    """Merge AI detection results into the evidence map."""
    from app.services.evidence_detector import EvidenceSignal

    for composite_key, ai_data in ai_results.items():
        if composite_key not in evidence:
            continue
        if ai_data.get("status") == "evidence_found":
            sources = ai_data.get("evidence_sources", [])
            for source in sources:
                evidence[composite_key].signals.append(EvidenceSignal(
                    source="ai",
                    file_path=source,
                    matched_text=ai_data.get("quality_notes", "AI detected"),
                    strength=0.7,
                ))
            evidence[composite_key].status = "evidence_found"


async def _save_analysis(
    db: AsyncSession,
    user_id: Optional[uuid.UUID],
    username: str,
    role_id: str,
    level: str,
    use_ai: bool,
    scoring_result: dict,
    filtered_repos: list,
    scoring_evidence: dict,
) -> Analysis:
    """Save analysis results to PostgreSQL."""
    analysis = Analysis(
        user_id=user_id,
        github_username=username or "cv_upload",
        role_id=role_id,
        level=level,
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        total_repos_scanned=len(filtered_repos),
        relevant_repos_found=sum(1 for r in filtered_repos if r.is_relevant),
        ai_provider_used=use_ai and "openai" or "none",
    )
    db.add(analysis)
    await db.flush()

    for skill_data in scoring_result["skills"]:
        skill_result = SkillResult(
            analysis_id=analysis.id,
            skill_id=skill_data["skill_id"],
            skill_name=skill_data["skill_name"],
            score=skill_data["score"],
            importance=skill_data["importance"],
        )
        db.add(skill_result)
        await db.flush()

        for sub in skill_data["subskills"]:
            subskill_result = SubskillResult(
                skill_result_id=skill_result.id,
                composite_key=sub["composite_key"],
                subskill_name=sub["subskill_name"],
                confidence=sub["confidence"],
                status=sub["status"],
                evidence_sources=sub.get("evidence_sources", []),
            )
            db.add(subskill_result)

    for repo in filtered_repos:
        repo_evidence = []
        for composite_key, ev in scoring_evidence.items():
            if ev.status == "evidence_found":
                for signal in ev.signals:
                    if repo.repo_name in signal.file_path:
                        repo_evidence.append(composite_key)
                        break

        repo_data = RepoData(
            analysis_id=analysis.id,
            repo_name=repo.repo_name,
            repo_url=repo.url,
            description=repo.description,
            primary_language=repo.primary_language,
            languages=repo.languages,
            stars=repo.stars,
            forks=repo.forks,
            topics=repo.topics,
            is_relevant=repo.is_relevant,
            relevant_files_count=len(repo.relevant_files),
            evidence_found=list(set(repo_evidence)),
        )
        db.add(repo_data)

    return analysis


def _build_response(
    analysis_id: Any,
    username: str,
    role_id: str,
    role_title: str,
    level: str,
    has_cv: bool,
    has_linkedin: bool,
    scoring_result: dict,
    filtered_repos: list,
) -> AnalyzeResponse:
    """Build the API response from scoring results."""
    skills = []
    for skill_data in scoring_result["skills"]:
        subskills = [
            SubskillEvidence(
                composite_key=sub["composite_key"],
                subskill_name=sub["subskill_name"],
                confidence=sub["confidence"],
                status=sub["status"],
                evidence_sources=sub.get("evidence_sources", []),
                contributing_sources=sub.get("contributing_sources", []),
                ceiling_applied=sub.get("ceiling_applied"),
                calculation_trace=sub.get("calculation_trace"),
            )
            for sub in skill_data["subskills"]
        ]
        skills.append(SkillScore(
            skill_id=skill_data["skill_id"],
            skill_name=skill_data["skill_name"],
            score=skill_data["score"],
            importance=skill_data["importance"],
            subskills=subskills,
        ))

    repos = [
        RepoInfo(
            repo_name=r.repo_name,
            repo_url=r.url,
            description=r.description,
            primary_language=r.primary_language,
            languages=r.languages,
            stars=r.stars,
            forks=r.forks,
            topics=r.topics,
            is_relevant=r.is_relevant,
            relevant_files_count=len(r.relevant_files),
            evidence_found=[],
        )
        for r in filtered_repos
    ]

    return AnalyzeResponse(
        id=str(analysis_id),
        github_username=username,
        role_id=role_id,
        role_name=role_title,
        level=level,
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        readiness_label=scoring_result["readiness_label"],
        total_repos_scanned=len(filtered_repos),
        relevant_repos_found=sum(1 for r in filtered_repos if r.is_relevant),
        has_cv=has_cv,
        has_linkedin=has_linkedin,
        skills=skills,
        repos=repos,
        created_at=datetime.now(timezone.utc),
    )
