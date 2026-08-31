"""
Users Router.
Provides user-specific endpoints, such as retrieving the authenticated user's analysis history.

Endpoints:
- GET /api/users/me/analyses -> List all past analyses executed by the current user
"""

import logging
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.db_models import Analysis, User
from app.models.schemas import UserAnalysisSummary
from app.services.kb_loader import kb
from app.services.scoring_engine import ScoringEngine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/users", tags=["users"])


@router.get(
    "/me/analyses",
    response_model=list[UserAnalysisSummary],
    summary="Get current user's analysis history",
)
async def get_my_analyses(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> list[UserAnalysisSummary]:
    """
    Retrieve all historical analysis results associated with the authenticated user,
    sorted with the most recent analysis first.
    """
    stmt = (
        select(Analysis)
        .where(Analysis.user_id == current_user.id)
        .order_by(Analysis.created_at.desc())
    )
    res = await db.execute(stmt)
    analyses = res.scalars().all()

    results: list[UserAnalysisSummary] = []
    for a in analyses:
        role_def = kb.get_role(a.role_id, a.level)
        role_title = role_def.get("title", a.role_id) if role_def else a.role_id

        engine = ScoringEngine(kb, a.role_id, a.level)
        tier_info = engine._get_readiness_tier(a.readiness_score)

        results.append(
            UserAnalysisSummary(
                id=str(a.id),
                github_username=a.github_username,
                role_id=a.role_id,
                role_name=role_title,
                level=a.level,
                readiness_score=a.readiness_score,
                readiness_tier=a.readiness_tier,
                readiness_label=tier_info["label"],
                created_at=a.created_at,
            )
        )

    logger.info(f"Retrieved {len(results)} analyses for user {current_user.email}")
    return results
