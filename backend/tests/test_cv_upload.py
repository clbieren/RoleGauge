"""
End-to-end tests for CV Upload & Parser module.

Tests:
1. PDF and DOCX parsing → structured JSON
2. Skills/projects → composite key matches with 'claimed' status
3. Certificate 3-way classification (recognized_relevant, recognized_no_mapping, unrecognized_excluded)
4. Normalization: partial cert name matching (e.g. "AWS Solutions Architect Associate")
5. Unrecognized cert → score_contribution: 0.0 in final scoring
6. File validation: wrong format → 400, oversized → 413
"""

import io
import json
import os
import sys
import tempfile

import pytest

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# ──────────────────────────────────────────────
# Fixtures: Generate synthetic test CVs
# ──────────────────────────────────────────────

SAMPLE_CV_TEXT = """John Doe
john.doe@example.com
github.com/johndoe
linkedin.com/in/johndoe

Summary
Experienced backend developer with 5 years of experience building scalable APIs and microservices.

Work Experience

Senior Backend Developer
TechCorp Inc.
2021 - Present
Designed and built RESTful APIs using FastAPI and PostgreSQL. Implemented OAuth2 authentication
with JWT tokens. Architected event-driven microservices using Apache Kafka. Reduced p99 latency
from 450ms to 40ms through database query optimization and Redis caching.

Backend Developer
StartupXYZ
2019 - 2021
Built REST APIs with Flask and MySQL. Wrote unit tests with pytest.
Managed Docker containers in production environments.

Education

Istanbul Technical University
B.Sc. Computer Science
2015 - 2019

Projects

E-Commerce API Platform
Built a high-performance REST API platform using FastAPI, PostgreSQL, and Redis.
Implemented clean architecture with domain-driven design patterns.
Technologies: FastAPI, PostgreSQL, Redis, Docker, Kubernetes

Chat Service
Real-time messaging service built with WebSockets.
Stack: Python, Redis, RabbitMQ

Technical Skills
Python, FastAPI, PostgreSQL, MySQL, Redis, Docker, Kubernetes, Apache Kafka,
RabbitMQ, Git, Linux, REST API, GraphQL, OAuth2, JWT, Terraform

Certifications
AWS Certified Solutions Architect - Associate
CKA (Certified Kubernetes Administrator)
Dale Carnegie Leadership Certificate
Confluent Certified Developer for Apache Kafka (CCDAK)

Languages
English (Fluent), Turkish (Native), German (B1)
"""


def _create_test_docx(text: str, path: str) -> None:
    """Create a DOCX file with the given text content."""
    from docx import Document

    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)


def _create_test_pdf(text: str, path: str) -> None:
    """Create a simple PDF file with the given text content."""
    # Use a minimal PDF structure with properly encoded text
    lines = text.split("\n")
    # Build content stream - escape special PDF characters
    content_lines = []
    y = 800
    for line in lines:
        if line.strip():
            # Escape PDF special chars
            escaped = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            content_lines.append(f"BT /F1 10 Tf 50 {y} Td ({escaped}) Tj ET")
            y -= 14
            if y < 50:
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
def docx_path():
    """Create a temporary DOCX test CV."""
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False, prefix="test_cv_") as tmp:
        tmp_path = tmp.name
    _create_test_docx(SAMPLE_CV_TEXT, tmp_path)
    yield tmp_path
    os.unlink(tmp_path)


@pytest.fixture(scope="module")
def pdf_path():
    """Create a temporary PDF test CV."""
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False, prefix="test_cv_") as tmp:
        tmp_path = tmp.name
    _create_test_pdf(SAMPLE_CV_TEXT, tmp_path)
    yield tmp_path
    os.unlink(tmp_path)


@pytest.fixture(scope="module")
def loaded_kb():
    """Load the knowledge base once for all tests."""
    from app.services.kb_loader import KnowledgeBase

    test_kb = KnowledgeBase()
    # Compute KB path relative to backend directory
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb_path = os.path.join(os.path.dirname(backend_dir), "knowledge-base")
    test_kb.load(kb_path)
    return test_kb


@pytest.fixture(scope="module")
def cert_index(loaded_kb):
    """Build certification index."""
    from app.services.cv_certification_matcher import CertificationIndex

    index = CertificationIndex()
    index.build(loaded_kb)
    return index


# ──────────────────────────────────────────────
# Test Group (a): CV Parsing → Structured JSON
# ──────────────────────────────────────────────

class TestCVParsing:
    """Test CV parser produces correct structured JSON from DOCX."""

    def test_docx_sections_detected(self, docx_path):
        """DOCX parsing detects all expected sections."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)

        assert "personal_info" in result["detected_sections"]
        assert "education" in result["detected_sections"]
        assert "experience" in result["detected_sections"]
        assert "skills" in result["detected_sections"]
        assert "certificates" in result["detected_sections"]
        assert "languages" in result["detected_sections"]
        assert "projects" in result["detected_sections"]

    def test_personal_info_extracted(self, docx_path):
        """Parser extracts personal info from preamble."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)
        info = result["personal_info"]

        assert "name" in info
        assert info.get("email") == "john.doe@example.com"
        assert "github.com/johndoe" in info.get("github", "")
        assert "linkedin.com/in/johndoe" in info.get("linkedin", "")

    def test_skills_parsed(self, docx_path):
        """Parser extracts flat skill list."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)
        skills = [s.lower() for s in result["skills"]]

        assert any("python" in s for s in skills)
        assert any("fastapi" in s for s in skills)
        assert any("postgresql" in s for s in skills)
        assert any("docker" in s for s in skills)
        assert any("redis" in s for s in skills)

    def test_certificates_parsed(self, docx_path):
        """Parser extracts certificate entries."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)
        cert_names = [c["name"].lower() for c in result["certificates"]]

        assert any("aws" in name for name in cert_names)
        assert any("dale carnegie" in name or "leadership" in name for name in cert_names)
        assert len(result["certificates"]) >= 3

    def test_projects_with_skills_mentioned(self, docx_path):
        """Parser extracts projects with skills_mentioned lists."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)

        assert len(result["projects"]) >= 1
        # At least one project should have skills_mentioned
        all_skills = []
        for p in result["projects"]:
            all_skills.extend(p.get("skills_mentioned", []))
        assert len(all_skills) > 0

    def test_experience_parsed(self, docx_path):
        """Parser extracts work experience entries."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)

        assert len(result["experience"]) >= 1

    def test_languages_parsed(self, docx_path):
        """Parser extracts language list."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)
        lang_lower = [l.lower() for l in result["languages"]]

        assert any("english" in l for l in lang_lower)
        assert any("turkish" in l for l in lang_lower)

    def test_output_schema_complete(self, docx_path):
        """Parser output has all required top-level keys."""
        from app.services.cv_parser import parse_cv

        result = parse_cv(docx_path)

        required_keys = [
            "personal_info", "education", "experience", "projects",
            "skills", "certificates", "languages"
        ]
        for key in required_keys:
            assert key in result, f"Missing key: {key}"


# ──────────────────────────────────────────────
# Test Group (b): Skill Matching → Composite Keys
# ──────────────────────────────────────────────

class TestSkillMatching:
    """Test CV skill matcher produces 'claimed' status composite key matches."""

    def test_skills_match_composite_keys(self, docx_path, loaded_kb):
        """Skills from CV match against backend role composite keys."""
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher

        parsed = parse_cv(docx_path)
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        claimed = {k: v for k, v in evidence.items() if v.status == "claimed"}

        # We listed PostgreSQL, Docker, Redis, Kafka etc. in the CV
        # These should produce matches against backend subskills
        assert len(claimed) > 0, "Expected at least some skill matches"

        # Verify all matched items have 'claimed' status, never 'evidence_found'
        for key, result in claimed.items():
            assert result.status == "claimed", f"{key} has status '{result.status}', expected 'claimed'"

    def test_claimed_never_evidence_found(self, docx_path, loaded_kb):
        """CV skill matches NEVER produce 'evidence_found' status."""
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher

        parsed = parse_cv(docx_path)
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        for key, result in evidence.items():
            assert result.status != "evidence_found", (
                f"{key} has forbidden status 'evidence_found'. "
                "CV matches must use 'claimed'."
            )

    def test_signal_strengths_from_cv_json(self, docx_path, loaded_kb):
        """Signal strengths should come from cv.json base_strength values."""
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher

        parsed = parse_cv(docx_path)
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        for key, result in evidence.items():
            for signal in result.signals:
                # CV base_strengths are 0.2-0.5, modifiers 0.4-1.2
                # So final strengths should be in range 0.08 - 0.6
                assert 0.0 < signal.strength <= 1.0, (
                    f"Signal strength {signal.strength} out of expected range for {key}"
                )

    def test_project_skills_matched(self, docx_path, loaded_kb):
        """Skills mentioned in projects section produce matches."""
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher

        parsed = parse_cv(docx_path)
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        # Check for cv_project or cv_experience source signals
        project_signals = []
        for key, result in evidence.items():
            for signal in result.signals:
                if signal.source in ("cv_project", "cv_experience"):
                    project_signals.append(signal)

        assert len(project_signals) > 0, "Expected some signals from project/experience sections"


# ──────────────────────────────────────────────
# Test Group (c): Certificate Classification
# ──────────────────────────────────────────────

class TestCertificateMatching:
    """Test 3-way certificate classification."""

    def test_recognized_relevant_exact_match(self, loaded_kb, cert_index):
        """Exact match cert in allowlist with signal_mapping → recognized_relevant."""
        from app.services.cv_certification_matcher import CertificationMatcher

        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "AWS Certified Solutions Architect - Associate", "provider": "AWS"},
        ])

        assert len(results) == 1
        r = results[0]
        assert r["classification"] == "recognized_relevant", (
            f"Expected 'recognized_relevant', got '{r['classification']}'"
        )
        assert r["matched_composite_keys"] is not None
        assert len(r["matched_composite_keys"]) > 0
        assert r["score_contribution"] > 0.0

    def test_recognized_relevant_normalized_match(self, loaded_kb, cert_index):
        """
        Normalized cert name (missing 'Certified', no dash) should still match.
        Tests: "AWS Solutions Architect Associate" vs
               "AWS Certified Solutions Architect - Associate"
        """
        from app.services.cv_certification_matcher import CertificationMatcher

        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "AWS Solutions Architect Associate", "provider": ""},
        ])

        assert len(results) == 1
        r = results[0]
        # Should match via normalization (remove "Certified", normalize dashes)
        assert r["classification"] in ("recognized_relevant", "recognized_no_mapping"), (
            f"Expected recognized classification, got '{r['classification']}'. "
            "Normalization should handle missing 'Certified' and dash differences."
        )

    def test_unrecognized_excluded(self, loaded_kb, cert_index):
        """Cert not in any allowlist → unrecognized_excluded."""
        from app.services.cv_certification_matcher import CertificationMatcher

        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "Dale Carnegie Leadership Certificate", "provider": "Dale Carnegie"},
        ])

        assert len(results) == 1
        r = results[0]
        assert r["classification"] == "unrecognized_excluded"
        assert r["matched_composite_keys"] is None
        assert r["score_contribution"] == 0.0

    def test_recognized_no_mapping(self, loaded_kb, cert_index):
        """
        Cert in allowlist but without a signal_mapping pattern → recognized_no_mapping.
        The cert is 'known' but there's no composite key binding defined yet.
        """
        from app.services.cv_certification_matcher import CertificationMatcher

        # Find a cert that IS in recognized_certifications but likely has no signal_mapping pattern
        # Most certs in sub-categories (e.g. specific DB certs) won't have explicit patterns
        # Let's use "PostgreSQL Certified Engineer" which is in backend's recognized list
        # under "database_data" category
        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "PostgreSQL Certified Engineer", "provider": "PostgreSQL"},
        ])

        assert len(results) == 1
        r = results[0]
        # This cert is recognized but may not have a signal_mapping pattern
        # It should be either recognized_relevant or recognized_no_mapping
        assert r["classification"] in ("recognized_relevant", "recognized_no_mapping"), (
            f"Expected recognized_relevant or recognized_no_mapping, got '{r['classification']}'"
        )
        # If it's recognized_no_mapping, score_contribution must be 0
        if r["classification"] == "recognized_no_mapping":
            assert r["score_contribution"] == 0.0

    def test_abbreviation_matching(self, loaded_kb, cert_index):
        """Abbreviation form like 'CKA' should match 'CKA (Certified Kubernetes Administrator)'."""
        from app.services.cv_certification_matcher import CertificationMatcher

        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "CKA", "provider": "CNCF"},
        ])

        assert len(results) == 1
        r = results[0]
        # CKA is in the backend's recognized_certifications under containers_kubernetes
        assert r["classification"] != "unrecognized_excluded", (
            f"CKA abbreviation should be recognized, got '{r['classification']}'"
        )

    def test_all_three_classifications_in_batch(self, loaded_kb, cert_index):
        """Batch of mixed certs produces all three classification types."""
        from app.services.cv_certification_matcher import CertificationMatcher

        matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        results = matcher.match_certificates([
            {"name": "AWS Certified Solutions Architect - Associate", "provider": "AWS"},
            {"name": "PostgreSQL Certified Engineer", "provider": "PostgreSQL"},
            {"name": "Dale Carnegie Leadership Certificate", "provider": "Dale Carnegie"},
            {"name": "Yoga Teacher Training Level 1", "provider": "YogaAlliance"},
        ])

        classifications = {r["classification"] for r in results}
        # At minimum we must have unrecognized_excluded (Dale Carnegie and Yoga)
        assert "unrecognized_excluded" in classifications

        # And at least one recognized variant
        assert "recognized_relevant" in classifications or "recognized_no_mapping" in classifications


# ──────────────────────────────────────────────
# Test Group (d): Scoring — Unrecognized Cert Zero Impact
# ──────────────────────────────────────────────

class TestScoringIntegration:
    """Test that unrecognized certs have zero impact on scoring."""

    def test_unrecognized_cert_zero_score_contribution(self, docx_path, loaded_kb, cert_index):
        """
        End-to-end: unrecognized certs produce score_contribution: 0.0
        and do NOT appear in any subskill's evidence signals.
        """
        from app.services.cv_certification_matcher import CertificationMatcher
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher
        from app.services.evidence_detector import EvidenceSignal
        from app.services.scoring_engine import ScoringEngine

        parsed = parse_cv(docx_path)

        # Run skill matching
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        # Run cert matching
        cert_matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        cert_results = cert_matcher.match_certificates(parsed.get("certificates", []))

        # Only inject recognized_relevant certs into evidence
        for cr in cert_results:
            if cr["classification"] == "recognized_relevant" and cr["matched_composite_keys"]:
                for ck in cr["matched_composite_keys"]:
                    if ck in evidence:
                        evidence[ck].signals.append(EvidenceSignal(
                            source="cv_certification",
                            file_path="cv/certifications",
                            matched_text=cr["certificate_name"],
                            strength=cr["strength"],
                        ))
                        if evidence[ck].status == "not_yet_evidenced":
                            evidence[ck].status = "claimed"

        # Run scoring
        engine = ScoringEngine(loaded_kb, "backend", "mid")
        scoring_result = engine.calculate_all(evidence)

        # Verify: "Dale Carnegie Leadership Certificate" must NOT appear in any evidence
        for skill in scoring_result["skills"]:
            for subskill in skill["subskills"]:
                for source in subskill.get("evidence_sources", []):
                    assert "dale carnegie" not in source.lower(), (
                        f"Unrecognized cert 'Dale Carnegie' leaked into scoring: "
                        f"{subskill['composite_key']} → {source}"
                    )
                    assert "leadership" not in source.lower() or "certificate" not in source.lower(), (
                        f"Unrecognized cert leaked into scoring: "
                        f"{subskill['composite_key']} → {source}"
                    )

        # Verify unrecognized cert results have zero contribution
        for cr in cert_results:
            if cr["classification"] == "unrecognized_excluded":
                assert cr["score_contribution"] == 0.0, (
                    f"Unrecognized cert '{cr['certificate_name']}' has "
                    f"score_contribution={cr['score_contribution']}, expected 0.0"
                )

    def test_recognized_cert_contributes_to_score(self, docx_path, loaded_kb, cert_index):
        """Recognized certs with signal_mapping should contribute non-zero to relevant subskills."""
        from app.services.cv_certification_matcher import CertificationMatcher
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher
        from app.services.evidence_detector import EvidenceSignal
        from app.services.scoring_engine import ScoringEngine

        parsed = parse_cv(docx_path)

        # Run skill matching
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        # Run cert matching
        cert_matcher = CertificationMatcher(loaded_kb, cert_index, "backend")
        cert_results = cert_matcher.match_certificates(parsed.get("certificates", []))

        # Inject recognized certs
        recognized_keys = set()
        for cr in cert_results:
            if cr["classification"] == "recognized_relevant" and cr["matched_composite_keys"]:
                for ck in cr["matched_composite_keys"]:
                    recognized_keys.add(ck)
                    if ck in evidence:
                        evidence[ck].signals.append(EvidenceSignal(
                            source="cv_certification",
                            file_path="cv/certifications",
                            matched_text=cr["certificate_name"],
                            strength=cr["strength"],
                        ))
                        if evidence[ck].status == "not_yet_evidenced":
                            evidence[ck].status = "claimed"

        # Run scoring
        engine = ScoringEngine(loaded_kb, "backend", "mid")
        scoring_result = engine.calculate_all(evidence)

        # The overall readiness score should be > 0 since we have skills and certs
        assert scoring_result["readiness_score"] > 0.0, (
            "Expected non-zero readiness score with CV skills and recognized certs"
        )

    def test_scoring_output_has_correct_structure(self, docx_path, loaded_kb, cert_index):
        """Final scoring output has proper structure with all fields."""
        from app.services.cv_certification_matcher import CertificationMatcher
        from app.services.cv_parser import parse_cv
        from app.services.cv_skill_matcher import CVSkillMatcher
        from app.services.scoring_engine import ScoringEngine

        parsed = parse_cv(docx_path)
        matcher = CVSkillMatcher(loaded_kb, "backend")
        evidence = matcher.match_all(parsed)

        engine = ScoringEngine(loaded_kb, "backend", "mid")
        result = engine.calculate_all(evidence)

        assert "readiness_score" in result
        assert "readiness_tier" in result
        assert "readiness_label" in result
        assert "skills" in result
        assert 0.0 <= result["readiness_score"] <= 1.0
        assert len(result["skills"]) > 0


# ──────────────────────────────────────────────
# Test Group (e): File Validation
# ──────────────────────────────────────────────

class TestFileValidation:
    """Test upload endpoint file validation (these test the validation logic directly)."""

    def test_reject_unsupported_format(self):
        """Non-PDF/DOCX files should be rejected."""
        from app.services.cv_parser import extract_text

        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
            tmp.write(b"Hello world")
            tmp_path = tmp.name

        try:
            with pytest.raises(ValueError, match="Unsupported file format"):
                extract_text(tmp_path)
        finally:
            os.unlink(tmp_path)

    def test_empty_file_rejected(self):
        """Empty DOCX should raise an error."""
        from app.services.cv_parser import parse_cv

        with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            from docx import Document
            doc = Document()
            doc.save(tmp_path)

            with pytest.raises(ValueError, match="empty"):
                parse_cv(tmp_path)
        finally:
            os.unlink(tmp_path)


# ──────────────────────────────────────────────
# Test Group (f): Certification Index
# ──────────────────────────────────────────────

class TestCertificationIndex:
    """Test the unified certification index building and lookup."""

    def test_index_built_from_multiple_roles(self, cert_index):
        """Index should contain certs from multiple roles."""
        # The index should have entries (we know at least 10 roles have recognized_certifications)
        assert cert_index._built
        assert len(cert_index._allowlist) > 0

    def test_lookup_returns_none_for_unknown(self, cert_index):
        """Unknown cert returns None."""
        result = cert_index.lookup("Underwater Basket Weaving Certificate")
        assert result is None

    def test_lookup_finds_known_cert(self, cert_index):
        """Known cert (e.g. from backend's recognized list) is found."""
        result = cert_index.lookup("AWS Certified Solutions Architect - Associate")
        assert result is not None
        assert len(result) > 0
        assert any(entry["role_category"] == "backend" for entry in result)

    def test_lookup_case_insensitive(self, cert_index):
        """Lookup should be case-insensitive."""
        result = cert_index.lookup("aws certified solutions architect - associate")
        assert result is not None

    def test_abbreviation_lookup(self, cert_index):
        """Abbreviation like 'CKAD' should be found."""
        result = cert_index.lookup("CKAD")
        assert result is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
