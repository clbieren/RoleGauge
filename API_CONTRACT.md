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
| **400 Bad Request** | Unknown role, invalid level, or invalid GitHub username/URL syntax. | `{"detail": "Unknown role: 'unknown-role'. Available roles: ['backend', 'frontend', ...]"}` |
| **404 Not Found** | GitHub user does not exist, or analysis result ID does not exist in DB. | `{"detail": "GitHub user 'nonexistent_user_999' was not found on GitHub."}` |
| **429 Too Many Requests** | GitHub REST API rate limit reached (60/hr unauthenticated, 5000/hr with token). | `{"detail": "GitHub API rate limit exceeded. Please provide a GITHUB_TOKEN or try again later."}` |
| **504 Gateway Timeout** | GitHub REST API request timed out (after 30s). | `{"detail": "GitHub API request timed out. Please check network connectivity or try again later."}` |
| **500 Internal Server Error** | Unexpected pipeline failure or database connection loss. | `{"detail": "Analysis pipeline failed: <error message>"}` |

---

## 3. Endpoints

---

### 3.1. `POST /api/analyze` — Execute Role & Skill Analysis

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

### 3.4. `GET /api/health` — Health & KB Status

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

export type EvidenceStatus = 'evidence_found' | 'not_yet_evidenced' | 'verified_gap';

export interface SubskillEvidence {
  composite_key: string;       // e.g. "be_api_design.rest_principles"
  subskill_name: string;
  confidence: number;          // 0.0 to 1.0
  status: EvidenceStatus;
  evidence_sources: string[];
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
  description: string | null;
  primary_language: string | null;
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
  skills: SkillScore[];
  repos: RepoInfo[];
  created_at: string;          // ISO 8601 UTC
}

export interface AnalyzeRequest {
  github_username: string;
  role_id: string;
  level?: SeniorityLevel;
  github_token?: string;
  use_ai?: boolean;
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
