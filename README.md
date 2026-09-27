<div align="center">

# ⚡ RoleGauge

### Evidence-based engineering skill assessment

RoleGauge evaluates engineering readiness using real-world evidence from GitHub repositories, CVs, LinkedIn profiles, and technical assessments — not only self-reported skills.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](backend/requirements.txt)
[![Node 20+](https://img.shields.io/badge/node-20%2B-green.svg)](frontend/package.json)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](#roadmap)

> **Don't just claim the skill. Show the evidence.**

</div>

---

## 📸 Product Preview

RoleGauge turns technical evidence into a clear, role-specific readiness profile.

<div align="center">

<a href="Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-09-27%20114918.png">
  <img src="Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-09-27%20114918.png" alt="RoleGauge analysis dashboard" width="48%" />
</a>
<a href="Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-09-27%20114944.png">
  <img src="Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-09-27%20114944.png" alt="RoleGauge readiness profile" width="48%" />
</a>

</div>

---

## ✨ What RoleGauge Does

- **Analyzes GitHub repositories** — languages, dependencies, architecture, tests, and engineering signals
- **Parses CVs and LinkedIn exports** — extracts relevant experience and technical evidence
- **Maps evidence to role-specific skills** — powered by a configurable knowledge base
- **Calculates deterministic scores** — the scoring engine, not an LLM, owns the final score
- **Generates actionable readiness profiles** — strengths, gaps, evidence, and recommended next steps
- **Supports 18 engineering roles** — from Backend and Frontend Engineering to AI, DevOps, Data, and Security

```text
Evidence sources → Evidence Engine → Skill Matcher → Scoring Engine → Readiness Profile
```

## 🧮 Transparent, Deterministic Scoring

The `ScoringEngine` is the sole numeric authority. Optional AI enrichment may suggest evidence signals, but it never assigns the final score.

```text
skill_score = Σ (signal_weight × signal_confidence)
              capped at signal_ceiling
              adjusted for diminishing returns
              gated by prerequisites
```

Weights, ceilings, prerequisites, and target levels are configured in [`knowledge-base/`](knowledge-base/), rather than hard-coded in application logic.

## 🚀 Quick Start

### Docker (recommended)

**Requirements:** Docker, Docker Compose, and Git.

```bash
git clone https://github.com/clbieren/RoleGauge.git
cd RoleGauge
cp .env.example .env
docker compose up --build
```

Open the application:

| Service | URL |
|---|---|
| Frontend | http://localhost:3000 |
| API | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

Stop the services with `docker compose down`.

### Local development

```bash
# Backend
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload --port 8000
```

```bash
# Frontend (in a second terminal)
cd frontend
npm install
npm run dev
```

## 🔌 API Overview

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/analyze` | Run a multi-source analysis |
| `GET` | `/api/results/{id}` | Retrieve an analysis result |
| `POST` | `/api/cv/upload` | Parse a CV (PDF/DOCX) |
| `POST` | `/api/linkedin/upload` | Parse a LinkedIn PDF export |
| `GET` | `/api/assessment/{role}` | Get a role-specific assessment |
| `POST` | `/api/assessment/evaluate` | Evaluate assessment answers |
| `GET` | `/api/roles` | List supported roles |

See [`API_CONTRACT.md`](API_CONTRACT.md) for the complete contract, error codes, and authentication details.

## 🔒 Privacy by Default

AI enrichment is disabled by default:

```env
AI_PROVIDER=none
```

With the default configuration, evidence detection runs locally and no candidate data is sent to an external AI provider. If you enable an AI provider, review the data-flow notes in the [Security & Privacy section](#security--privacy) and ensure you are authorized to process the data.

### Security & Privacy

RoleGauge may process CVs, LinkedIn exports, GitHub tokens, and other candidate information. It is self-hosted, so you control the infrastructure, access, and retention policy. See [`SECURITY.md`](SECURITY.md) for vulnerability reporting.

## 🏗️ Architecture

```text
Frontend (Next.js / React / TypeScript)
                │
                ▼
Backend (FastAPI / Python)
                │
   ┌────────────┼────────────┐
   ▼            ▼            ▼
GitHub       CV & LinkedIn  Assessment
Fetcher      Parsers        Engine
                │
                ▼
Evidence Detection → Skill Matching → Deterministic Scoring
                │
        PostgreSQL + Redis
```

## 🧪 Tests

```bash
python -m pytest backend/tests -v
python -m pytest backend/tests --cov=app --cov-report=term-missing
```

## 🗺️ Roadmap

- **Available:** GitHub analysis, CV and LinkedIn parsing, deterministic scoring, 18 roles, adaptive assessments, FastAPI backend, and Next.js frontend
- **Next:** Real-time progress, WebSocket streaming, candidate benchmarking, expanded knowledge bases, and a demo video
- **Future:** GitHub App integration, ATS integrations, webhooks, organization dashboards, shareable profiles, and README badges

## 🤝 Contributing

Contributions are welcome. Useful starting points include:

- Add a skill detection pattern
- Improve a role taxonomy
- Add scoring-engine tests
- Improve CV parsing or evidence detection
- Add a new supported role
- Improve documentation

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## 📄 License

MIT — see [`LICENSE`](LICENSE).

---

<div align="center">

**RoleGauge** — *Don't just claim the skill. Show the evidence.*

</div>
