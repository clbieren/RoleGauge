"""
Roles Router.
GET /api/roles — Lists all available roles from the knowledge base.
"""

import re
from fastapi import APIRouter

from app.models.schemas import RolesListResponse, RoleInfo
from app.services.kb_loader import kb

router = APIRouter(prefix="/api", tags=["roles"])


@router.get("/roles", response_model=RolesListResponse)
async def list_roles() -> RolesListResponse:
    """
    List all available roles with their metadata.
    Reads from the knowledge base (roles and skills directories).
    """
    roles = []

    for category in sorted(kb.role_categories):
        # Get any level definition for basic role info
        role_def = (
            kb.get_role(category, "junior")
            or kb.get_role(category, "mid")
            or kb.get_role(category, "senior")
        )

        # Count skills
        skills_count = len(kb.get_skills_for_role(category))

        # Available levels
        levels = list(kb.roles.get(category, {}).keys()) or ["junior", "mid", "senior"]

        raw_title = (
            role_def.get("title", category.replace("-", " ").title())
            if role_def
            else category.replace("-", " ").title()
        )
        # Strip level prefix (Junior, Mid, Senior) so roles are presented cleanly
        clean_title = re.sub(r"^(junior|mid|senior)\s+", "", raw_title, flags=re.IGNORECASE)
        description = role_def.get("description", "") if role_def else f"{clean_title} skills and competencies"

        roles.append(RoleInfo(
            role_id=category,
            title=clean_title,
            description=description,
            category=category,
            levels=sorted(levels),
            skill_count=skills_count,
        ))

    return RolesListResponse(roles=roles)
