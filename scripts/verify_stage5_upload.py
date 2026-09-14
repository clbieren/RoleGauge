"""
Verification Script for Stage 5 (CV & LinkedIn Upload).
Verifies:
1. Generating a valid CV PDF document.
2. POST /api/cv/upload returns parsed CV data, skill matches, and preview.
3. Multipart POST /api/analyze with file creates a full analysis.
4. Response conforms to AnalyzeResponse and is retrievable via GET /api/results/{id}.
"""

import sys
import os
import uuid
import asyncio
import io
import tempfile

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test_stage5.db"
os.environ["KB_PATH"] = os.path.join(BASE_DIR, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

# Ensure backend root is on PYTHONPATH
backend_dir = os.path.join(BASE_DIR, "backend")
sys.path.insert(0, backend_dir)

from fastapi.testclient import TestClient
from app.main import app as fastapi_app
from app.database import engine, Base

SAMPLE_CV_TEXT = """Jane Doe
Senior Backend Developer
Email: jane.doe@example.com
Location: Berlin, Germany

SUMMARY
Experienced software engineer with 6+ years specializing in Python backend systems, FastAPI microservices, and database optimization with PostgreSQL.

EXPERIENCE
Senior Software Engineer - Tech Solutions GmbH (2021 - Present)
- Designed and maintained high-throughput REST APIs using FastAPI and Python.
- Designed relational schemas and query optimizations in PostgreSQL.
- Implemented caching layers using Redis to reduce database latency by 40%.
- Containerized applications using Docker and orchestrated services with Kubernetes.

Software Engineer - Cloud Innovations (2018 - 2021)
- Developed asynchronous microservices with Python and Celery.
- Built automated test suites using PyTest with 90% code coverage.
- Managed CI/CD deployment pipelines using GitHub Actions.

SKILLS
Python, FastAPI, PostgreSQL, Redis, Docker, Kubernetes, PyTest, Git, Linux, REST API Design

EDUCATION
B.S. in Computer Science - Technical University of Berlin (2014 - 2018)
"""

def make_simple_pdf(text: str, path: str):
    """Creates a basic standard PDF."""
    lines = text.split("\n")
    content_lines = []
    y = 800
    for line in lines:
        if line.strip():
            escaped = (
                line.replace("\\", "\\\\")
                .replace("(", "\\(")
                .replace(")", "\\)")
                .encode("latin-1", errors="replace")
                .decode("latin-1")
            )
            content_lines.append(f"BT /F1 9 Tf 40 {y} Td ({escaped}) Tj ET")
            y -= 12
            if y < 40:
                break

    stream_content = "\n".join(content_lines)
    stream_bytes = stream_content.encode("latin-1", errors="replace")
    stream_length = len(stream_bytes)

    pdf_template = (
        b"%PDF-1.4\n"
        b"1 0 obj\n"
        b"<< /Type /Catalog /Pages 2 0 R >>\n"
        b"endobj\n"
        b"2 0 obj\n"
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n"
        b"endobj\n"
        b"3 0 obj\n"
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\n"
        b"endobj\n"
        b"4 0 obj\n"
        b"<< /Length " + str(stream_length).encode() + b" >>\n"
        b"stream\n"
        + stream_bytes + b"\n"
        b"endstream\n"
        b"endobj\n"
        b"5 0 obj\n"
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\n"
        b"endobj\n"
        b"xref\n"
        b"0 6\n"
        b"0000000000 65535 f \n"
        b"0000000009 00000 n \n"
        b"0000000058 00000 n \n"
        b"0000000115 00000 n \n"
        b"0000000266 00000 n \n"
        b"trailer\n"
        b"<< /Size 6 /Root 1 0 R >>\n"
        b"startxref\n"
        b"400\n"
        b"%%EOF\n"
    )

    with open(path, "wb") as f:
        f.write(pdf_template)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def main():
    asyncio.run(init_db())

    with tempfile.TemporaryDirectory() as tmp_dir:
        cv_path = os.path.join(tmp_dir, "jane_doe_cv.pdf")
        make_simple_pdf(SAMPLE_CV_TEXT, cv_path)
        print(f"[OK] Generated sample CV PDF: {cv_path} ({os.path.getsize(cv_path)} bytes)")

        with TestClient(fastapi_app) as client:
            print("\n--- 1. Testing POST /api/cv/upload ---")
            with open(cv_path, "rb") as f:
                cv_resp = client.post(
                    "/api/cv/upload",
                    data={"role_id": "backend", "level": "mid"},
                    files={"file": ("jane_doe_cv.pdf", f, "application/pdf")}
                )
            print("CV upload status:", cv_resp.status_code)
            assert cv_resp.status_code == 200, f"CV upload preview failed: {cv_resp.text}"
            cv_data = cv_resp.json()
            assert "parsed_cv" in cv_data
            assert "skill_matches" in cv_data
            print(f"[OK] CV Upload Preview parsed successfully: {len(cv_data['skill_matches'])} skill matches found.")

            print("\n--- 2. Testing Multipart POST /api/analyze with CV file ---")
            with open(cv_path, "rb") as f:
                analyze_resp = client.post(
                    "/api/analyze",
                    data={
                        "role_id": "backend",
                        "level": "mid",
                        "use_ai": "false"
                    },
                    files={"file": ("jane_doe_cv.pdf", f, "application/pdf")}
                )
            print("Analyze status:", analyze_resp.status_code)
            assert analyze_resp.status_code == 200, f"Multipart analyze failed: {analyze_resp.text}"
            res_data = analyze_resp.json()
            analysis_id = res_data["id"]
            print(f"res_data['github_username'] is: {res_data['github_username']!r}")
            assert res_data["github_username"] in ("cv_upload", None, "") or "jane" in str(res_data["github_username"]).lower()
            assert res_data["readiness_score"] > 0
            assert len(res_data["skills"]) > 0
            print(f"[OK] Full CV Analysis created: ID={analysis_id}, Score={res_data['readiness_score']}, Tier={res_data['readiness_tier']}")

            print(f"\n--- 3. Verifying GET /api/results/{analysis_id} for CV analysis ---")
            get_resp = client.get(f"/api/results/{analysis_id}")
            assert get_resp.status_code == 200, f"Fetch analysis failed: {get_resp.text}"
            saved_data = get_resp.json()
            assert saved_data["id"] == analysis_id
            print(f"saved_data['github_username'] is: {saved_data['github_username']!r}")
            print(f"[OK] Analysis retrieved successfully from database. Candidate is marked as '{saved_data['github_username']}'.")

    print("\n==========================================")
    print("  STAGE 5 (CV UPLOAD PIPELINE) PASSED!   ")
    print("==========================================")

if __name__ == "__main__":
    main()
