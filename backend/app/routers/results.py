"""
Results Router.
GET /api/results/{id} — Retrieve a saved analysis result.
"""

import uuid
import logging

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.dependencies.auth import get_optional_user
from app.exceptions import AnalysisNotFoundError, RoleGaugeException
from app.models.db_models import Analysis, RepoData, SkillResult, SubskillResult, User
from app.models.schemas import (
    AnalyzeResponse,
    RepoInfo,
    SkillScore,
    SubskillEvidence,
    resolve_ad_placements,
)
from app.services.kb_loader import kb
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["results"])


@router.get("/results/{analysis_id}", response_model=AnalyzeResponse)
async def get_result(
    analysis_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user),
) -> AnalyzeResponse:
    """Retrieve a previously saved analysis result by UUID."""
    try:
        parsed_id = uuid.UUID(analysis_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid analysis ID format: '{analysis_id}'. Must be a valid UUID."
        )

    try:
        # Load analysis with all relationships
        stmt = (
            select(Analysis)
            .options(
                selectinload(Analysis.skill_results).selectinload(SkillResult.subskill_results),
                selectinload(Analysis.repo_data),
            )
            .where(Analysis.id == parsed_id)
        )
        result = await db.execute(stmt)
        analysis = result.scalar_one_or_none()

        if not analysis:
            raise AnalysisNotFoundError(analysis_id)

        # Authorization check: private analyses are only visible to their creator
        if analysis.user_id is not None:
            if not current_user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Authentication required to view this analysis.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            if current_user.id != analysis.user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You do not have permission to view this analysis.",
                )

        # Build response from DB data
        role_def = kb.get_role(analysis.role_id, analysis.level)
        role_title = role_def.get("title", analysis.role_id) if role_def else analysis.role_id

        # Get readiness label from scoring engine instance
        engine = ScoringEngine(kb, analysis.role_id, analysis.level)
        tier_info = engine._get_readiness_tier(analysis.readiness_score)

        skills = []
        for sr in analysis.skill_results:
            subskills = [
                SubskillEvidence(
                    composite_key=sub.composite_key,
                    subskill_name=sub.subskill_name,
                    confidence=sub.confidence,
                    status=sub.status,
                    evidence_sources=sub.evidence_sources or [],
                )
                for sub in sr.subskill_results
            ]
            skills.append(SkillScore(
                skill_id=sr.skill_id,
                skill_name=sr.skill_name,
                score=sr.score,
                importance=sr.importance,
                subskills=subskills,
            ))

        repos = [
            RepoInfo(
                repo_name=rd.repo_name,
                repo_url=rd.repo_url,
                description=rd.description,
                primary_language=rd.primary_language,
                languages=rd.languages or {},
                stars=rd.stars,
                forks=rd.forks,
                topics=rd.topics or [],
                is_relevant=rd.is_relevant,
                relevant_files_count=rd.relevant_files_count,
                evidence_found=rd.evidence_found or [],
            )
            for rd in analysis.repo_data
        ]

        analysis_tier, ad_placements = resolve_ad_placements(current_user)

        return AnalyzeResponse(
            id=str(analysis.id),
            github_username=analysis.github_username,
            role_id=analysis.role_id,
            role_name=role_title,
            level=analysis.level,
            readiness_score=analysis.readiness_score,
            readiness_tier=analysis.readiness_tier,
            readiness_label=tier_info["label"],
            total_repos_scanned=analysis.total_repos_scanned,
            relevant_repos_found=analysis.relevant_repos_found,
            has_cv=analysis.github_username == "cv_upload",
            has_linkedin=False,
            ai_enrichment_available=False,
            analysis_tier=analysis_tier,
            ad_placements=ad_placements,
            skills=skills,
            repos=repos,
            created_at=analysis.created_at,
        )

    except RoleGaugeException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Error retrieving analysis result for {analysis_id}")
        raise HTTPException(status_code=500, detail=f"Database retrieval failed: {str(e)}")
