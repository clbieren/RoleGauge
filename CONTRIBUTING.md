# Contributing to RoleGauge

Thank you for your interest in contributing to RoleGauge! We welcome all kinds of contributions — bug reports, feature requests, documentation improvements, and code changes.

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Docker and Docker Compose (for containerized development)
- Git

### Local Development Setup

**1. Clone the repository:**

```bash
git clone https://github.com/clbieren/RoleGauge.git
cd RoleGauge
```

**2. Backend setup:**

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env
```

**3. Frontend setup:**

```bash
cd frontend
npm install
```

**4. Run tests:**

```bash
python -m pytest backend/tests -v
```

## Contribution Areas

We especially welcome contributions in these areas:

- **Skill Detection Patterns** — Add new evidence signals to `knowledge-base/evidence/`
- **Role Knowledge Bases** — Improve or add role taxonomies in `knowledge-base/roles/`
- **Scoring Engine Tests** — Add edge-case tests in `backend/tests/test_scoring_engine.py`
- **CV & LinkedIn Parsing** — Enhance parsers in `backend/app/services/`
- **New Roles** — Create new role definitions with skills and evidence patterns
- **Documentation** — Improve README, API docs, or add examples
- **Frontend Components** — Enhance UI/UX in `frontend/`

## Pull Request Process

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure:
   - Code follows existing style conventions
   - Tests pass locally: `pytest backend/tests -v`
   - No hardcoded secrets or API keys
   - Commit messages are clear and descriptive

3. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Open a Pull Request** on the main repository with:
   - Clear title and description
   - Link to related issues (if any)
   - Summary of changes

5. **Address feedback** from maintainers and reviewers

## Code Style

- **Python:** Follow PEP 8. Use `black` for formatting.
- **TypeScript/React:** Use `prettier` and `eslint`.
- **Git:** Write clear, imperative commit messages (`add feature X`, not `Added feature X`).

## Reporting Issues

Found a bug? Please open an issue with:

- **Description:** What is the problem?
- **Reproduction:** Steps to reproduce
- **Expected behavior:** What should happen?
- **Actual behavior:** What actually happens?
- **Environment:** Python version, OS, etc.

## Questions or Discussions

For questions about architecture, design decisions, or future directions, open a GitHub Discussion instead of an issue.

---

Thank you for contributing to RoleGauge! 🎉
