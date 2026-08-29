"""
Analyze Router.
POST /api/analyze — Main analysis pipeline endpoint.
Orchestrates: GitHub fetch → Role filter → Evidence detect → Scoring → DB save.
"""

import logging
import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.exceptions import RoleGaugeException, RoleNotFoundError
from app.models.db_models import Analysis, SkillResult, SubskillResult, RepoData
from app.models.schemas import AnalyzeRequest, AnalyzeResponse, SkillScore, SubskillEvidence, RepoInfo
from app.services.github_fetcher import GitHubFetcher, extract_username
from app.services.role_filter import RoleFilter
from app.services.evidence_detector import EvidenceDetector
from app.services.scoring_engine import ScoringEngine
from app.services.ai_provider import get_ai_provider
from app.services.kb_loader import kb

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_github_profile(
    request: AnalyzeRequest,
    db: AsyncSession = Depends(get_db),
) -> AnalyzeResponse:
    """
    Analyze a GitHub user's profile for a specific role and level.

    Pipeline:
    1. Validate role & level parameters
    2. Extract GitHub username from input
    3. Fetch public repos via GitHub REST API
    4. Filter repos by role relevance
    5. Fetch content of relevant files
    6. Detect evidence (keyword + optional AI)
    7. Calculate scores via dynamic scoring engine
    8. Save results to database
    9. Return structured response
    """
    # 1. Validate role and level in KB
    if request.role_id not in kb.role_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown role: '{request.role_id}'. Available roles: {kb.role_categories}",
        )

    role_def = kb.get_role(request.role_id, request.level)
    if not role_def:
        raise HTTPException(
            status_code=400,
            detail=f"Level '{request.level}' not found for role '{request.role_id}'",
        )

    try:
        # Step 2: Extract username
        try:
            username = extract_username(request.github_username)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        logger.info(f"Starting analysis for {username} as {request.role_id}/{request.level}")

        # Step 3: Fetch repos from GitHub
        fetcher = GitHubFetcher(token=request.github_token)
        repos = await fetcher.fetch_user_repos(username)

        if not repos:
            raise HTTPException(status_code=404, detail=f"No public repositories found for user '{username}'")

        # Step 4: Filter by role
        role_filter = RoleFilter(kb, request.role_id)
        filtered_repos = role_filter.filter_repos(repos)

        # Step 5: Fetch content of relevant files
        files_to_fetch = role_filter.get_files_to_fetch_content(filtered_repos)
        for repo_full_name, file_paths in files_to_fetch.items():
            contents = await fetcher.fetch_specific_files(repo_full_name, file_paths)
            # Attach contents to the corresponding FilteredRepo
            for f_repo in filtered_repos:
                if f_repo.full_name == repo_full_name:
                    f_repo.file_contents = contents
                    break

        # Step 6: Detect evidence
        detector = EvidenceDetector(kb, request.role_id)
        evidence = detector.detect_all(filtered_repos)

        # Optional: AI enrichment
        if request.use_ai:
            ai_provider = get_ai_provider()
            unevidenced = [
                key for key, result in evidence.items()
                if result.status == "not_yet_evidenced"
            ]
            if unevidenced:
                ai_data = _prepare_ai_data(filtered_repos)
                ai_results = await ai_provider.analyze_evidence(
                    request.role_id, request.level, unevidenced, ai_data
                )
                _merge_ai_results(evidence, ai_results)

        # Step 7: Calculate scores via dynamic scoring engine
        engine = ScoringEngine(kb, request.role_id, request.level)
        scoring_result = engine.calculate_all(evidence)

        # Step 8: Save to database
        analysis = await _save_analysis(
            db, username, request, scoring_result, filtered_repos, evidence
        )

        # Step 9: Build response
        role_title = role_def.get("title", f"{request.level.capitalize()} {request.role_id}")
        return _build_response(analysis.id, username, request, role_title, scoring_result, filtered_repos)

    except RoleGaugeException as e:
        logger.warning(f"Analysis error for {request.github_username}: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Analysis failed unexpectedly for {request.github_username}")
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
    username: str,
    request: AnalyzeRequest,
    scoring_result: dict,
    filtered_repos: list,
    evidence: dict,
) -> Analysis:
    """Save analysis results to PostgreSQL."""
    analysis = Analysis(
        github_username=username,
        role_id=request.role_id,
        level=request.level,
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        total_repos_scanned=len(filtered_repos),
        relevant_repos_found=sum(1 for r in filtered_repos if r.is_relevant),
        ai_provider_used=request.use_ai and "openai" or "none",
    )
    db.add(analysis)
    await db.flush()  # Get the ID

    # Save skill results
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

        # Save subskill results
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

    # Save repo data
    for repo in filtered_repos:
        repo_evidence = []
        for composite_key, ev in evidence.items():
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
    analysis_id,
    username: str,
    request: AnalyzeRequest,
    role_title: str,
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

    from datetime import datetime, timezone

    return AnalyzeResponse(
        id=str(analysis_id),
        github_username=username,
        role_id=request.role_id,
        role_name=role_title,
        level=request.level,
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        readiness_label=scoring_result["readiness_label"],
        total_repos_scanned=len(filtered_repos),
        relevant_repos_found=sum(1 for r in filtered_repos if r.is_relevant),
        skills=skills,
        repos=repos,
        created_at=datetime.now(timezone.utc),
    )
