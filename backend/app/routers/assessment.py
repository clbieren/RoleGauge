"""
Assessment Router.
Endpoints for starting adaptive Q&A assessments and evaluating candidate submissions.

POST /api/assessment/start  -> Selects targeted questions, creates session.
POST /api/assessment/submit -> Evaluates answers, fuses assessment signals into EvidenceEngine,
                               recalculates readiness score, updates database, and returns results.
"""

import logging
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.dependencies.auth import get_optional_user
from app.exceptions import AnalysisNotFoundError, RoleGaugeException
from app.models.db_models import Analysis, AssessmentSession, RepoData, SkillResult, SubskillResult, User
from app.models.schemas import (
    AnalyzeResponse,
    AssessmentAnswerItem,
    AssessmentQuestionEvaluation,
    AssessmentQuestionPublic,
    AssessmentStartRequest,
    AssessmentStartResponse,
    AssessmentSubmitRequest,
    AssessmentSubmitResponse,
    RepoInfo,
    SkillScore,
    SubskillEvidence,
    resolve_ad_placements,
)
from app.services.assessment_evaluator import AssessmentEvaluator
from app.services.assessment_selector import AssessmentSelector
from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.evidence_engine import EvidenceEngine
from app.services.kb_loader import kb
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/assessment", tags=["assessment"])


@router.post("/start", response_model=AssessmentStartResponse)
async def start_assessment(
    req: AssessmentStartRequest,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user),
) -> AssessmentStartResponse:
    """
    Start an adaptive assessment session.
    Selects prioritized questions based on existing analysis signals.
    CRITICAL: expected_answer_keywords are strictly kept server-side and omitted from output.
    """
    analysis: Optional[Analysis] = None

    # Option 1: Load via analysis_id
    if req.analysis_id:
        try:
            parsed_id = uuid.UUID(req.analysis_id)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid analysis_id UUID format: '{req.analysis_id}'")

        stmt = (
            select(Analysis)
            .options(
                selectinload(Analysis.skill_results).selectinload(SkillResult.subskill_results),
            )
            .where(Analysis.id == parsed_id)
        )
        res = await db.execute(stmt)
        analysis = res.scalar_one_or_none()
        if not analysis:
            raise HTTPException(status_code=404, detail=f"Analysis '{req.analysis_id}' not found.")

        role_id = analysis.role_id
        level = analysis.level

    # Option 2: Start fresh for github_username + role_id
    elif req.role_id:
        role_id = req.role_id
        level = req.level or "mid"
        username = req.github_username or "anonymous"

        if role_id not in kb.role_categories:
            raise HTTPException(status_code=400, detail=f"Unknown role: '{role_id}'")

        # Check if an existing analysis already exists for this user/role
        stmt = (
            select(Analysis)
            .options(
                selectinload(Analysis.skill_results).selectinload(SkillResult.subskill_results),
            )
            .where(
                Analysis.github_username == username,
                Analysis.role_id == role_id,
                Analysis.level == level,
            )
            .order_by(Analysis.created_at.desc())
        )
        res = await db.execute(stmt)
        analysis = res.scalar_one_or_none()

        # If no analysis exists yet, initialize a baseline analysis
        if not analysis:
            engine = ScoringEngine(kb, role_id, level)
            empty_evidence = {}
            for s_id, s_data in kb.get_skills_for_role(role_id).items():
                for sub in s_data.get("subskills", []):
                    ck = f"{s_id}.{sub['id']}"
                    empty_evidence[ck] = SubskillEvidenceResult(
                        composite_key=ck,
                        subskill_name=sub.get("name", sub["id"]),
                        status="not_yet_evidenced",
                        signals=[],
                    )

            scoring_res = engine.calculate_all(empty_evidence)
            analysis = Analysis(
                github_username=username,
                role_id=role_id,
                level=level,
                readiness_score=scoring_res["readiness_score"],
                readiness_tier=scoring_res["readiness_tier"],
                total_repos_scanned=0,
                relevant_repos_found=0,
                ai_provider_used="none",
            )
            db.add(analysis)
            await db.flush()

            for s_data in scoring_res["skills"]:
                sk_res = SkillResult(
                    analysis_id=analysis.id,
                    skill_id=s_data["skill_id"],
                    skill_name=s_data["skill_name"],
                    score=s_data["score"],
                    importance=s_data["importance"],
                )
                db.add(sk_res)
                await db.flush()

                for sub in s_data["subskills"]:
                    sub_res = SubskillResult(
                        skill_result_id=sk_res.id,
                        composite_key=sub["composite_key"],
                        subskill_name=sub["subskill_name"],
                        confidence=sub["confidence"],
                        status=sub["status"],
                        evidence_sources=[],
                    )
                    db.add(sub_res)
            await db.commit()

        # Reload analysis with relationships eager-loaded
        stmt = (
            select(Analysis)
            .options(
                selectinload(Analysis.skill_results).selectinload(SkillResult.subskill_results),
            )
            .where(Analysis.id == analysis.id)
        )
        res = await db.execute(stmt)
        analysis = res.scalar_one()
    else:
        raise HTTPException(
            status_code=400,
            detail="Either 'analysis_id' or 'role_id' must be provided to start an assessment.",
        )

    # Build subskills evidence map from the loaded analysis
    subskills_map: dict[str, dict[str, Any]] = {}
    for sk in analysis.skill_results:
        for sub in sk.subskill_results:
            subskills_map[sub.composite_key] = {
                "confidence": sub.confidence,
                "status": sub.status,
                "subskill_name": sub.subskill_name,
            }

    # Select questions using AssessmentSelector
    selector = AssessmentSelector(kb)
    selected_questions = selector.select_questions(
        role_id=role_id,
        level=level,
        subskills_evidence=subskills_map,
        voluntary_composite_keys=req.voluntary_composite_keys,
        max_questions=req.max_questions,
    )

    if not selected_questions:
        raise HTTPException(
            status_code=404,
            detail=f"No suitable assessment questions found for role '{role_id}' (level: '{level}').",
        )

    # Persist AssessmentSession
    session_user_id = current_user.id if current_user else analysis.user_id
    session = AssessmentSession(
        user_id=session_user_id,
        analysis_id=analysis.id,
        role_id=role_id,
        level=level,
        questions_data=[q.to_internal_dict() for q in selected_questions],
        status="active",
    )
    db.add(session)
    await db.commit()
    await db.refresh(session)

    # Public question list (strict exclusion of expected_answer_keywords)
    public_questions = [
        AssessmentQuestionPublic(
            composite_key=q.composite_key,
            subskill_name=q.subskill_name,
            question=q.question,
            type=q.type,
            level=q.level,
        )
        for q in selected_questions
    ]

    return AssessmentStartResponse(
        assessment_session_id=str(session.id),
        analysis_id=str(analysis.id),
        role_id=role_id,
        level=level,
        total_questions=len(public_questions),
        questions=public_questions,
    )


@router.post("/submit", response_model=AssessmentSubmitResponse)
async def submit_assessment(
    req: AssessmentSubmitRequest,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user),
) -> AssessmentSubmitResponse:
    """
    Submit candidate answers for an active assessment session.
    Evaluates responses with rule-based keyword matching, merges verified signals into EvidenceEngine,
    recalculates scoring with ScoringEngine, updates database, and returns updated analysis.
    """
    try:
        session_id = uuid.UUID(req.assessment_session_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid assessment_session_id UUID format: '{req.assessment_session_id}'",
        )

    # Load AssessmentSession with associated Analysis and Subskill results
    stmt = (
        select(AssessmentSession)
        .options(
            selectinload(AssessmentSession.analysis)
            .selectinload(Analysis.skill_results)
            .selectinload(SkillResult.subskill_results),
            selectinload(AssessmentSession.analysis).selectinload(Analysis.repo_data),
        )
        .where(AssessmentSession.id == session_id)
    )
    res = await db.execute(stmt)
    session = res.scalar_one_or_none()

    if not session:
        raise HTTPException(
            status_code=404,
            detail=f"Assessment session '{req.assessment_session_id}' not found.",
        )

    analysis = session.analysis
    if not analysis:
        raise HTTPException(
            status_code=404,
            detail=f"Associated analysis for session '{req.assessment_session_id}' not found.",
        )

    # Normalize answers input (dict or list of AssessmentAnswerItem)
    answers_dict: dict[str, str] = {}
    if isinstance(req.answers, dict):
        answers_dict = {str(k): str(v) for k, v in req.answers.items()}
    elif isinstance(req.answers, list):
        for item in req.answers:
            if isinstance(item, AssessmentAnswerItem):
                answers_dict[item.composite_key] = item.answer
            elif isinstance(item, dict):
                answers_dict[item.get("composite_key", "")] = item.get("answer", "")

    # Step 1: Evaluate answers using rule-based AssessmentEvaluator
    evaluator = AssessmentEvaluator(kb)
    eval_results = evaluator.evaluate_all(
        questions_data=session.questions_data,
        user_answers=answers_dict,
    )

    # Step 2: Build assessment_evidence dictionary for EvidenceEngine
    assessment_evidence: dict[str, list[dict[str, Any]]] = {}
    for ev in eval_results:
        assessment_evidence[ev.composite_key] = [
            {
                "status": ev.status,
                "strength": ev.strength,
                "score": ev.score,
                "detail": ev.feedback,
                "type": ev.question_type,
            }
        ]

    # Step 3: Reconstruct existing non-assessment evidence signals from DB
    existing_github_signals: dict[str, SubskillEvidenceResult] = {}
    existing_cv_signals: dict[str, SubskillEvidenceResult] = {}
    existing_linkedin_signals: dict[str, SubskillEvidenceResult] = {}

    for sk_res in analysis.skill_results:
        for sub_res in sk_res.subskill_results:
            ck = sub_res.composite_key
            sources = sub_res.contributing_sources or sub_res.evidence_sources or []
            
            gh_sigs: list[EvidenceSignal] = []
            cv_sigs: list[EvidenceSignal] = []
            li_sigs: list[EvidenceSignal] = []

            if isinstance(sources, list):
                for src in sources:
                    if isinstance(src, dict):
                        s_name = src.get("source", "")
                        # Filter out prior assessment signals so we don't duplicate
                        if s_name == "assessment":
                            continue
                        sig = EvidenceSignal(
                            source=s_name,
                            file_path=src.get("file_path", ""),
                            matched_text=src.get("signal", src.get("matched_text", "")),
                            strength=float(src.get("strength", 0.5)),
                        )
                        if s_name in ("cv_skills_list", "cv_experience", "cv_project", "cv_education", "cv_certification"):
                            cv_sigs.append(sig)
                        elif s_name.startswith("linkedin_"):
                            li_sigs.append(sig)
                        else:
                            gh_sigs.append(sig)

            if gh_sigs:
                existing_github_signals[ck] = SubskillEvidenceResult(
                    composite_key=ck,
                    subskill_name=sub_res.subskill_name,
                    status="evidence_found",
                    signals=gh_sigs,
                )
            if cv_sigs:
                existing_cv_signals[ck] = SubskillEvidenceResult(
                    composite_key=ck,
                    subskill_name=sub_res.subskill_name,
                    status="claimed",
                    signals=cv_sigs,
                )
            if li_sigs:
                existing_linkedin_signals[ck] = SubskillEvidenceResult(
                    composite_key=ck,
                    subskill_name=sub_res.subskill_name,
                    status="claimed",
                    signals=li_sigs,
                )

    # Step 4: Multi-source Fusion via EvidenceEngine (feeding REAL assessment_evidence)
    evidence_engine = EvidenceEngine(kb, analysis.role_id, analysis.level)
    unified_evidence = evidence_engine.merge_evidence(
        github_evidence=existing_github_signals or None,
        cv_skills_evidence=existing_cv_signals or None,
        linkedin_evidence=existing_linkedin_signals or None,
        assessment_evidence=assessment_evidence,
    )

    # Step 5: ScoringEngine calculation
    scoring_evidence = {
        ck: u.to_subskill_evidence_result() for ck, u in unified_evidence.items()
    }
    scoring_engine = ScoringEngine(kb, analysis.role_id, analysis.level)
    scoring_result = scoring_engine.calculate_all(scoring_evidence)

    # Step 6: Update database records
    analysis.readiness_score = scoring_result["readiness_score"]
    analysis.readiness_tier = scoring_result["readiness_tier"]

    # Update skill and subskill results
    for sk_data in scoring_result["skills"]:
        sk_id = sk_data["skill_id"]
        # Find matching SkillResult
        for sk_res in analysis.skill_results:
            if sk_res.skill_id == sk_id:
                sk_res.score = sk_data["score"]
                # Update SubskillResults
                for sub_data in sk_data["subskills"]:
                    ck = sub_data["composite_key"]
                    for sub_res in sk_res.subskill_results:
                        if sub_res.composite_key == ck:
                            sub_res.confidence = sub_data["confidence"]
                            sub_res.status = sub_data["status"]
                            sub_res.contributing_sources = sub_data.get("contributing_sources", [])
                            sub_res.ceiling_applied = sub_data.get("ceiling_applied")
                            sub_res.calculation_trace = sub_data.get("calculation_trace")
                            break
                break

    # Mark session completed and save answers
    session.answers_data = answers_dict
    session.status = "completed"
    await db.commit()

    # Step 7: Build response
    role_def = kb.get_role(analysis.role_id, analysis.level)
    role_title = role_def.get("title", analysis.role_id) if role_def else analysis.role_id

    public_evaluations = [
        AssessmentQuestionEvaluation(
            composite_key=ev.composite_key,
            subskill_name=ev.subskill_name,
            question=ev.question,
            type=ev.question_type,
            verdict=ev.verdict,
            status=ev.status,
            score=ev.score,
            strength=ev.strength,
            match_ratio=ev.match_ratio,
            matched_keywords_count=len(ev.matched_keywords),
            total_keywords_count=ev.total_keywords,
            feedback=ev.feedback,
        )
        for ev in eval_results
    ]

    summary = {
        "total": len(eval_results),
        "correct": sum(1 for e in eval_results if e.verdict == "correct"),
        "partial": sum(1 for e in eval_results if e.verdict == "partial"),
        "incorrect": sum(1 for e in eval_results if e.verdict == "incorrect"),
    }

    # Build AnalyzeResponse
    skills_response: list[SkillScore] = []
    for sk_data in scoring_result["skills"]:
        subskills_list = [
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
            for sub in sk_data["subskills"]
        ]
        skills_response.append(SkillScore(
            skill_id=sk_data["skill_id"],
            skill_name=sk_data["skill_name"],
            score=sk_data["score"],
            importance=sk_data["importance"],
            subskills=subskills_list,
        ))

    repos_response = [
        RepoInfo(
            repo_name=r.repo_name,
            repo_url=r.repo_url,
            description=r.description,
            primary_language=r.primary_language,
            languages=r.languages or {},
            stars=r.stars,
            forks=r.forks,
            topics=r.topics or [],
            is_relevant=r.is_relevant,
            relevant_files_count=r.relevant_files_count,
            evidence_found=r.evidence_found or [],
        )
        for r in (analysis.repo_data or [])
    ]

    analysis_tier, ad_placements = resolve_ad_placements(current_user)

    updated_analysis = AnalyzeResponse(
        id=str(analysis.id),
        github_username=analysis.github_username,
        role_id=analysis.role_id,
        role_name=role_title,
        level=analysis.level,
        readiness_score=scoring_result["readiness_score"],
        readiness_tier=scoring_result["readiness_tier"],
        readiness_label=scoring_result["readiness_label"],
        total_repos_scanned=analysis.total_repos_scanned,
        relevant_repos_found=analysis.relevant_repos_found,
        has_cv=analysis.github_username == "cv_upload",
        has_linkedin=False,
        ai_enrichment_available=False,
        analysis_tier=analysis_tier,
        ad_placements=ad_placements,
        skills=skills_response,
        repos=repos_response,
        created_at=analysis.created_at,
    )

    return AssessmentSubmitResponse(
        assessment_session_id=str(session.id),
        analysis_id=str(analysis.id),
        evaluations=public_evaluations,
        summary=summary,
        updated_analysis=updated_analysis,
    )
