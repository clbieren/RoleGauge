"""
RoleGauge API Schemas.
Pydantic models for request/response validation and serialization.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ──────────────────────────────────────────────
# Request Schemas
# ──────────────────────────────────────────────

class AnalyzeRequest(BaseModel):
    """Request body for POST /api/analyze."""
    github_username: str = Field(..., min_length=1, max_length=255, description="GitHub username or profile URL")
    role_id: str = Field(..., description="Role identifier (e.g. 'game-dev', 'backend')")
    level: str = Field("mid", description="Target seniority level ('junior', 'mid', 'senior')")
    github_token: Optional[str] = Field(None, description="Optional GitHub PAT for higher rate limits")
    use_ai: bool = Field(False, description="Whether to use AI for deeper evidence analysis")


# ──────────────────────────────────────────────
# Response Schemas
# ──────────────────────────────────────────────

class SubskillEvidence(BaseModel):
    """Evidence result for a single subskill."""
    composite_key: str
    subskill_name: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    status: str  # evidence_found | not_yet_evidenced
    evidence_sources: list[str] = []


class SkillScore(BaseModel):
    """Score for a single skill with its subskill breakdown."""
    skill_id: str
    skill_name: str
    score: float = Field(..., ge=0.0, le=1.0)
    importance: float
    subskills: list[SubskillEvidence] = []


class RepoInfo(BaseModel):
    """Metadata about a scanned repository."""
    repo_name: str
    repo_url: str
    description: Optional[str] = None
    primary_language: Optional[str] = None
    languages: dict[str, int] = {}
    stars: int = 0
    forks: int = 0
    topics: list[str] = []
    is_relevant: bool = False
    relevant_files_count: int = 0
    evidence_found: list[str] = []  # Composite keys found


class AnalyzeResponse(BaseModel):
    """Full analysis result returned by POST /api/analyze."""
    id: str
    github_username: str
    role_id: str
    role_name: str
    level: str
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    readiness_tier: str
    readiness_label: str
    total_repos_scanned: int
    relevant_repos_found: int
    skills: list[SkillScore] = []
    repos: list[RepoInfo] = []
    created_at: datetime


class RoleInfo(BaseModel):
    """Summary of an available role."""
    role_id: str
    title: str
    description: str
    category: str  # The KB directory name (e.g. "game-dev")
    levels: list[str] = ["junior", "mid", "senior"]
    skill_count: int = 0


class RolesListResponse(BaseModel):
    """Response for GET /api/roles."""
    roles: list[RoleInfo]


class AnalysisProgress(BaseModel):
    """SSE progress event during analysis."""
    step: str
    message: str
    progress: float = Field(..., ge=0.0, le=1.0)  # 0.0 to 1.0
    detail: Optional[str] = None
