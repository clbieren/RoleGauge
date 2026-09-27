<div align="center">

<h1>⚡ RoleGauge</h1>

<p><strong>Automated Technical Skill Evaluation & Readiness Scoring Engine for Engineering Roles</strong></p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Next.js-16-000000?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js"/>
  <img src="https://img.shields.io/badge/PostgreSQL-16+-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Roles_Supported-18-6366f1?style=for-the-badge" alt="18 Roles"/>
  <img src="https://img.shields.io/badge/AI_Provider-Pluggable-f59e0b?style=for-the-badge" alt="AI"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge" alt="MIT"/>
</p>

</div>

---

## What is RoleGauge?

**RoleGauge** is a multi-source technical skill evaluation platform that generates **verifiable, data-driven readiness scores** for engineering candidates. Instead of relying on self-reported skills or generic interview questions, RoleGauge fuses evidence from three independent sources — **GitHub repositories**, **parsed CVs**, and **LinkedIn profiles** — and evaluates them against deep, role-specific knowledge bases.

The result is an objective, auditable readiness score that reflects real-world technical ability.

> [!NOTE]
> **AI Enrichment Status:** AI enrichment is currently disabled platform-wide (cost/business decision). The infrastructure remains fully intact (`ai_provider.py`) for future re-activation. All evaluations currently run through high-accuracy deterministic keyword and heuristic pattern detection.

---

## Core Features

| Feature | Description |
|---|---|
| **Multi-Source Evidence Fusion** | Blends GitHub code evidence, CV project mentions, and LinkedIn certifications into unified subskill verdicts |
| **Dynamic Scoring Engine** | Weighted criteria with signal ceilings, diminishing returns, and prerequisite logic — all configurable via `engine.json` |
| **Adaptive Q&A Assessments** | Generates targeted technical questions to verify claimed skills or fill evidence gaps |
| **GitHub Deep Scan** | Analyzes repositories, languages, file patterns, dependencies, and code structure at scale |
| **CV Parsing** | Extracts skills, projects, certifications from PDF and DOCX formats |
| **LinkedIn Profile Parsing** | Matches certifications and endorsements against role-specific skill taxonomies |
| **Tiered Rate Limiting** | Per-IP and per-user rate limits with Redis-backed enforcement in production |
| **Pluggable AI Providers** | Supports OpenAI, Gemini, and Groq for AI-enriched evidence detection (dormant, ready to activate) |

---

## Supported Engineering Roles

RoleGauge ships with **18 built-in role knowledge bases**, each containing hundreds of scored subskills:

| | | |
|---|---|---|
| AI Engineer | DevOps Engineer | Network Engineer |
| Android Developer | Frontend Engineer | QA Engineer |
| Backend Engineer | Game Developer | Technical Writer |
| Blockchain Developer | iOS Developer | UX Designer |
| Cyber Security Engineer | Machine Learning Engineer | API Design Specialist |
| Data Analyst | MLOps Engineer | |
| Data Engineer | | |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                            RoleGauge                                │
├──────────────────────┬──────────────────────────────────────────────┤
│   Frontend           │   Backend (FastAPI + Python 3.11)            │
│                      │                                              │
│   Next.js 16         │  ┌──────────────────────────────────────┐   │
│   React 19           │  │           Analysis Pipeline           │   │
│   TypeScript         │  │                                      │   │
│   Recharts           │  │  GitHub Fetcher  ──►  Evidence Engine│   │
│                      │  │  CV Parser       ──►  Skill Matcher  │   │
│                      │  │  LinkedIn Parser ──►  Cert Matcher   │   │
│                      │  └──────────────┬───────────────────────┘   │
│                      │                 │                            │
│                      │  ┌──────────────▼───────────────────────┐   │
│                      │  │           Scoring Engine              │   │
│                      │  │                                      │   │
│                      │  │  Knowledge Base  ──►  Weighted Score │   │
│                      │  │  Signal Ceilings + Diminishing Returns│   │
│                      │  │  Prerequisite Logic + Denominator     │   │
│                      │  └──────────────────────────────────────┘   │
├──────────────────────┼──────────────────────────────────────────────┤
│   PostgreSQL 16+     │   Redis (Rate Limiting — Production)         │
└──────────────────────┴──────────────────────────────────────────────┘
```

---

## Getting Started

### Prerequisites

- **Python** 3.11+
- **Node.js** 18+
- **PostgreSQL** 16+ (or Docker)
- **Docker & Docker Compose** (recommended)

---

### Option 1: Docker Compose (Recommended)

The fastest way to get the full stack running locally.

**1. Clone the repository**
```bash
git clone https://github.com/your-org/rolegauge.git
cd rolegauge
```

**2. Configure environment variables**
```bash
cp .env.example .env
# Edit .env — at minimum, set GITHUB_TOKEN for higher API rate limits
```

**3. Start all services**
```bash
docker-compose up --build
```

| Service | URL |
|---|---|
| Frontend | `http://localhost:3000` |
| Backend API | `http://localhost:8000` |
| API Docs (Swagger UI) | `http://localhost:8000/docs` |
| API Docs (ReDoc) | `http://localhost:8000/redoc` |

> [!IMPORTANT]
> Redis is **mandatory** in production for rate limiting. Add `REDIS_URL=redis://your-redis:6379` to your `.env`. Without Redis, in-memory rate limit counters are not shared across workers or container replicas — clients can bypass limits by distributing requests across workers.

---

### Option 2: Manual Setup

#### Backend

```bash
cd backend

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp ../.env.example .env
# Edit .env with DATABASE_URL, GITHUB_TOKEN, etc.

# Run the development server
uvicorn app.main:app --reload --port 8000
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
# → http://localhost:3000
```

---

### Running Tests

```bash
# From the project root
python -m pytest backend/tests -v

# With coverage report
python -m pytest backend/tests --cov=app --cov-report=term-missing
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```env
# Application
APP_NAME=RoleGauge
DEBUG=false
BACKEND_PORT=8000
FRONTEND_PORT=3000

# Database — PostgreSQL REQUIRED for production
DATABASE_URL=postgresql+asyncpg://rolegauge:rolegauge@db:5432/rolegauge

# GitHub API
GITHUB_TOKEN=              # Optional — raises rate limit 60 → 5,000 req/hr
GITHUB_MAX_REPOS=100
GITHUB_MAX_FILE_SIZE=500000

# AI Provider — "none" | "openai" | "groq" | "gemini"
AI_PROVIDER=none
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
GROQ_API_KEY=
GROQ_MODEL=llama-3.3-70b-versatile
GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.0-flash

# Redis — REQUIRED in production
# REDIS_URL=redis://localhost:6379

# CORS allowed origins
CORS_ORIGINS=["http://localhost:3000"]
```

---

## API Overview

Full interactive documentation is served at `/docs` (Swagger UI) and `/redoc` when the backend is running.

### Key Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/analyze` | Run full multi-source analysis | Optional |
| `GET` | `/api/results/{id}` | Fetch analysis result by ID | Optional |
| `POST` | `/api/cv/upload` | Parse PDF/DOCX and extract skills | Optional |
| `POST` | `/api/linkedin/upload` | Parse LinkedIn PDF export | Optional |
| `GET` | `/api/assessment/{role}` | Fetch adaptive Q&A assessment | Optional |
| `POST` | `/api/assessment/evaluate` | Submit and score answers | Optional |
| `GET` | `/api/roles` | List all supported roles | Public |
| `POST` | `/api/auth/register` | Create a new account | Public |
| `POST` | `/api/auth/login` | Authenticate and receive JWT | Public |

### Rate Limits

| Endpoint | Guest (IP-based) | Authenticated User |
|---|---|---|
| `POST /api/analyze` | 5 / hour | 20 / hour |
| `POST /api/auth/login` | 5 / 15 min | 5 / 15 min |
| `POST /api/auth/register` | 5 / 15 min | 5 / 15 min |
| `POST /api/cv/upload` | 10 / hour | 30 / hour |
| `POST /api/linkedin/upload` | 10 / hour | 30 / hour |

> For the complete API contract, error codes, and request/response schemas, see [`API_CONTRACT.md`](./API_CONTRACT.md).

---

## Scoring Engine

The backend `ScoringEngine` is the **sole numeric authority** — external AI models detect evidence signals only; they never generate scores.

```
                   Σ ( subskill_weight × evidence_score × signal_ceiling_factor )
Final Score  =    ──────────────────────────────────────────────────────────────────
                              Σ ( subskill_weight × denominator_factor )
```

All parameters are defined declaratively in the knowledge base — no hard-coded formulas:

```
knowledge-base/
├── scoring/
│   └── engine.json          ←  Weights, ceilings, diminishing returns factor
├── roles/
│   └── <role-name>/         ←  Per-role subskill definitions & target levels
├── skills/                  ←  Shared skill taxonomy
└── evidence/                ←  Evidence detection patterns & keyword sets
```

---

## Project Structure

```
rolegauge/
├── backend/                 ←  FastAPI application
│   ├── app/
│   │   ├── routers/         ←  API route handlers (analyze, auth, cv, linkedin, …)
│   │   ├── services/        ←  Business logic (scoring, parsing, evidence, AI)
│   │   └── models/          ←  SQLAlchemy ORM models
│   └── tests/               ←  Pytest test suite
├── frontend/                ←  Next.js 16 application
│   └── src/
├── knowledge-base/          ←  Role definitions, skill taxonomy, scoring config
├── docker-compose.yml
└── .env.example
```

---

## Roadmap

- [ ] Redis integration for production-grade rate limiting
- [ ] AI enrichment re-activation (OpenAI / Gemini / Groq)
- [ ] Real-time analysis progress streaming via WebSockets
- [ ] Candidate comparison & benchmarking dashboard
- [ ] Webhook support for ATS (Applicant Tracking System) integrations
- [ ] Additional roles: Embedded Systems, Cloud Architect, Site Reliability Engineer

---

## Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/): `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

<div align="center">
  <sub>Built with care by the RoleGauge team</sub>
</div>
