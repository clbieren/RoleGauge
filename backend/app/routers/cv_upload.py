"""
CV Upload Router.
POST /api/cv/upload — Upload and analyze a CV (PDF or DOCX).

Pipeline:
1. Validate file type and size
2. Parse CV via cv_parser (rule-based, no AI)
3. Match skills via cv_skill_matcher
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
    CVCertificateMatch,
    CVParsedData,
    CVProjectData,
    CVScoringPreview,
    CVSkillMatch,
    CVUploadResponse,
    SkillScore,
    SubskillEvidence,
)
from app.services.cv_certification_matcher import (
    CertificationIndex,
    CertificationMatcher,
    get_certification_index,
)
from app.services.cv_parser import parse_cv
from app.services.cv_skill_matcher import CVSkillMatcher
from app.services.kb_loader import kb
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["cv"])


def _ensure_cert_index_built() -> CertificationIndex:
    """Ensure the certification index is built (lazy initialization)."""
    cert_index = get_certification_index()
    if not cert_index._built:
        cert_index.build(kb)
        logger.info("Certification index built on first CV upload")
    return cert_index


@router.post("/cv/upload", response_model=CVUploadResponse)
async def upload_cv(
    file: UploadFile = File(..., description="CV file (PDF or DOCX, max 10MB)"),
    role_id: str = Form(..., description="Target role category (e.g. 'backend', 'devops')"),
    level: str = Form("mid", description="Target seniority level ('junior', 'mid', 'senior')"),
) -> CVUploadResponse:
    """
    Upload a CV file and get structured parsing, skill matching,
    certification classification, and scoring preview.

    Accepts only PDF and DOCX files up to 10MB.
    """
    # ── Step 1: Validate ──

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

    # Validate file extension
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required.")

    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in settings.CV_ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: '{file_ext}'. Only PDF and DOCX are accepted.",
        )

    # Validate file size (read content)
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
            suffix=file_ext, delete=False, prefix="rolegauge_cv_"
        ) as tmp:
            tmp.write(content)
            temp_path = tmp.name

        logger.info(f"CV uploaded: {file.filename} ({len(content)} bytes) → {temp_path}")

        # Parse CV
        parsed = parse_cv(temp_path)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"CV parsing failed for {file.filename}")
        raise HTTPException(status_code=500, detail=f"CV parsing failed: {str(e)}")
    finally:
        # Always clean up temp file
        if temp_path and os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
                logger.debug(f"Temp file deleted: {temp_path}")
            except OSError as e:
                logger.warning(f"Failed to delete temp file {temp_path}: {e}")

    # ── Step 3: Match skills ──
    skill_matcher = CVSkillMatcher(kb, role_id)
    evidence = skill_matcher.match_all(parsed)

    # Build skill match list for response
    skill_matches: list[CVSkillMatch] = []
    seen_matches: set[str] = set()  # Deduplicate
    for composite_key, result in evidence.items():
        if result.status == "claimed":
            for signal in result.signals:
                match_key = f"{composite_key}:{signal.source}:{signal.matched_text}"
                if match_key not in seen_matches:
                    seen_matches.add(match_key)
                    # Determine matched_from from source type
                    source_to_from = {
                        "cv_skills_list": "skills_list",
                        "cv_project": "project",
                        "cv_experience": "experience",
                        "cv_signal_pattern": "signal_pattern",
                    }
                    skill_matches.append(CVSkillMatch(
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
        CVCertificateMatch(
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
            from app.services.evidence_detector import EvidenceSignal
            for composite_key in cert_match["matched_composite_keys"]:
                if composite_key in evidence:
                    evidence[composite_key].signals.append(EvidenceSignal(
                        source="cv_certification",
                        file_path="cv/certifications",
                        matched_text=cert_match["certificate_name"],
                        strength=cert_match["strength"],
                    ))
                    if evidence[composite_key].status == "not_yet_evidenced":
                        evidence[composite_key].status = "claimed"

    # ── Step 5: Run scoring preview ──
    engine = ScoringEngine(kb, role_id, level)
    scoring_result = engine.calculate_all(evidence)

    # Build response
    parsed_cv = CVParsedData(
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
        detected_sections=parsed.get("detected_sections", []),
    )

    scoring_preview = CVScoringPreview(
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
        f"CV analysis complete for role '{role_id}/{level}': "
        f"{len(skill_matches)} skill matches, "
        f"{len(certificate_matches)} cert matches, "
        f"readiness={scoring_result['readiness_score']:.4f} ({scoring_result['readiness_tier']})"
    )

    return CVUploadResponse(
        parsed_cv=parsed_cv,
        skill_matches=skill_matches,
        certificate_matches=certificate_matches,
        scoring_preview=scoring_preview,
    )
