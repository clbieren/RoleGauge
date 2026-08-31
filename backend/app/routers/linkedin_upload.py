"""
LinkedIn Upload Router.
POST /api/linkedin/upload — Upload and analyze a LinkedIn Profile PDF export ("Save to PDF").

Pipeline:
1. Validate file type (PDF only) and size (<= 10MB)
2. Parse LinkedIn PDF via cv_parser with source_type="linkedin"
3. Match skills and experience via linkedin_skill_matcher
4. Match certificates via cv_certification_matcher (allowlist, 3-way classification)
5. Run scoring preview via scoring_engine
6. Clean up temp file
7. Return structured response
"""

import logging
import os
import tempfile
from typing import Any

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.config import settings
from app.models.schemas import (
    CVCertificateData,
    CVProjectData,
    LinkedInCertificateMatch,
    LinkedInParsedData,
    LinkedInScoringPreview,
    LinkedInSkillMatch,
    LinkedInUploadResponse,
    SkillScore,
    SubskillEvidence,
)
from app.services.cv_certification_matcher import (
    CertificationIndex,
    CertificationMatcher,
    get_certification_index,
)
from app.services.cv_parser import parse_cv
from app.services.evidence_detector import EvidenceSignal
from app.services.kb_loader import kb
from app.services.linkedin_skill_matcher import LinkedInSkillMatcher
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["linkedin"])


def _ensure_cert_index_built() -> CertificationIndex:
    """Ensure the certification index is built (lazy initialization)."""
    cert_index = get_certification_index()
    if not cert_index._built:
        cert_index.build(kb)
        logger.info("Certification index built on first LinkedIn upload")
    return cert_index


@router.post("/linkedin/upload", response_model=LinkedInUploadResponse)
async def upload_linkedin(
    file: UploadFile = File(..., description="LinkedIn profile export (PDF only, max 10MB)"),
    role_id: str = Form(..., description="Target role category (e.g. 'backend', 'devops')"),
    level: str = Form("mid", description="Target seniority level ('junior', 'mid', 'senior')"),
) -> LinkedInUploadResponse:
    """
    Upload a LinkedIn Profile PDF ("Save to PDF") and get structured parsing,
    skill matching, certification classification, and scoring preview.

    Accepts only PDF files up to 10MB.
    """
    # ── Step 1: Validate Inputs ──

    # Validate role
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

    # Validate file extension (LinkedIn imports must be PDF)
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required.")

    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext != ".pdf":
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: '{file_ext}'. LinkedIn import requires PDF files exported via 'Save to PDF'.",
        )

    # Validate file size
    content = await file.read()
    if len(content) > settings.CV_MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large: {len(content)} bytes. Maximum allowed: {settings.CV_MAX_FILE_SIZE} bytes (10MB).",
        )

    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # ── Step 2: Save to temp file and parse ──
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".pdf", delete=False, prefix="rolegauge_linkedin_"
        ) as tmp:
            tmp.write(content)
            temp_path = tmp.name

        logger.info(f"LinkedIn PDF uploaded: {file.filename} ({len(content)} bytes) → {temp_path}")

        # Parse with source_type="linkedin"
        parsed = parse_cv(temp_path, source_type="linkedin")

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"LinkedIn PDF parsing failed for {file.filename}")
        raise HTTPException(status_code=500, detail=f"LinkedIn parsing failed: {str(e)}")
    finally:
        # Always clean up temp file
        if temp_path and os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
                logger.debug(f"Temp file deleted: {temp_path}")
            except OSError as e:
                logger.warning(f"Failed to delete temp file {temp_path}: {e}")

    # ── Step 3: Match skills ──
    skill_matcher = LinkedInSkillMatcher(kb, role_id)
    evidence = skill_matcher.match_all(parsed)

    # Build skill match list for response
    skill_matches: list[LinkedInSkillMatch] = []
    seen_matches: set[str] = set()
    for composite_key, result in evidence.items():
        if result.status == "claimed":
            for signal in result.signals:
                match_key = f"{composite_key}:{signal.source}:{signal.matched_text}"
                if match_key not in seen_matches:
                    seen_matches.add(match_key)
                    source_to_from = {
                        "linkedin_skills": "skills",
                        "linkedin_experience": "experience",
                        "linkedin_summary": "summary",
                        "linkedin_project": "project",
                        "linkedin_recommendation": "recommendations",
                        "linkedin_post": "posts_articles",
                        "linkedin_signal_pattern": "signal_pattern",
                    }
                    skill_matches.append(LinkedInSkillMatch(
                        composite_key=composite_key,
                        matched_from=source_to_from.get(signal.source, signal.source),
                        matched_term=signal.matched_text,
                        status="claimed",
                        strength=round(signal.strength, 4),
                    ))

    # ── Step 4: Match certificates ──
    cert_index = _ensure_cert_index_built()
    cert_matcher = CertificationMatcher(kb, cert_index, role_id)
    cert_results = cert_matcher.match_certificates(parsed.get("certificates", []))

    certificate_matches = [
        LinkedInCertificateMatch(
            certificate_name=cr["certificate_name"],
            classification=cr["classification"],
            matched_composite_keys=cr["matched_composite_keys"],
            score_contribution=cr["score_contribution"],
            matched_from_role=cr.get("matched_from_role"),
            category_group=cr.get("category_group"),
        )
        for cr in cert_results
    ]

    # Inject recognized_relevant cert signals into evidence for scoring
    for cert_match in cert_results:
        if cert_match["classification"] == "recognized_relevant" and cert_match["matched_composite_keys"]:
            for composite_key in cert_match["matched_composite_keys"]:
                if composite_key in evidence:
                    evidence[composite_key].signals.append(EvidenceSignal(
                        source="linkedin_certification",
                        file_path="linkedin/certifications",
                        matched_text=cert_match["certificate_name"],
                        strength=cert_match["strength"],
                    ))
                    if evidence[composite_key].status == "not_yet_evidenced":
                        evidence[composite_key].status = "claimed"

    # ── Step 5: Run scoring preview ──
    engine = ScoringEngine(kb, role_id, level)
    scoring_result = engine.calculate_all(evidence)

    # Build response
    parsed_linkedin = LinkedInParsedData(
        personal_info=parsed.get("personal_info", {}),
        education=parsed.get("education", []),
        experience=parsed.get("experience", []),
        projects=[
            CVProjectData(
                name=p.get("name", ""),
                description=p.get("description", ""),
                skills_mentioned=p.get("skills_mentioned", []),
            )
            for p in parsed.get("projects", [])
        ],
        skills=parsed.get("skills", []),
        certificates=[
            CVCertificateData(
                name=c.get("name", ""),
                provider=c.get("provider", ""),
            )
            for c in parsed.get("certificates", [])
        ],
        languages=parsed.get("languages", []),
        volunteering=parsed.get("volunteering", []),
        honors_awards=parsed.get("honors_awards", []),
        publications=parsed.get("publications", []),
        recommendations=parsed.get("recommendations", []),
        detected_sections=parsed.get("detected_sections", []),
    )

    scoring_preview = LinkedInScoringPreview(
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        readiness_label=scoring_result["readiness_label"],
        skills=[
            SkillScore(
                skill_id=s["skill_id"],
                skill_name=s["skill_name"],
                score=s["score"],
                importance=s["importance"],
                subskills=[
                    SubskillEvidence(
                        composite_key=sub["composite_key"],
                        subskill_name=sub["subskill_name"],
                        confidence=sub["confidence"],
                        status=sub["status"],
                        evidence_sources=sub.get("evidence_sources", []),
                    )
                    for sub in s["subskills"]
                ],
            )
            for s in scoring_result["skills"]
        ],
    )

    logger.info(
        f"LinkedIn analysis complete for role '{role_id}/{level}': "
        f"{len(skill_matches)} skill matches, "
        f"{len(certificate_matches)} cert matches, "
        f"readiness={scoring_result['readiness_score']:.4f} ({scoring_result['readiness_tier']})"
    )

    return LinkedInUploadResponse(
        parsed_linkedin=parsed_linkedin,
        skill_matches=skill_matches,
        certificate_matches=certificate_matches,
        scoring_preview=scoring_preview,
    )
