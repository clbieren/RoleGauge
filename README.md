# ⚡ RoleGauge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](backend/requirements.txt)
[![Node 20+](https://img.shields.io/badge/node-20%2B-green)](frontend/package.json)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange)](#-roadmap)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](#-tests)

### Open-source engineering skill assessment powered by real-world evidence.

RoleGauge evaluates engineering readiness using evidence from **GitHub repositories, CVs, LinkedIn profiles, and technical assessments**, instead of relying on self-reported skills or generic interview questions.

> **Don't just claim the skill. Show the evidence.**

**Project status: Alpha.** Core pipeline (GitHub/CV/LinkedIn parsing → scoring → profile) works end-to-end locally. Real-time progress, streaming, and benchmarking are not yet built — see [Roadmap](#-roadmap). Expect breaking changes between versions until v1.0.

---

## 🎥 Example Output

Below is a real sample of what `/api/analyze` returns for a GitHub-only analysis (trimmed for readability — full schema in [`API_CONTRACT.md`](https://github.com/clbieren/RoleGauge/blob/main/API_CONTRACT.md)):

```json
{
  "role": "Backend Engineer",
  "overall_score": 0.71,
  "skills": [
    {
      "name": "API Design",
      "score": 0.82,
      "target_level": "senior",
      "evidence": [
        { "source": "github", "signal": "openapi_spec_present", "weight": 0.3 },
        { "source": "github", "signal": "rest_framework:fastapi", "weight": 0.25 },
        { "source": "cv", "signal": "keyword:REST API", "weight": 0.05 }
      ]
    },
    {
      "name": "Database Design",
      "score": 0.58,
      "target_level": "mid",
      "evidence": [
        { "source": "github", "signal": "orm_usage:sqlalchemy", "weight": 0.2 },
        { "source": "github", "signal": "migration_files_present", "weight": 0.15 }
      ]
    }
  ],
  "prerequisites_met": ["version_control", "testing_basics"],
  "generated_at": "2026-09-20T14:02:11Z"
}
```

A demo GIF of the local setup is planned but not yet recorded — tracked in the roadmap.

---

## 🐳 Run it yourself

RoleGauge is designed to be **self-hosted and run locally**. No hosted account is required, and no data leaves your machine unless you explicitly enable an external AI provider (see [AI Is Optional](#-ai-is-optional--data-flow)).

```bash
git clone https://github.com/clbieren/RoleGauge.git
cd RoleGauge
cp .env.example .env
docker compose up --build
```

Then open:

```text
Frontend  → http://localhost:3000
API       → http://localhost:8000
Swagger   → http://localhost:8000/docs
```

**Requirements:** Docker, Docker Compose, Git.

**Stop:** `docker compose down`

---

## 🤔 Why RoleGauge?

Most technical profiles rely on self-reported skills, CV keywords, certifications, and generic interview questions. RoleGauge instead maps observable evidence — GitHub repos, dependency files, CV/LinkedIn content, and assessment answers — to role-specific skills, then scores that evidence deterministically rather than trusting an LLM's opinion outright.

```text
Evidence sources → Evidence Engine → Skill Matcher → Scoring Engine → Readiness Profile
```

---

## 🧮 Deterministic Scoring — how it actually works

The `ScoringEngine` is the **sole numeric authority** in RoleGauge. AI providers, when enabled, may propose evidence signals (e.g. "this repo shows async programming"), but they never assign the final score.

**Simplified example** of how a skill score is computed:

```text
skill_score = Σ (signal_weight × signal_confidence)
              capped at signal_ceiling
              then adjusted for diminishing_returns
              gated by prerequisites (0 if unmet)
```

Concretely, for "API Design" above:

```text
0.3 (openapi_spec) + 0.25 (fastapi usage) + 0.05 (cv keyword) = 0.60 raw
→ diminishing_returns curve applied (repeated similar signals count less)
→ 0.82 after normalization against role target_level "senior"
```

Configuration (weights, ceilings, prerequisites, target levels) lives in `knowledge-base/scoring/engine.json` and `knowledge-base/roles/<role>/`, not hard-coded in Python — so contributors can tune scoring without touching the engine itself.

---

## 🎯 Supported Roles

18 engineering-oriented roles, each with its own skill taxonomy, evidence patterns, and target levels:

| Role | Role | Role |
|---|---|---|
| AI Engineer | DevOps Engineer | Network Engineer |
| Android Developer | Frontend Engineer | QA Engineer |
| Backend Engineer | Game Developer | Technical Writer |
| Blockchain Developer | iOS Developer | UX Designer |
| Cyber Security Engineer | Machine Learning Engineer | API Design Specialist |
| Data Analyst | MLOps Engineer | Data Engineer |

**Example taxonomy** (`knowledge-base/roles/backend-engineer/skills.json`, abbreviated):

```text
Backend Engineer
 ├── API Design          (target: senior)  ← evidence: OpenAPI specs, REST/GraphQL frameworks
 ├── Database Design     (target: mid)     ← evidence: ORM usage, migrations, schema files
 ├── Testing Discipline  (target: mid)     ← evidence: test file ratio, CI config
 └── Concurrency         (target: senior)  ← evidence: async patterns, queue/worker code
```

Other roles follow the same structure under `knowledge-base/roles/`.

---

## 🤖 AI Is Optional — data flow

AI enrichment is **disabled by default**:

```env
AI_PROVIDER=none
```

If you enable `openai`, `gemini`, or `groq`, be aware of what actually happens:

- Repository file contents, CV text, and/or LinkedIn export text are sent to the configured third-party provider's API to help detect evidence signals (e.g. "does this code show testing discipline?").
- Anthropic/Claude is not currently a supported provider option.
- The `ScoringEngine` never sends raw candidate data anywhere — only the AI provider call does, and only for the enrichment step.
- No data is sent anywhere when `AI_PROVIDER=none` (the default) — all evidence detection runs locally via static analysis.
- RoleGauge does not currently redact PII before sending text to an AI provider. Treat any AI-enabled run as sharing raw CV/LinkedIn/code content with that provider, subject to their own data retention policy.

If you're processing candidate data you're not authorized to send to a third party, keep `AI_PROVIDER=none`.

---

## 🔒 Security & Privacy

RoleGauge processes potentially sensitive data (CVs, LinkedIn exports, GitHub tokens, candidate PII). Current state, plainly:

- **Auth:** `/api/auth/register` and `/api/auth/login` exist for multi-user self-hosted deployments (e.g. a team sharing one instance) — a single local user can ignore them entirely. Passwords are hashed with bcrypt before storage; see `backend/app/services/auth.py`.
- **GitHub tokens:** stored in `.env`, read at runtime, never logged. A token only needs `public_repo` read scope (or none, for public repos, at lower rate limits) — do not grant broader scopes than that.
- **Rate limiting:** enforced via Redis on `/api/analyze` and `/api/assessment/evaluate`; default limits are defined in `.env.example` (`RATE_LIMIT_PER_MINUTE`) — check that file for the current value, as it may change between releases.
- **Data retention:** analysis results are stored in PostgreSQL indefinitely until you delete them; there is currently no automatic expiry or GDPR/KVKK-style deletion endpoint. If you need one, this is an open contribution area (see Roadmap).
- **Your responsibility:** since this is self-hosted, you control the infrastructure and are responsible for authorization to process any candidate's data, and for your own retention/deletion policy.
- Report vulnerabilities per `SECURITY.md`.

---

## 🏗️ Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                         RoleGauge                            │
├───────────────────────┬───────────────────────────────────────┤
│        Frontend       │                Backend                │
│   Next.js 16 / React 19 / TypeScript / Recharts               │
│                        │  FastAPI + Python 3.11                │
│                        │  ┌──────────────────────────────┐    │
│                        │  │ GitHub Fetcher / CV Parser /  │    │
│                        │  │ LinkedIn Parser / Evidence     │    │
│                        │  │ Detection / Skill Matching     │    │
│                        │  └───────────────┬────────────────┘    │
│                        │  ┌───────────────▼────────────────┐    │
│                        │  │ Scoring Engine (Knowledge Base) │    │
│                        │  └───────────────┬────────────────┘    │
├────────────────────────┴──────────────────┼───────────────────┤
│              PostgreSQL 16+               │       Redis       │
│         (results, users, sessions)        │  (rate limiting)  │
└────────────────────────────────────────────┴───────────────────┘
```

**Project structure:**

```text
RoleGauge/
├── backend/          # FastAPI app, services, models, tests
├── frontend/          # Next.js app
├── knowledge-base/
│   ├── scoring/       # engine.json — weights, ceilings, curves
│   ├── roles/         # per-role skills, evidence patterns, target levels
│   ├── skills/
│   └── evidence/
├── docker-compose.yml
├── .env.example
├── API_CONTRACT.md
└── README.md
```

---

## 🔌 API

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/analyze` | Run multi-source analysis |
| `GET` | `/api/results/{id}` | Retrieve analysis |
| `POST` | `/api/cv/upload` | Parse CV (PDF/DOCX) |
| `POST` | `/api/linkedin/upload` | Parse LinkedIn PDF export |
| `GET` | `/api/assessment/{role}` | Get role-specific assessment |
| `POST` | `/api/assessment/evaluate` | Evaluate answers |
| `GET` | `/api/roles` | List roles |
| `POST` | `/api/auth/register` | Register (multi-user deployments) |
| `POST` | `/api/auth/login` | Login (returns JWT) |

Full contract, error codes, and auth header format: [`API_CONTRACT.md`](https://github.com/clbieren/RoleGauge/blob/main/API_CONTRACT.md). Interactive docs at `/docs` (Swagger) and `/redoc` once running.

---

## 🧪 Development Without Docker

**Backend:**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Tests

```bash
python -m pytest backend/tests -v
python -m pytest backend/tests --cov=app --cov-report=term-missing
```

Current coverage is not yet published as a badge — run the command above locally to check. Scoring engine tests live in `backend/tests/test_scoring_engine.py`; contributions adding edge-case tests there are especially welcome, since this module is the system's numeric authority.

---

## 🗺️ Roadmap

**🟢 Available:** GitHub repository analysis · CV parsing · LinkedIn parsing · deterministic scoring engine · 18 engineering roles · adaptive assessments · FastAPI backend · Next.js frontend · configurable knowledge base · pluggable AI providers

**🟡 Next:** Real-time analysis progress · WebSocket streaming · candidate benchmarking · improved GitHub analysis · more role knowledge bases · better local dev tooling · demo GIF/video · published test coverage badge · PII redaction before AI enrichment · data retention/deletion endpoint

**🔵 Community:** Embedded Systems Engineer · Cloud Architect · Site Reliability Engineer · Rust Engineer · community skill taxonomies · community evidence detectors

**🔮 Future:** GitHub App integration · ATS integrations · webhooks · organization dashboards · shareable skill profiles · GitHub README badges

---

## 🤝 Contributing

Good first contributions:

```text
Add a skill detection pattern
Improve a role taxonomy
Add scoring engine tests
Improve CV parsing
Add a new role
Improve evidence detection
Improve documentation
```

See `CONTRIBUTING.md` for setup and PR guidelines.

---

## 📜 License

MIT — see [`LICENSE`](https://github.com/clbieren/RoleGauge/blob/main/LICENSE).

---

## ⭐ Support RoleGauge

Star the repo · report bugs · open feature requests · contribute code · improve the knowledge base · share the project.

**RoleGauge** — *Don't just claim the skill. Show the evidence.*
