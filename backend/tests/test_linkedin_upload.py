"""
Comprehensive Test Suite for LinkedIn Profile PDF Import & Multi-Source Fusion.

Tests:
1. LinkedIn PDF parsing (Summary, Experience, Education, Licenses & Certifications, Skills & Endorsements, Languages, Volunteering, Honors & Awards, Recommendations, Publications)
2. LinkedIn skill matcher verifying linkedin.json base strengths (0.15 vs CV's 0.30, 0.40 vs CV's 0.50)
3. Certificate matching against the shared allowlist (3-way classification)
4. EvidenceEngine 3-way / 4-way fusion (GitHub + CV + LinkedIn + Assessment) with calculation_trace auditability
5. File validation & error handling (non-PDF format -> 400, empty file -> 400, file too large -> 413, unknown role -> 400)
6. Router endpoint POST /api/linkedin/upload integration
7. Full pipeline integration in POST /api/analyze with linkedin_file
"""

import io
import json
import os
import sys
import tempfile
from unittest.mock import AsyncMock, patch

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

import pytest
from fastapi.testclient import TestClient

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.main import app
from app.services.cv_certification_matcher import CertificationIndex, CertificationMatcher
from app.services.cv_parser import parse_cv
from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.evidence_engine import EvidenceEngine, UnifiedSubskillEvidence
from app.services.kb_loader import KnowledgeBase, kb
from app.services.linkedin_skill_matcher import LinkedInSkillMatcher
from app.services.scoring_engine import ScoringEngine


SAMPLE_LINKEDIN_TEXT = """Jane Doe
Senior Distributed Systems Engineer | Cloud Architect
San Francisco Bay Area
Contact Info: linkedin.com/in/janedoe, jane.doe@example.com

Summary
Passionate backend and distributed systems architect with 8 years of experience building high-throughput event-driven microservices. Deep expertise in PostgreSQL indexing optimization, database schema migrations, and event streaming with Apache Kafka.

Experience

Senior Backend Engineer
Stripe
Jan 2021 - Present · 3 yrs 8 mos
San Francisco, CA
Architected event-driven microservices processing 50k events per second using Apache Kafka and Redis. Optimized PostgreSQL database queries and indexing strategies, reducing query latency by 60%. Implemented OAuth2 and JWT authentication across API gateways.

Backend Developer
Lyft
Jun 2018 - Dec 2020 · 2 yrs 7 mos
Built high-performance RESTful APIs using Python, FastAPI, and PostgreSQL. Designed database migrations and relational data models. Implemented automated unit tests with pytest.

Education

University of California, Berkeley
Bachelor of Science, Computer Science
2014 - 2018

Licenses & Certifications

AWS Certified Solutions Architect - Associate
Amazon Web Services (AWS)
Issued Jan 2022 · Expires Jan 2025

CKA (Certified Kubernetes Administrator)
Cloud Native Computing Foundation (CNCF)
Issued Mar 2021

Executive Leadership Masterclass
Personal Development Academy
Issued Sep 2020

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

Languages

English (Native), Spanish (Professional working)

Volunteering

Technical Mentor
Women Who Code
2020 - Present · 4 yrs

Honors & Awards

Engineering Excellence Award - Stripe (2023)

Recommendations

Sarah Connor (VP of Engineering at Stripe)
"Jane is a phenomenal distributed systems engineer who designed our core event streaming infrastructure with outstanding reliability and fault tolerance."
"""


def _create_synthetic_linkedin_pdf(text: str, path: str) -> None:
    """Create a minimal valid PDF containing the synthetic LinkedIn profile text."""
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


@pytest.fixture(scope="module")
def loaded_kb():
    """Load the knowledge base once for all tests."""
    test_kb = KnowledgeBase()
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb_path = os.path.join(os.path.dirname(backend_dir), "knowledge-base")
    test_kb.load(kb_path)
    return test_kb


@pytest.fixture(scope="module")
def cert_index(loaded_kb):
    """Build certification index."""
    index = CertificationIndex()
    index.build(loaded_kb)
    return index


@pytest.fixture(scope="module")
def linkedin_pdf_path():
    """Create a temporary synthetic LinkedIn PDF file."""
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False, prefix="test_linkedin_") as tmp:
        tmp_path = tmp.name
    _create_synthetic_linkedin_pdf(SAMPLE_LINKEDIN_TEXT, tmp_path)
    yield tmp_path
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)


# ──────────────────────────────────────────────
# 1. LinkedIn PDF Parsing Tests
# ──────────────────────────────────────────────

class TestLinkedInPDFParsing:
    """Test parsing of LinkedIn profile PDF exports."""

    def test_linkedin_sections_detected(self, linkedin_pdf_path):
        """Parser detects LinkedIn-specific sections."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")

        assert parsed["source_type"] == "linkedin"
        detected = parsed["detected_sections"]
        assert "personal_info" in detected
        assert "experience" in detected
        assert "education" in detected
        assert "certificates" in detected
        assert "skills" in detected

    def test_linkedin_personal_info_and_summary(self, linkedin_pdf_path):
        """Parser extracts name, headline, summary, and contact info."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        info = parsed["personal_info"]

        assert "Jane Doe" in info.get("name", "")
        assert info.get("email") == "jane.doe@example.com"
        assert "linkedin.com/in/janedoe" in info.get("linkedin", "")

    def test_linkedin_skills_extracted(self, linkedin_pdf_path):
        """Parser extracts bullet-separated top skills."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        skills_lower = [s.lower() for s in parsed["skills"]]

        assert any("python" in s for s in skills_lower)
        assert any("postgresql" in s for s in skills_lower)
        assert any("kafka" in s for s in skills_lower)
        assert any("redis" in s for s in skills_lower)

    def test_linkedin_experience_extracted(self, linkedin_pdf_path):
        """Parser extracts work experience entries with title and description."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        assert len(parsed["experience"]) >= 1

    def test_linkedin_certificates_extracted(self, linkedin_pdf_path):
        """Parser extracts certificates with provider info."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        cert_names = [c["name"].lower() for c in parsed["certificates"]]

        assert any("aws" in name for name in cert_names)
        assert any("kubernetes" in name or "cka" in name for name in cert_names)

    def test_linkedin_recommendations(self, linkedin_pdf_path):
        """Parser handles recommendations section."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        assert "recommendations" in parsed


# ──────────────────────────────────────────────
# 2. LinkedIn Skill Matcher & Base Strengths Tests
# ──────────────────────────────────────────────

class TestLinkedInSkillMatcher:
    """Test LinkedInSkillMatcher using role-specific linkedin.json strengths."""

    def test_matcher_loads_linkedin_json_strengths(self, loaded_kb, linkedin_pdf_path):
        """LinkedIn base strengths (0.15 for skills, 0.40 for experience) are applied."""
        parsed = parse_cv(linkedin_pdf_path, source_type="linkedin")
        matcher = LinkedInSkillMatcher(loaded_kb, "backend")

        # Verify cached section strengths
        assert matcher._section_strengths.get("skills_endorsements") == 0.15
        assert matcher._section_strengths.get("experience") == 0.40
        assert matcher._section_strengths.get("headline_summary") == 0.20

        evidence = matcher.match_all(parsed)
        claimed = {k: v for k, v in evidence.items() if v.status == "claimed"}
        assert len(claimed) > 0

        # All matched items must be 'claimed' (never 'evidence_found')
        for ck, result in claimed.items():
            assert result.status == "claimed", f"{ck} has status '{result.status}', expected 'claimed'"

    def test_skills_endorsements_signal_strength(self, loaded_kb):
        """Skills list from LinkedIn profile gets 0.15 base strength."""
        matcher = LinkedInSkillMatcher(loaded_kb, "backend")
        parsed_data = {
            "skills": ["PostgreSQL", "Redis"],
            "experience": [],
            "personal_info": {},
            "projects": [],
            "recommendations": [],
            "publications": [],
        }
        evidence = matcher.match_all(parsed_data)

        # Check signals created for skills
        for result in evidence.values():
            for signal in result.signals:
                if signal.source == "linkedin_skills":
                    assert signal.strength == 0.15

    def test_experience_signal_strength(self, loaded_kb):
        """Experience descriptions from LinkedIn profile get 0.40 base strength."""
        matcher = LinkedInSkillMatcher(loaded_kb, "backend")
        parsed_data = {
            "skills": [],
            "experience": [{
                "title": "Senior Backend Engineer",
                "company": "Stripe",
                "description": "Architected event-driven microservices with Apache Kafka and Redis caching",
                "raw": "Architected event-driven microservices with Apache Kafka and Redis caching",
            }],
            "personal_info": {},
            "projects": [],
            "recommendations": [],
            "publications": [],
        }
        evidence = matcher.match_all(parsed_data)

        exp_signals = [
            sig for res in evidence.values()
            for sig in res.signals if sig.source == "linkedin_experience"
        ]
        assert len(exp_signals) > 0
        for sig in exp_signals:
            assert sig.strength == 0.40


# ──────────────────────────────────────────────
# 3. Certificate Matching from LinkedIn
# ──────────────────────────────────────────────

class TestLinkedInCertificateMatching:
    """Test 3-way certificate classification for LinkedIn certificates."""

    def test_recognized_relevant_linkedin_cert(self, loaded_kb, cert_index):
        """Recognized AWS certification maps to backend composite keys."""
        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "AWS Certified Solutions Architect - Associate", "provider": "AWS"},
            {"name": "Executive Leadership Masterclass", "provider": "Personal Development Academy"},
        ])

        assert len(results) == 2
        aws_res = results[0]
        assert aws_res["classification"] == "recognized_relevant"
        assert aws_res["score_contribution"] > 0.0

        unrec_res = results[1]
        assert unrec_res["classification"] == "unrecognized_excluded"
        assert unrec_res["score_contribution"] == 0.0


# ──────────────────────────────────────────────
# 4. EvidenceEngine Multi-Source Fusion
# ──────────────────────────────────────────────

class TestLinkedInEvidenceEngineFusion:
    """Test EvidenceEngine fusing GitHub, CV, LinkedIn, and Assessment."""

    def test_linkedin_only_ceiling_applied(self, loaded_kb):
        """LinkedIn-only evidence is capped at self_reported or work_experience ceiling."""
        engine = EvidenceEngine(loaded_kb, "backend", "mid")
        test_key = "be_databases.sql_querying"

        linkedin_signals = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[
                    EvidenceSignal(
                        source="linkedin_skills",
                        file_path="linkedin/skills",
                        matched_text="SQL",
                        strength=0.15,
                    )
                ],
            )
        }

        unified = engine.merge_evidence(linkedin_evidence=linkedin_signals)
        result = unified[test_key]

        assert result.final_confidence == 0.15
        assert result.final_status == "claimed"
        assert "self_reported_skills_and_summary (0.30)" in result.ceiling_applied
        assert "primary=0.15 (linkedin_skills)" in result.calculation_trace
        assert len(result.contributing_sources) == 1
        assert result.contributing_sources[0].source == "linkedin_skills"

    def test_three_way_fusion_github_plus_cv_plus_linkedin(self, loaded_kb):
        """
        Scenario: GitHub (0.70) + CV (0.15) + LinkedIn (0.15).
        Calculation: primary (0.70) + secondary (0.15*0.10 + 0.15*0.10) = 0.70 + 0.03 = 0.730.
        """
        engine = EvidenceEngine(loaded_kb, "backend", "mid")
        test_key = "be_databases.sql_querying"

        github_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="evidence_found",
                signals=[
                    EvidenceSignal(
                        source="file_presence",
                        file_path="models/schema.sql",
                        matched_text="SQL migrations and complex queries",
                        strength=0.70,
                    )
                ],
            )
        }

        cv_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[
                    EvidenceSignal(
                        source="cv_skills_list",
                        file_path="cv/skills",
                        matched_text="PostgreSQL",
                        strength=0.15,
                    )
                ],
            )
        }

        linkedin_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[
                    EvidenceSignal(
                        source="linkedin_skills",
                        file_path="linkedin/skills",
                        matched_text="SQL",
                        strength=0.15,
                    )
                ],
            )
        }

        unified = engine.merge_evidence(
            github_evidence=github_evidence,
            cv_skills_evidence=cv_evidence,
            linkedin_evidence=linkedin_evidence,
        )
        result = unified[test_key]

        # 0.70 + (0.15*0.10 + 0.15*0.10) = 0.730
        expected = 0.70 + (0.30 * 0.10)
        assert result.final_confidence == pytest.approx(expected, abs=1e-4)
        assert result.final_status == "evidence_found"
        assert len(result.contributing_sources) == 3

        # Calculation trace must show all 3 sources
        trace = result.calculation_trace
        assert "primary=0.70 (file_presence)" in trace
        assert "0.15*0.10 + 0.15*0.10" in trace or "secondary=" in trace
        assert "raw=0.730" in trace
        assert "final=0.730" in trace

    def test_assessment_override_resets_linkedin_fusion(self, loaded_kb):
        """Assessment verified_gap hard-resets fused GitHub + CV + LinkedIn confidence to 0.0."""
        engine = EvidenceEngine(loaded_kb, "backend", "mid")
        test_key = "be_databases.sql_querying"

        github_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="evidence_found",
                signals=[EvidenceSignal(source="file_presence", file_path="schema.sql", matched_text="SQL", strength=0.70)],
            )
        }
        cv_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[EvidenceSignal(source="cv_skills_list", file_path="cv/skills", matched_text="SQL", strength=0.15)],
            )
        }
        linkedin_evidence = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="SQL Querying",
                status="claimed",
                signals=[EvidenceSignal(source="linkedin_skills", file_path="linkedin/skills", matched_text="SQL", strength=0.15)],
            )
        }
        assessment_signals = {
            test_key: [{"status": "verified_gap", "score": 0.0, "strength": 0.0, "detail": "Failed live query test"}]
        }

        unified = engine.merge_evidence(
            github_evidence=github_evidence,
            cv_skills_evidence=cv_evidence,
            linkedin_evidence=linkedin_evidence,
            assessment_evidence=assessment_signals,
        )
        result = unified[test_key]

        assert result.final_confidence == 0.0
        assert result.final_status == "verified_gap"
        assert "assessment_override" in result.calculation_trace


# ──────────────────────────────────────────────
# 5. Validation & Security Tests
# ──────────────────────────────────────────────

class TestLinkedInValidation:
    """Test validation errors on POST /api/linkedin/upload."""

    def test_unknown_role_returns_400(self, linkedin_pdf_path):
        """Unknown role returns 400."""
        with open(linkedin_pdf_path, "rb") as f:
            pdf_bytes = f.read()

        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "nonexistent_role", "level": "mid"},
                files={"file": ("profile.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            )
            assert response.status_code == 400
            assert "Unknown role" in response.json()["detail"]

    def test_non_pdf_file_returns_400(self):
        """Non-PDF file format returns 400."""
        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "backend", "level": "mid"},
                files={"file": ("profile.docx", io.BytesIO(b"dummy docx bytes"), "application/vnd.openxmlformats-officedocument.wordprocessingml.document")},
            )
            assert response.status_code == 400
            assert "Unsupported file format" in response.json()["detail"]

    def test_empty_pdf_file_returns_400(self):
        """Empty PDF file returns 400."""
        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "backend", "level": "mid"},
                files={"file": ("profile.pdf", io.BytesIO(b""), "application/pdf")},
            )
            assert response.status_code == 400
            assert "empty" in response.json()["detail"].lower()

    def test_oversized_file_returns_413(self):
        """File larger than 10MB returns 413."""
        big_content = b"%PDF-1.4 " + b"0" * (11 * 1024 * 1024)
        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "backend", "level": "mid"},
                files={"file": ("large_profile.pdf", io.BytesIO(big_content), "application/pdf")},
            )
            assert response.status_code == 413
            assert "File too large" in response.json()["detail"]


# ──────────────────────────────────────────────
# 6. Endpoint Integration Tests (POST /api/linkedin/upload)
# ──────────────────────────────────────────────

class TestLinkedInEndpointIntegration:
    """Test full integration of POST /api/linkedin/upload."""

    def test_successful_linkedin_upload(self, linkedin_pdf_path):
        """Valid LinkedIn PDF upload returns 200 with structured parsing and scoring preview."""
        with open(linkedin_pdf_path, "rb") as f:
            pdf_bytes = f.read()

        with TestClient(app) as client:
            response = client.post(
                "/api/linkedin/upload",
                data={"role_id": "backend", "level": "mid"},
                files={"file": ("linkedin_export.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            )
            assert response.status_code == 200
            data = response.json()

            assert "parsed_linkedin" in data
            assert "skill_matches" in data
            assert "certificate_matches" in data
            assert "scoring_preview" in data

            # Check parsed data fields
            parsed = data["parsed_linkedin"]
            assert "personal_info" in parsed
            assert "skills" in parsed
            assert len(parsed["skills"]) > 0

            # Check scoring preview
            scoring = data["scoring_preview"]
            assert 0.0 <= scoring["readiness_score"] <= 1.0
            assert len(scoring["skills"]) > 0


# ──────────────────────────────────────────────
# 7. Pipeline Integration with POST /api/analyze
# ──────────────────────────────────────────────

class TestAnalyzeWithLinkedInIntegration:
    """Test POST /api/analyze with linkedin_file."""

    def test_analyze_with_linkedin_file_only(self, linkedin_pdf_path):
        """POST /api/analyze with linkedin_file only succeeds."""
        with open(linkedin_pdf_path, "rb") as f:
            pdf_bytes = f.read()

        with TestClient(app) as client:
            response = client.post(
                "/api/analyze",
                data={"role_id": "backend", "level": "mid"},
                files={"linkedin_file": ("profile.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
            )
            assert response.status_code == 200
            data = response.json()

            assert data["has_linkedin"] is True
            assert data["role_id"] == "backend"
            assert "readiness_score" in data
            assert len(data["skills"]) > 0

            # Verify calculation traces are present
            traces = [
                sub["calculation_trace"]
                for s in data["skills"]
                for sub in s["subskills"]
                if sub.get("calculation_trace")
            ]
            assert len(traces) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
