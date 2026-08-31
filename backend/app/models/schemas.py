"""
RoleGauge API Schemas.
Pydantic models for request/response validation and serialization.
"""

from pydantic import BaseModel, Field
from typing import Any, Optional
from datetime import datetime


# ──────────────────────────────────────────────
# Request Schemas
# ──────────────────────────────────────────────

class AnalyzeRequest(BaseModel):
    """Request body for POST /api/analyze."""
    github_username: Optional[str] = Field(None, max_length=255, description="GitHub username or profile URL")
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
    status: str  # evidence_found | claimed | not_yet_evidenced | verified_gap
    evidence_sources: list[str] = []
    contributing_sources: list[dict[str, Any]] = []
    ceiling_applied: Optional[str] = None
    calculation_trace: Optional[str] = None


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
    github_username: Optional[str] = ""
    role_id: str
    role_name: str
    level: str
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    readiness_tier: str
    readiness_label: str
    total_repos_scanned: int
    relevant_repos_found: int
    has_cv: bool = False
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


# ──────────────────────────────────────────────
# CV Upload Schemas
# ──────────────────────────────────────────────

class CVProjectData(BaseModel):
    """A project entry from the parsed CV."""
    name: str = ""
    description: str = ""
    skills_mentioned: list[str] = []


class CVCertificateData(BaseModel):
    """A certificate entry from the parsed CV."""
    name: str = ""
    provider: str = ""


class CVParsedData(BaseModel):
    """Structured data extracted from a CV by the parser."""
    personal_info: dict[str, str] = {}
    education: list[dict[str, str]] = []
    experience: list[dict[str, str]] = []
    projects: list[CVProjectData] = []
    skills: list[str] = []
    certificates: list[CVCertificateData] = []
    languages: list[str] = []
    detected_sections: list[str] = []


class CVSkillMatch(BaseModel):
    """A single skill match result from CV analysis."""
    composite_key: str
    matched_from: str  # "skills_list" | "project" | "experience" | "signal_pattern"
    matched_term: str
    status: str = "claimed"
    strength: float


class CVCertificateMatch(BaseModel):
    """A single certificate match result from CV analysis."""
    certificate_name: str
    classification: str  # "recognized_relevant" | "recognized_no_mapping" | "unrecognized_excluded"
    matched_composite_keys: Optional[list[str]] = None
    score_contribution: float = 0.0
    matched_from_role: Optional[str] = None
    category_group: Optional[str] = None


class CVScoringPreview(BaseModel):
    """Scoring preview from CV-only evidence."""
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    readiness_tier: str
    readiness_label: str
    skills: list[SkillScore] = []


class CVUploadResponse(BaseModel):
    """Full response from POST /api/cv/upload."""
    parsed_cv: CVParsedData
    skill_matches: list[CVSkillMatch] = []
    certificate_matches: list[CVCertificateMatch] = []
    scoring_preview: CVScoringPreview


# ──────────────────────────────────────────────
# Assessment Schemas
# ──────────────────────────────────────────────

class AssessmentStartRequest(BaseModel):
    """Request body for POST /api/assessment/start."""
    analysis_id: Optional[str] = Field(None, description="Existing analysis ID (UUID)")
    github_username: Optional[str] = Field(None, description="GitHub username if starting fresh")
    role_id: Optional[str] = Field(None, description="Role identifier (e.g. 'backend', 'devops')")
    level: str = Field("mid", description="Target seniority level ('junior', 'mid', 'senior')")
    voluntary_composite_keys: Optional[list[str]] = Field(None, description="Optional voluntary subskills to test")
    max_questions: int = Field(10, ge=1, le=25, description="Maximum number of questions to select")


class AssessmentQuestionPublic(BaseModel):
    """Public question payload sent to client (expected_answer_keywords strictly omitted)."""
    composite_key: str
    subskill_name: str
    question: str
    type: str  # conceptual | scenario | practical_task
    level: str  # junior | mid | senior


class AssessmentStartResponse(BaseModel):
    """Response body from POST /api/assessment/start."""
    assessment_session_id: str
    analysis_id: str
    role_id: str
    level: str
    total_questions: int
    questions: list[AssessmentQuestionPublic]


class AssessmentAnswerItem(BaseModel):
    """A single submitted answer for a subskill question."""
    composite_key: str
    answer: str


class AssessmentSubmitRequest(BaseModel):
    """Request body for POST /api/assessment/submit."""
    assessment_session_id: str = Field(..., description="ID of active assessment session")
    answers: dict[str, str] | list[AssessmentAnswerItem] = Field(
        ..., description="Map of {composite_key: answer_text} or list of answer items"
    )


class AssessmentQuestionEvaluation(BaseModel):
    """Evaluation result for an individual question answer."""
    composite_key: str
    subskill_name: str
    question: str = ""
    type: str = ""
    verdict: str  # correct | partial | incorrect
    status: str  # evidence_found | partial_answer | verified_gap
    score: float
    strength: float
    match_ratio: float
    matched_keywords_count: int
    total_keywords_count: int
    feedback: str


class AssessmentSubmitResponse(BaseModel):
    """Response body from POST /api/assessment/submit."""
    assessment_session_id: str
    analysis_id: str
    evaluations: list[AssessmentQuestionEvaluation]
    summary: dict[str, int]
    updated_analysis: AnalyzeResponse


