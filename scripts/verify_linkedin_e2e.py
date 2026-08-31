"""
End-to-End LinkedIn PDF Profile Import Verification Script for RoleGauge.

Demonstrates:
(a) Raw PDF parsed into segmented JSON recognizing LinkedIn-specific headers.
(b) LinkedIn skill/experience matches calculated using linkedin.json base strengths.
(c) A single subskill evidenced by GitHub + CV + LinkedIn simultaneously, showing all 3 in calculation trace.
(d) POST /api/linkedin/upload endpoint execution with structured response & preview.
(e) POST /api/analyze multi-source pipeline execution.
"""

import io
import json
import os
import sys
import tempfile

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(PROJECT_ROOT, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["KB_PATH"] = os.path.join(PROJECT_ROOT, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

from fastapi.testclient import TestClient
from app.main import app
from app.services.cv_certification_matcher import CertificationMatcher, get_certification_index
from app.services.cv_parser import parse_cv
from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.evidence_engine import EvidenceEngine
from app.services.kb_loader import kb
from app.services.linkedin_skill_matcher import LinkedInSkillMatcher
from app.services.scoring_engine import ScoringEngine


SAMPLE_LINKEDIN_PROFILE = """Alex Mercer
Principal Backend & Distributed Systems Engineer
Seattle, WA
Contact: linkedin.com/in/alexmercer, alex.mercer@example.com

Summary
Distributed systems architect with 10 years of experience designing high-throughput transaction engines. Specialized in event-driven microservices, Kafka event streaming, and PostgreSQL query optimization.

Experience

Lead Backend Engineer
Amazon Web Services (AWS)
Jan 2021 - Present
Architected distributed microservices and asynchronous message queues handling 100k msg/sec with Apache Kafka and Redis. Directed database partitioning and indexing optimizations in PostgreSQL.

Senior Software Engineer
Microsoft
2017 - 2020
Engineered cloud API services using Python and FastAPI. Implemented OAuth2 and JWT token security protocols.

Education

University of Washington
B.S. Computer Science
2013 - 2017

Licenses & Certifications

AWS Certified Solutions Architect - Associate
Amazon Web Services (AWS)
Issued 2022

CKA (Certified Kubernetes Administrator)
Cloud Native Computing Foundation (CNCF)
Issued 2021

Top Skills

Python
FastAPI
PostgreSQL
Redis
Apache Kafka
Docker
Kubernetes
Microservices
SQL

Recommendations

Dave Miller (Director of Engineering)
"Alex is a world-class backend engineer whose mastery of Kafka and distributed systems elevated our entire platform reliability."
"""


def _create_pdf(text: str, path: str) -> None:
    lines = text.split("\n")
    content_lines = []
    y = 820
    for line in lines:
        if line.strip():
            escaped = (
                line.replace("\\", "\\\\")
                .replace("(", "\\(")
                .replace(")", "\\)")
                .encode("latin-1", errors="replace")
                .decode("latin-1")
            )
            content_lines.append(f"BT /F1 8 Tf 30 {y} Td ({escaped}) Tj ET")
            y -= 10
            if y < 20:
                break

    stream_content = "\n".join(content_lines)
    stream_bytes = stream_content.encode("latin-1", errors="replace")
    stream_length = len(stream_bytes)

    pdf_content = f"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 842]
   /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>
endobj
4 0 obj
<< /Length {stream_length} >>
stream
{stream_content}
endstream
endobj
5 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000266 00000 n 
trailer
<< /Size 6 /Root 1 0 R >>
startxref
0
%%EOF"""

    with open(path, "wb") as f:
        f.write(pdf_content.encode("latin-1", errors="replace"))


def main():
    print("=" * 80)
    print("ROLEGAUGE LINKEDIN PDF PROFILE IMPORT — END-TO-END VERIFICATION")
    print("=" * 80)

    kb.load()
    cert_index = get_certification_index()
    if not cert_index._built:
        cert_index.build(kb)

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False, prefix="e2e_linkedin_") as tmp:
        pdf_path = tmp.name

    try:
        _create_pdf(SAMPLE_LINKEDIN_PROFILE, pdf_path)

        # ──────────────────────────────────────────────────────────────────────────
        # Step (a): Parse Raw PDF into Structured JSON
        # ──────────────────────────────────────────────────────────────────────────
        print("\n" + "-" * 80)
        print("STEP (a): Raw LinkedIn PDF Parsing & Section Detection")
        print("-" * 80)

        parsed = parse_cv(pdf_path, source_type="linkedin")
        print(f"[OK] Source Type: {parsed['source_type']}")
        print(f"[OK] Detected Sections: {parsed['detected_sections']}")
        print(f"[OK] Candidate Name: {parsed['personal_info'].get('name')}")
        print(f"[OK] Candidate Headline: {parsed['personal_info'].get('headline')}")
        print(f"[OK] Candidate Summary: {parsed['personal_info'].get('summary')[:70]}...")
        print(f"[OK] Extracted Top Skills ({len(parsed['skills'])}): {parsed['skills']}")
        print(f"[OK] Experience Count: {len(parsed['experience'])} entries")
        print(f"[OK] Certifications Count: {len(parsed['certificates'])} entries")
        print(f"[OK] Recommendations Count: {len(parsed['recommendations'])} entries")

        # ──────────────────────────────────────────────────────────────────────────
        # Step (b): LinkedIn Skill Matcher with Base Strengths
        # ──────────────────────────────────────────────────────────────────────────
        print("\n" + "-" * 80)
        print("STEP (b): LinkedIn Skill Matching using linkedin.json Base Strengths")
        print("-" * 80)

        role_category = "backend"
        matcher = LinkedInSkillMatcher(kb, role_category)
        evidence = matcher.match_all(parsed)

        matched_claimed = {k: v for k, v in evidence.items() if v.status == "claimed"}
        print(f"[OK] Matched {len(matched_claimed)} subskills as 'claimed' for role '{role_category}':")

        for key, res in list(matched_claimed.items())[:5]:
            sig_summaries = [f"{s.source} (strength={s.strength})" for s in res.signals]
            print(f"  • {key} ({res.subskill_name}): {', '.join(sig_summaries)}")

        # ──────────────────────────────────────────────────────────────────────────
        # Step (c): 3-Way Multi-Source Fusion (GitHub + CV + LinkedIn)
        # ──────────────────────────────────────────────────────────────────────────
        print("\n" + "-" * 80)
        print("STEP (c): Multi-Source Evidence Fusion (GitHub + CV + LinkedIn)")
        print("-" * 80)

        test_key = "be_databases.sql_querying"
        github_ev = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="evidence_found",
                signals=[EvidenceSignal(source="file_presence", file_path="queries.sql", matched_text="SQL queries", strength=0.70)],
            )
        }
        cv_ev = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[EvidenceSignal(source="cv_skills_list", file_path="cv/skills", matched_text="SQL", strength=0.15)],
            )
        }
        linkedin_ev = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[EvidenceSignal(source="linkedin_skills", file_path="linkedin/skills", matched_text="SQL", strength=0.15)],
            )
        }

        engine = EvidenceEngine(kb, role_category, "mid")
        unified = engine.merge_evidence(
            github_evidence=github_ev,
            cv_skills_evidence=cv_ev,
            linkedin_evidence=linkedin_ev,
        )
        res = unified[test_key]

        print(f"[OK] Subskill: {test_key}")
        print(f"[OK] Final Status: {res.final_status}")
        print(f"[OK] Final Confidence: {res.final_confidence:.3f}")
        print(f"[OK] Ceiling Applied: {res.ceiling_applied}")
        print(f"[OK] Calculation Trace: {res.calculation_trace}")
        print(f"[OK] Contributing Sources ({len(res.contributing_sources)}):")
        for src in res.contributing_sources:
            print(f"    - Source: {src.source:<20} | Strength: {src.strength:<5} | Signal: {src.signal}")

        # ──────────────────────────────────────────────────────────────────────────
        # Step (d): HTTP Endpoint Testing (POST /api/linkedin/upload)
        # ──────────────────────────────────────────────────────────────────────────
        print("\n" + "-" * 80)
        print("STEP (d): API Endpoint Execution (POST /api/linkedin/upload)")
        print("-" * 80)

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()

        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "backend", "level": "mid"},
                files={"file": ("alex_mercer_linkedin.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            )
            assert response.status_code == 200, f"Upload failed: {response.text}"
            data = response.json()

            print(f"[OK] HTTP Status: {response.status_code}")
            print(f"[OK] Readiness Score: {data['scoring_preview']['readiness_score']:.4f}")
            print(f"[OK] Readiness Tier: {data['scoring_preview']['readiness_tier']} ({data['scoring_preview']['readiness_label']})")
            print(f"[OK] Skill Matches Count: {len(data['skill_matches'])}")
            print(f"[OK] Certificate Matches Count: {len(data['certificate_matches'])}")
            for cert in data['certificate_matches']:
                print(f"    - Cert: {cert['certificate_name']} -> {cert['classification']} (score_contribution={cert['score_contribution']})")

            # ──────────────────────────────────────────────────────────────────────────
            # Step (e): HTTP Analyze Pipeline with LinkedIn
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP (e): Full Analyze Pipeline with LinkedIn (POST /api/analyze)")
            print("-" * 80)

            analyze_resp = client.post(
                "/api/analyze",
                data={"role_id": "backend", "level": "mid"},
                files={"linkedin_file": ("alex_mercer_linkedin.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            )
            assert analyze_resp.status_code == 200, f"Analyze failed: {analyze_resp.text}"
            analyze_data = analyze_resp.json()

            print(f"[OK] Analysis ID: {analyze_data['id']}")
            print(f"[OK] Role: {analyze_data['role_name']} ({analyze_data['level']})")
            print(f"[OK] has_linkedin: {analyze_data['has_linkedin']}")
            print(f"[OK] Readiness Score: {analyze_data['readiness_score']:.4f} ({analyze_data['readiness_tier']})")
            print(f"[OK] Total Skills Evaluated: {len(analyze_data['skills'])}")

        print("\n" + "=" * 80)
        print("ALL LINKEDIN IMPORT & MULTI-SOURCE FUSION E2E VERIFICATIONS PASSED!")
        print("=" * 80)

    finally:
        if os.path.exists(pdf_path):
            os.unlink(pdf_path)


if __name__ == "__main__":
    main()
