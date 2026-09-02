import re
from pydantic import BaseModel, Field, field_validator
from typing import Any, Optional
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


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


class AdPlacements(BaseModel):
    """Signals indicating active advertisement slots for client rendering."""
    loading_screen: bool = True
    results_sidebar_left: bool = True
    results_sidebar_right: bool = True


def resolve_ad_placements(user: Optional[Any] = None) -> tuple[str, AdPlacements]:
    """
    Determine analysis_tier and ad_placements based on user status.
    Prepared for future user.is_premium attribute:
    - Standard/Guest users: analysis_tier='standard', all ad slots active (True).
    - Premium users: analysis_tier='premium', all ad slots disabled (False).
    """
    is_premium = getattr(user, "is_premium", False) if user else False
    if is_premium:
        return "premium", AdPlacements(
            loading_screen=False,
            results_sidebar_left=False,
            results_sidebar_right=False,
        )
    return "standard", AdPlacements(
        loading_screen=True,
        results_sidebar_left=True,
        results_sidebar_right=True,
    )


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
    has_linkedin: bool = False
    ai_enrichment_available: bool = False
    analysis_tier: str = "standard"
    ad_placements: AdPlacements = Field(default_factory=AdPlacements)
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
    volunteering: list[dict[str, str]] = []
    honors_awards: list[dict[str, str]] = []
    publications: list[dict[str, str]] = []
    recommendations: list[dict[str, str]] = []
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
# LinkedIn Upload Schemas
# ──────────────────────────────────────────────

class LinkedInParsedData(BaseModel):
    """Structured data extracted from a LinkedIn PDF export."""
    personal_info: dict[str, str] = {}
    education: list[dict[str, str]] = []
    experience: list[dict[str, str]] = []
    projects: list[CVProjectData] = []
    skills: list[str] = []
    certificates: list[CVCertificateData] = []
    languages: list[str] = []
    volunteering: list[dict[str, str]] = []
    honors_awards: list[dict[str, str]] = []
    publications: list[dict[str, str]] = []
    recommendations: list[dict[str, str]] = []
    detected_sections: list[str] = []


class LinkedInSkillMatch(BaseModel):
    """A single skill match result from LinkedIn analysis."""
    composite_key: str
    matched_from: str  # "skills" | "experience" | "summary" | "project" | "signal_pattern" | "posts_articles" | "recommendations"
    matched_term: str
    status: str = "claimed"
    strength: float


class LinkedInCertificateMatch(BaseModel):
    """A single certificate match result from LinkedIn analysis."""
    certificate_name: str
    classification: str  # "recognized_relevant" | "recognized_no_mapping" | "unrecognized_excluded"
    matched_composite_keys: Optional[list[str]] = None
    score_contribution: float = 0.0
    matched_from_role: Optional[str] = None
    category_group: Optional[str] = None


class LinkedInScoringPreview(BaseModel):
    """Scoring preview from LinkedIn-only evidence."""
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    readiness_tier: str
    readiness_label: str
    skills: list[SkillScore] = []


class LinkedInUploadResponse(BaseModel):
    """Full response from POST /api/linkedin/upload."""
    parsed_linkedin: LinkedInParsedData
    skill_matches: list[LinkedInSkillMatch] = []
    certificate_matches: list[LinkedInCertificateMatch] = []
    scoring_preview: LinkedInScoringPreview


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


# ──────────────────────────────────────────────
# Authentication & User Schemas
# ──────────────────────────────────────────────

class UserRegisterRequest(BaseModel):
    """Request body for POST /api/auth/register."""
    email: str = Field(..., description="Valid email address")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    full_name: Optional[str] = Field(None, max_length=255, description="Optional display name")

    @field_validator("email")
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        v = v.strip().lower()
        if not EMAIL_REGEX.match(v):
            raise ValueError("Invalid email address format")
        return v


class UserLoginRequest(BaseModel):
    """Request body for POST /api/auth/login."""
    email: str = Field(..., description="Registered email address")
    password: str = Field(..., description="User password")

    @field_validator("email")
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        v = v.strip().lower()
        if not EMAIL_REGEX.match(v):
            raise ValueError("Invalid email address format")
        return v


class TokenRefreshRequest(BaseModel):
    """Request body for POST /api/auth/refresh."""
    refresh_token: str = Field(..., description="Valid refresh token")


class UserResponse(BaseModel):
    """Public user profile response."""
    id: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: datetime


class TokenResponse(BaseModel):
    """Access and refresh token response upon login/registration."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenRefreshResponse(BaseModel):
    """Fresh access token response upon refresh."""
    access_token: str
    token_type: str = "bearer"


class UserAnalysisSummary(BaseModel):
    """Summary item for a user's past analysis history."""
    id: str
    github_username: str
    role_id: str
    role_name: str
    level: str
    readiness_score: float
    readiness_tier: str
    readiness_label: str
    created_at: datetime



