# RoleGauge

RoleGauge is an automated technical skill evaluation and readiness scoring engine for engineering roles. It analyzes GitHub repositories, parsed CVs (PDF/DOCX), and LinkedIn profiles against comprehensive role-specific knowledge bases to calculate verifiable readiness scores.

> [!NOTE]
> **AI Enrichment Status:**
> AI enrichment is currently disabled platform-wide (cost/business decision). The infrastructure remains intact (`ai_provider.py`, `test_ai_provider.py`) for future re-activation.
> All evaluations currently run through high-accuracy, deterministic keyword and heuristic pattern detection rules.

---

## Core Features

- **Multi-Source Evidence Fusion**: Blends code-level GitHub repository evidence, parsed CV mentions/projects, and LinkedIn certifications into unified subskill results.
- **Dynamic Scoring Engine**: Evaluates readiness scores using weighted criteria, signal ceilings, diminishing returns, and prerequisite weightings defined in the knowledge base.
- **Adaptive Q&A Assessments**: Generates interactive targeted technical questions to verify candidate claimed skills or fill evidence gaps.
- **Advertising Integration**: Provides backend-controlled signals (`ad_placements`, `analysis_tier`) for frontend banner monetization on loading and result screens while keeping candidate landing flows distraction-free.

---

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 16+ (or SQLite in-memory for testing)

### Running Backend Tests
```bash
python -m pytest backend/tests
```

### Running Backend Server
```bash
uvicorn app.main:app --reload --port 8000
```