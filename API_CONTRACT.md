# RoleGauge API Contract & Integration Specification

**Version:** 1.2.0  
**Target Audience:** Frontend Developers, AI Engineers, Backend Integrators  
**Base URL (Local/Docker):** `http://localhost:8000`

---

## 1. Architectural Principles & Database Policy

> [!IMPORTANT]
> **Production Database Policy:**
> - **PostgreSQL 16+** is strictly **REQUIRED** for staging and production environments.
> - **SQLite** (`sqlite+aiosqlite:///`) is supported exclusively as an isolated fixture for local unit tests and development scripts without Docker.
> - Analysis results, subskill evidence breakdowns, and scanned repository statistics are persisted transactionally in PostgreSQL.

> [!NOTE]
> **Scoring Authority:**
> - The backend `ScoringEngine` is the **SOLE numeric authority**.
> - AI Providers (OpenAI/Gemini) **never generate scores directly**; they only detect evidence signals for unevidenced subskills.
> - All scoring formulas (signal ceilings, diminishing factor for secondary signals, target level vs. lower prerequisite weights, and denominator isolation) are dynamically read from `knowledge-base/scoring/engine.json`.

> [!WARNING]
> **Production Rate Limiter & Redis Mandate:**
> - In development and isolated test suites, an in-memory storage (`memory://`) is used for convenience.
> - **In production environments, REDIS IS STRICTLY MANDATORY (`REDIS_URL=redis://...`).**
> - *Why?* Even on a single server, worker restarts wipe in-memory counters. In multi-worker (e.g. Gunicorn/Uvicorn cluster) or containerized replica (Kubernetes pods) architectures, in-memory counters are isolated per process, allowing clients to bypass limits by distributing requests across workers. Production deployments **MUST** provide a shared Redis instance.

---

## 2. Global Error Handling Contract

All error responses strictly adhere to FastAPI's standard JSON structure:

```json
{
  "detail": "Descriptive human-readable error explanation."
}
```

### HTTP Status Code Mapping

| Status Code | Reason / Condition | Example Detail Payload |
|:---|:---|:---|
| **400 Bad Request** | Unknown role, invalid level, invalid email format, or invalid UUID syntax. | `{"detail": "Unknown role: 'unknown-role'. Available roles: ['backend', 'frontend', ...]"}` |
| **401 Unauthorized** | Missing, expired, or invalid JWT Bearer token, or incorrect login password. | `{"detail": "Invalid or expired authentication token."}` |
| **403 Forbidden** | Attempting to access a private analysis created by another user. | `{"detail": "You do not have permission to view this analysis."}` |
| **404 Not Found** | GitHub user does not exist, or analysis result ID does not exist in DB. | `{"detail": "GitHub user 'nonexistent_user_999' was not found on GitHub."}` |
| **409 Conflict** | Attempting to register an email that already exists. | `{"detail": "An account with this email address already exists."}` |
| **422 Unprocessable** | Request validation error (e.g. password < 8 chars, malformed email). | `{"detail": [{"loc": ["body", "password"], "msg": "String should have at least 8 characters"}]}` |
| **429 Too Many Requests** | RoleGauge rate limit or GitHub REST API rate limit reached. Includes `Retry-After` header. | `{"detail": "Rate limit exceeded. Try again in 3600 seconds."}` |
| **504 Gateway Timeout** | GitHub REST API request timed out (after 30s). | `{"detail": "GitHub API request timed out. Please check network connectivity or try again later."}` |
| **500 Internal Server Error** | Unexpected pipeline failure or database connection loss. | `{"detail": "Analysis pipeline failed: <error message>"}` |

---

## 2.1 Tiered Rate Limiting Specification

RoleGauge protects backend resources, protects against brute-force attacks, and controls OpenAI API costs via layered rate limits:

| Endpoint | Guest Limit (IP-based) | Auth User Limit (`user_id`) | Scope & Purpose |
|:---|:---|:---|:---|
| `POST /api/analyze` (Standard) | **5 / hour** | **20 / hour** | Standard GitHub/CV profile analysis |
| `POST /api/analyze` (`use_ai: true`) | **2 / hour** | **10 / hour** | High-cost OpenAI GPT-4o-mini evidence detection |
| `POST /api/auth/register` | **5 / 15 minutes (IP)** | **5 / 15 minutes (IP)** | Anti-spam & registration bot prevention |
| `POST /api/auth/login` | **5 / 15 minutes (IP)** | **5 / 15 minutes (IP)** | Brute-force & credential stuffing defense |
| `POST /api/cv/upload` | **10 / hour** | **30 / hour** | PDF/DOCX file parsing & skill extraction |
| `POST /api/linkedin/upload` | **10 / hour** | **30 / hour** | LinkedIn PDF parsing & certification matching |

**429 Response Headers:**
- `Retry-After`: Number of seconds until the current rate limit window resets.
- `X-RateLimit-Limit`: Maximum requests permitted in the window.
- `X-RateLimit-Remaining`: Remaining requests permitted (`0` when rate limited).
- `X-RateLimit-Reset`: Unix timestamp when the window resets.

---

## 3. Authentication & Authorization Matrix

RoleGauge uses standard **JWT Bearer Authentication** (HS256):
- **Access Token:** Short-lived (30 minutes), carried in `Authorization: Bearer <access_token>` header.
- **Refresh Token:** Long-lived (7 days), used at `POST /api/auth/refresh` to obtain a new access token.

> [!NOTE]
> **Token Revocation (MVP Architectural Scope):**
> RoleGauge MVP adopts standard stateless JWT tokens. Currently, logout is handled on the client side by discarding the stored tokens (client-side disposal); there is no server-side token revocation/blacklisting database table. A Redis-backed token revocation list (or refresh token rotation/family tracking) is scoped for future production iterations.

### Endpoint Authentication Matrix

| Endpoint | Method | Auth Requirement | Description |
|:---|:---|:---|:---|
| `/api/auth/register` | POST | **Public** | Register a new account; returns tokens and user profile. |
| `/api/auth/login` | POST | **Public** | Login with email/password; returns access + refresh tokens. |
| `/api/auth/refresh` | POST | **Public** | Refresh access token using valid refresh token. |
| `/api/auth/me` | GET | **Required** | Get current authenticated user profile. |
| `/api/users/me/analyses` | GET | **Required** | Retrieve user's historical analysis records. |
| `/api/analyze` | POST | **Optional** | If token present, associates analysis with user account. |
| `/api/cv/upload` | POST | **Optional** | Open to guests and authenticated users. |
| `/api/linkedin/upload` | POST | **Optional** | Open to guests and authenticated users. |
| `/api/assessment/start` | POST | **Optional** | If token present, links session to user. |
| `/api/assessment/submit` | POST | **Optional** | Evaluates answers and recalculates analysis. |
| `/api/results/{id}` | GET | **Conditional** | Public for guest analyses (`user_id=None`); restricted to owner for user analyses. |
| `/api/roles` | GET | **Public** | List all available roles and levels. |
| `/api/health` | GET | **Public** | System liveness and loaded roles count. |

---

## 4. Endpoints

---

### 4.1. `POST /api/auth/register` — Register User Account

#### Request Body Schema
```json
{
  "email": "developer@example.com",
  "password": "StrongPassword123!",
  "full_name": "Jane Doe"
}
```

#### Response (201 Created)
```json
{
  "access_token": "eyJhbGciOi...",
  "refresh_token": "eyJhbGciOi...",
  "token_type": "bearer",
  "user": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "email": "developer@example.com",
    "full_name": "Jane Doe",
    "is_active": true,
    "created_at": "2026-09-01T00:00:00Z"
  }
}
```

---

### 4.2. `POST /api/auth/login` — User Login

#### Request Body Schema
```json
{
  "email": "developer@example.com",
  "password": "StrongPassword123!"
}
```

#### Response (200 OK)
Returns identical JSON schema to `POST /api/auth/register`.

---

### 4.3. `POST /api/auth/refresh` — Refresh Access Token

#### Request Body Schema
```json
{
  "refresh_token": "eyJhbGciOi..."
}
```

#### Response (200 OK)
```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```

---

### 4.4. `GET /api/auth/me` — Current User Profile

#### Request Headers
- `Authorization: Bearer <access_token>`

#### Response (200 OK)
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "email": "developer@example.com",
  "full_name": "Jane Doe",
  "is_active": true,
  "created_at": "2026-09-01T00:00:00Z"
}
```

---

### 4.5. `GET /api/users/me/analyses` — User Analysis History

#### Request Headers
- `Authorization: Bearer <access_token>`

#### Response (200 OK)
```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "github_username": "tiangolo",
    "role_id": "backend",
    "role_name": "Backend Developer",
    "level": "mid",
    "readiness_score": 0.8125,
    "readiness_tier": "ready",
    "readiness_label": "Ready",
    "created_at": "2026-09-01T00:00:00Z"
  }
]
```

---

### 4.6. `POST /api/analyze` — Execute Role & Skill Analysis

Performs the full pipeline: extracts username, scans public repositories, filters role-relevant code and dependencies, detects evidence for subskills, evaluates mathematical scoring formulas, saves results to PostgreSQL, and returns the full assessment breakdown.

#### Request Headers
- `Content-Type: application/json`

#### Request Body Schema

| Field | Type | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `github_username` | `string` | **Yes** | — | GitHub username or profile URL (e.g. `"torvalds"`, `"https://github.com/tiangolo"`) |
| `role_id` | `string` | **Yes** | — | Target role category ID (e.g. `"backend"`, `"frontend"`, `"game-dev"`, `"ai-engineer"`) |
| `level` | `string` | No | `"mid"` | Target seniority level: `"junior"`, `"mid"`, or `"senior"` |
| `github_token` | `string` | No | `null` | Optional GitHub Personal Access Token to avoid rate limits |
| `use_ai` | `boolean` | No | `false` | If `true`, runs AI enrichment for unevidenced subskills using configured AI provider |

#### Example Request
```json
{
  "github_username": "tiangolo",
  "role_id": "backend",
  "level": "mid",
  "use_ai": false
}
```

#### Response Body Schema (JSON)

```json
{
  "id": "UUID (string)",
  "github_username": "string",
  "role_id": "string",
  "role_name": "string",
  "level": "junior | mid | senior",
  "readiness_score": 0.7850,
  "readiness_tier": "ready",
  "readiness_label": "Ready",
  "total_repos_scanned": 30,
  "relevant_repos_found": 8,
  "skills": [
    {
      "skill_id": "be_api_design",
      "skill_name": "API Design & Implementation",
      "score": 0.8500,
      "importance": 0.90,
      "subskills": [
        {
          "composite_key": "be_api_design.rest_principles",
          "subskill_name": "RESTful API Design & Best Practices",
          "confidence": 1.0,
          "status": "evidence_found",
          "evidence_sources": [
            "fastapi/app/main.py → APIRouter",
            "fastapi/requirements.txt → pydantic"
          ]
        },
        {
          "composite_key": "be_api_design.openapi_spec",
          "subskill_name": "OpenAPI / Swagger Documentation",
          "confidence": 0.0,
          "status": "not_yet_evidenced",
          "evidence_sources": []
        }
      ]
    }
  ],
  "repos": [
    {
      "repo_name": "fastapi",
      "repo_url": "https://github.com/tiangolo/fastapi",
      "description": "FastAPI framework, high performance, easy to learn, fast to code, ready for production",
      "primary_language": "Python",
      "languages": {
        "Python": 2849102
      },
      "stars": 75000,
      "forks": 6200,
      "topics": ["fastapi", "async", "api", "python"],
      "is_relevant": true,
      "relevant_files_count": 42,
      "evidence_found": [
        "be_api_design.rest_principles",
        "be_architecture_patterns.modular_design"
      ]
    }
  ],
  "created_at": "2026-08-29T10:45:00.000000Z"
}
```

---

### 3.2. `GET /api/results/{id}` — Retrieve Saved Analysis

Fetches a previously executed analysis by UUID directly from PostgreSQL.

#### Request Path Parameters
- `id` (string, required): Analysis UUID (e.g. `e38c29db-6031-4171-bc01-9a99f187a554`).

#### Example Request
```http
GET /api/results/e38c29db-6031-4171-bc01-9a99f187a554 HTTP/1.1
Host: localhost:8000
Accept: application/json
```

#### Response
Returns identical JSON schema to `POST /api/analyze`.

---

### 3.3. `GET /api/roles` — List Available Roles & Seniority Levels

Returns all active role categories loaded in the Knowledge Base.

#### Response Example
```json
[
  {
    "category": "backend",
    "name": "Backend Developer",
    "levels": ["junior", "mid", "senior"]
  },
  {
    "category": "frontend",
    "name": "Frontend Developer",
    "levels": ["junior", "mid", "senior"]
  },
  {
    "category": "ai-engineer",
    "name": "AI Engineer",
    "levels": ["junior", "mid", "senior"]
  }
]
```

---

### 3.4. `POST /api/assessment/start` — Start Adaptive Assessment Session

Initiates an adaptive Q&A assessment for a candidate. Selects prioritized questions based on `trigger_conditions` in `assessment.json` (`not_yet_evidenced` expected subskills, low confidence, critical skills, or voluntary requests).

> [!IMPORTANT]
> `expected_answer_keywords` are strictly kept server-side to prevent cheating and are omitted from all client responses.

#### Request Body
```json
{
  "analysis_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "voluntary_composite_keys": ["be_databases.sql_querying"],
  "max_questions": 10
}
```

#### Response Body
```json
{
  "assessment_session_id": "550e8400-e29b-41d4-a716-446655440000",
  "analysis_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "role_id": "backend",
  "level": "mid",
  "total_questions": 3,
  "questions": [
    {
      "composite_key": "be_databases.sql_querying",
      "subskill_name": "SQL Querying & Window Functions",
      "question": "Write a SQL query using window functions to retrieve the top 3 highest-earning employees in each department.",
      "type": "scenario",
      "level": "mid"
    }
  ]
}
```

---

### 3.5. `POST /api/assessment/submit` — Submit Assessment Answers

Evaluates candidate answers against `engine.json` keyword matching thresholds (correct >= 60%, partial 30%-59%, incorrect < 30%), feeds verified signals into `EvidenceEngine`, recalculates scoring via `ScoringEngine`, updates the database record, and returns question evaluations and the updated analysis.

#### Request Body
```json
{
  "assessment_session_id": "550e8400-e29b-41d4-a716-446655440000",
  "answers": {
    "be_databases.sql_querying": "I would use DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) in a CTE, then filter WHERE rank <= 3."
  }
}
```

#### Response Body
```json
{
  "assessment_session_id": "550e8400-e29b-41d4-a716-446655440000",
  "analysis_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "evaluations": [
    {
      "composite_key": "be_databases.sql_querying",
      "subskill_name": "SQL Querying & Window Functions",
      "verdict": "correct",
      "status": "evidence_found",
      "score": 1.0,
      "strength": 0.8,
      "match_ratio": 0.8333,
      "matched_keywords_count": 5,
      "total_keywords_count": 6,
      "feedback": "Correct answer: matched 5/6 keywords (83.3% >= 60%). Status: evidence_found (signal strength: 0.80)."
    }
  ],
  "summary": {
    "total": 1,
    "correct": 1,
    "partial": 0,
    "incorrect": 0
  },
  "updated_analysis": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "github_username": "tiangolo",
    "role_id": "backend",
    "role_name": "Backend Developer",
    "level": "mid",
    "readiness_score": 0.8125,
    "readiness_tier": "ready",
    "readiness_label": "Ready",
    "skills": [...]
  }
}
```

---

### 3.6. `POST /api/cv/upload` — Upload & Parse CV (PDF/DOCX)

Rule-based extraction and scoring preview for resume documents (.pdf, .docx, <= 10MB).

#### Request Form Data (Multipart)
- `file` (File, required): CV file (.pdf or .docx).
- `role_id` (string, required): Role ID (e.g. `"backend"`).
- `level` (string, optional, default `"mid"`): `"junior"`, `"mid"`, or `"senior"`.

#### Response Body Schema
```json
{
  "parsed_cv": {
    "personal_info": {"name": "...", "email": "..."},
    "education": [...],
    "experience": [...],
    "projects": [...],
    "skills": ["Python", "FastAPI"],
    "certificates": [{"name": "AWS Certified Solutions Architect", "provider": "AWS"}],
    "languages": ["English"],
    "detected_sections": ["personal_info", "experience", "skills", "certificates"]
  },
  "skill_matches": [
    {
      "composite_key": "be_api_design.rest_principles",
      "matched_from": "skills_list",
      "matched_term": "FastAPI",
      "status": "claimed",
      "strength": 0.30
    }
  ],
  "certificate_matches": [
    {
      "certificate_name": "AWS Certified Solutions Architect",
      "classification": "recognized_relevant",
      "matched_composite_keys": ["be_architecture_patterns.cloud_native"],
      "score_contribution": 0.20
    }
  ],
  "scoring_preview": {
    "readiness_score": 0.4500,
    "readiness_tier": "developing",
    "readiness_label": "Developing",
    "skills": [...]
  }
}
```

---

### 3.7. `POST /api/linkedin/upload` — Upload & Parse LinkedIn Profile PDF

Extracts structured profile data from LinkedIn "Save to PDF" exports, applies role-specific base strengths from `knowledge-base/evidence/{role}/linkedin.json` (skills_endorsements: 0.15, headline_summary: 0.20, experience: 0.40, projects: 0.30, recommendations: 0.30), matches certifications against the allowlist, and calculates a scoring preview.

> [!NOTE]
> LinkedIn PDF export aktivite/gönderileri içermez, bu yüzden `posts_articles` kaynağı şu an aktif değildir.

#### Request Form Data (Multipart)
- `file` (File, required): LinkedIn PDF export (.pdf only, <= 10MB).
- `role_id` (string, required): Role ID (e.g. `"backend"`).
- `level` (string, optional, default `"mid"`): `"junior"`, `"mid"`, or `"senior"`.

#### Response Body Schema
```json
{
  "parsed_linkedin": {
    "personal_info": {"name": "...", "headline": "...", "summary": "..."},
    "education": [...],
    "experience": [...],
    "projects": [...],
    "skills": ["Python", "FastAPI", "PostgreSQL", "Kafka"],
    "certificates": [{"name": "AWS Certified Solutions Architect - Associate", "provider": "AWS"}],
    "languages": ["English"],
    "volunteering": [...],
    "honors_awards": [...],
    "publications": [...],
    "recommendations": [{"recommender": "...", "text": "..."}],
    "detected_sections": ["personal_info", "experience", "education", "certificates", "skills", "recommendations"]
  },
  "skill_matches": [
    {
      "composite_key": "be_databases.sql_querying",
      "matched_from": "skills",
      "matched_term": "PostgreSQL",
      "status": "claimed",
      "strength": 0.15
    },
    {
      "composite_key": "be_architecture_patterns.event_driven_architecture",
      "matched_from": "experience",
      "matched_term": "Kafka",
      "status": "claimed",
      "strength": 0.40
    }
  ],
  "certificate_matches": [
    {
      "certificate_name": "AWS Certified Solutions Architect - Associate",
      "classification": "recognized_relevant",
      "matched_composite_keys": ["be_architecture_patterns.cloud_native"],
      "score_contribution": 0.20
    }
  ],
  "scoring_preview": {
    "readiness_score": 0.5200,
    "readiness_tier": "approaching",
    "readiness_label": "Approaching",
    "skills": [...]
  }
}
```

---

### 3.8. `GET /api/health` — Health & KB Status

Verifies backend liveness, loaded role counts, and AI provider status.

#### Response Example
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "roles_loaded": 18,
  "ai_provider": "none"
}
```

---

## 4. TypeScript Interfaces (For Frontend Integration)

Frontend developers can copy and use these exact TypeScript interfaces:

```typescript
export type SeniorityLevel = 'junior' | 'mid' | 'senior';

export type ReadinessTier = 'not_ready' | 'developing' | 'approaching' | 'ready' | 'exceeds';

export type EvidenceStatus = 'evidence_found' | 'claimed' | 'not_yet_evidenced' | 'verified_gap';

export interface SubskillEvidence {
  composite_key: string;       // e.g. "be_api_design.rest_principles"
  subskill_name: string;
  confidence: number;          // 0.0 to 1.0
  status: EvidenceStatus;
  evidence_sources: string[];
  contributing_sources?: Array<{ source: string; strength: number; signal: string }>;
  ceiling_applied?: string;
  calculation_trace?: string;
}

export interface SkillScore {
  skill_id: string;
  skill_name: string;
  score: number;               // 0.0 to 1.0
  importance: number;          // 0.0 to 1.0
  subskills: SubskillEvidence[];
}

export interface RepoInfo {
  repo_name: string;
  repo_url: string;
  description?: string;
  primary_language?: string;
  languages: Record<string, number>;
  stars: number;
  forks: number;
  topics: string[];
  is_relevant: boolean;
  relevant_files_count: number;
  evidence_found: string[];
}

export interface AnalyzeResponse {
  id: string;                  // UUID
  github_username: string;
  role_id: string;
  role_name: string;
  level: SeniorityLevel;
  readiness_score: number;     // 0.0 to 1.0
  readiness_tier: ReadinessTier;
  readiness_label: string;
  total_repos_scanned: number;
  relevant_repos_found: number;
  has_cv?: boolean;
  has_linkedin?: boolean;
  skills: SkillScore[];
  repos: RepoInfo[];
  created_at: string;          // ISO 8601 UTC
}

export interface AnalyzeRequest {
  github_username?: string;
  role_id: string;
  level?: SeniorityLevel;
  github_token?: string;
  use_ai?: boolean;
}

export interface LinkedInParsedData {
  personal_info: Record<string, string>;
  education: Array<Record<string, string>>;
  experience: Array<Record<string, string>>;
  projects: Array<{ name: string; description: string; skills_mentioned: string[] }>;
  skills: string[];
  certificates: Array<{ name: string; provider: string }>;
  languages: string[];
  volunteering: Array<Record<string, string>>;
  honors_awards: Array<Record<string, string>>;
  publications: Array<Record<string, string>>;
  recommendations: Array<{ recommender: string; text: string }>;
  detected_sections: string[];
}

export interface LinkedInSkillMatch {
  composite_key: string;
  matched_from: string;
  matched_term: string;
  status: string;
  strength: number;
}

export interface LinkedInCertificateMatch {
  certificate_name: string;
  classification: 'recognized_relevant' | 'recognized_no_mapping' | 'unrecognized_excluded';
  matched_composite_keys?: string[];
  score_contribution: number;
  matched_from_role?: string;
  category_group?: string;
}

export interface LinkedInUploadResponse {
  parsed_linkedin: LinkedInParsedData;
  skill_matches: LinkedInSkillMatch[];
  certificate_matches: LinkedInCertificateMatch[];
  scoring_preview: {
    readiness_score: number;
    readiness_tier: ReadinessTier;
    readiness_label: string;
    skills: SkillScore[];
  };
}

export interface AssessmentQuestionPublic {
  composite_key: string;
  subskill_name: string;
  question: string;
  type: 'conceptual' | 'scenario' | 'practical_task';
  level: SeniorityLevel;
}

export interface AssessmentStartResponse {
  assessment_session_id: string;
  analysis_id: string;
  role_id: string;
  level: SeniorityLevel;
  total_questions: number;
  questions: AssessmentQuestionPublic[];
}

export interface AssessmentQuestionEvaluation {
  composite_key: string;
  subskill_name: string;
  verdict: 'correct' | 'partial' | 'incorrect';
  status: 'evidence_found' | 'partial_answer' | 'verified_gap';
  score: number;
  strength: number;
  match_ratio: number;
  matched_keywords_count: number;
  total_keywords_count: number;
  feedback: string;
}

export interface AssessmentSubmitResponse {
  assessment_session_id: string;
  analysis_id: string;
  evaluations: AssessmentQuestionEvaluation[];
  summary: {
    total: number;
    correct: number;
    partial: number;
    incorrect: number;
  };
  updated_analysis: AnalyzeResponse;
}

export interface UserRegisterRequest {
  email: string;
  password: string;
  full_name?: string;
}

export interface UserLoginRequest {
  email: string;
  password: string;
}

export interface TokenRefreshRequest {
  refresh_token: string;
}

export interface UserResponse {
  id: string;
  email: string;
  full_name?: string;
  is_active: boolean;
  created_at: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user: UserResponse;
}

export interface TokenRefreshResponse {
  access_token: string;
  token_type: string;
}

export interface UserAnalysisSummary {
  id: string;
  github_username: string;
  role_id: string;
  role_name: string;
  level: SeniorityLevel;
  readiness_score: number;
  readiness_tier: ReadinessTier;
  readiness_label: string;
  created_at: string;
}

export interface ApiError {
  detail: string;
}
```

---

## 5. AI Integration Contract (For AI Provider Developers)

When `use_ai: true` is passed:
1. The backend collects all subskills with `status: "not_yet_evidenced"`.
2. A filtered bundle containing `file_contents`, `dependencies`, and `readme` is passed to the AI provider.
3. The AI provider **only** returns evidence classifications and candidate source locations:

```json
{
  "be_api_design.openapi_spec": {
    "status": "evidence_found",
    "evidence_sources": ["fastapi/openapi/docs.py:L14-22"],
    "quality_notes": "Detected custom OpenAPI schema definitions"
  }
}
```
4. The backend Scoring Engine then applies mathematical ceilings and weighting deterministically.
