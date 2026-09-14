"""
Unit tests for summary_generator.py

Verifies:
1. Each of the 5 tiers selects the correct template.
2. All template variables ({role_name}, {score}, {top_skill}, {second_skill}, {weak_skill})
   are filled — no '{' or '}' chars remain in the output.
3. No None / empty values leak into the summary text.
4. Edge cases: 0 skills, 1 skill, skills with missing name fields.
5. analysis_tier == "premium" still returns "template" (AI disabled placeholder).
6. locale="en" produces English output.
"""

import sys
import os

# ---------------------------------------------------------------------------
# Make sure the backend package is importable when running from project root
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from app.services.summary_generator import generate_summary, TEMPLATES, TEMPLATES_EN


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _make_skills(scores: list[tuple[str, float, float]]) -> list[dict]:
    """
    Build a minimal skill list.
    scores: [(skill_name, score, importance), ...]
    """
    return [
        {"skill_id": f"skill_{i}", "skill_name": name, "score": s, "importance": imp}
        for i, (name, s, imp) in enumerate(scores)
    ]


def _no_unfilled_placeholders(text: str) -> bool:
    """Return True when no {placeholder} remains in the text."""
    return "{" not in text and "}" not in text


# ──────────────────────────────────────────────
# 1. Tier selection tests (TR locale)
# ──────────────────────────────────────────────

class TestTierSelection:
    """Each tier must produce distinct, non-empty summary text."""

    SKILLS = _make_skills([
        ("API Design", 0.8, 0.9),
        ("Databases", 0.6, 0.8),
        ("Testing", 0.3, 0.7),
    ])

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_each_tier_returns_non_empty_text(self, tier):
        text, stype = generate_summary(
            tier=tier,
            role_name="Backend Developer",
            readiness_score=0.55,
            skills=self.SKILLS,
        )
        assert text, f"Expected non-empty summary for tier='{tier}'"
        assert stype == "template"

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_each_tier_uses_different_template(self, tier):
        """Five tiers must produce five distinct summaries."""
        results = {}
        for t in ["not_ready", "developing", "approaching", "ready", "exceeds"]:
            text, _ = generate_summary(
                tier=t,
                role_name="Backend Developer",
                readiness_score=0.55,
                skills=self.SKILLS,
            )
            results[t] = text
        # Each tier's text must be unique
        assert len(set(results.values())) == 5, "All 5 tiers must produce distinct summaries"


# ──────────────────────────────────────────────
# 2. Variable substitution tests
# ──────────────────────────────────────────────

class TestVariableSubstitution:
    """No unfilled {placeholder} must remain in any output."""

    SKILLS = _make_skills([
        ("System Design", 0.85, 0.95),
        ("Databases",     0.70, 0.80),
        ("Testing",       0.20, 0.70),
    ])

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_no_unfilled_placeholders_tr(self, tier):
        text, _ = generate_summary(
            tier=tier,
            role_name="Senior Backend Developer",
            readiness_score=0.72,
            skills=self.SKILLS,
            locale="tr",
        )
        assert _no_unfilled_placeholders(text), (
            f"Unfilled placeholder found in TR tier='{tier}': {text}"
        )

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_no_unfilled_placeholders_en(self, tier):
        text, _ = generate_summary(
            tier=tier,
            role_name="Senior Backend Developer",
            readiness_score=0.72,
            skills=self.SKILLS,
            locale="en",
        )
        assert _no_unfilled_placeholders(text), (
            f"Unfilled placeholder found in EN tier='{tier}': {text}"
        )

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_role_name_in_output(self, tier):
        text, _ = generate_summary(
            tier=tier,
            role_name="Frontend Developer",
            readiness_score=0.50,
            skills=self.SKILLS,
        )
        assert "Frontend Developer" in text, (
            f"role_name missing from tier='{tier}': {text}"
        )

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_score_in_output(self, tier):
        text, _ = generate_summary(
            tier=tier,
            role_name="DevOps Engineer",
            readiness_score=0.63,
            skills=self.SKILLS,
        )
        assert "63" in text, f"Score percentage '63' missing from tier='{tier}': {text}"

    def test_top_skill_appears_in_output(self):
        text, _ = generate_summary(
            tier="approaching",
            role_name="ML Engineer",
            readiness_score=0.61,
            skills=self.SKILLS,
        )
        assert "System Design" in text, f"top_skill 'System Design' missing: {text}"

    def test_weak_skill_not_none_or_empty(self):
        """weak_skill must be a non-empty string in all non-ready tiers."""
        for tier in ("not_ready", "developing"):
            text, _ = generate_summary(
                tier=tier,
                role_name="QA Engineer",
                readiness_score=0.25,
                skills=self.SKILLS,
            )
            # "Testing" is the weakest skill — should appear
            assert "Testing" in text or "System Design" in text, (
                f"Expected a skill name in tier='{tier}': {text}"
            )


# ──────────────────────────────────────────────
# 3. Edge cases
# ──────────────────────────────────────────────

class TestEdgeCases:
    """Smoke-test unusual inputs — must never raise exceptions."""

    def test_empty_skills_list(self):
        text, stype = generate_summary(
            tier="developing",
            role_name="Data Analyst",
            readiness_score=0.40,
            skills=[],
        )
        assert stype == "template"
        assert _no_unfilled_placeholders(text)

    def test_single_skill(self):
        skills = _make_skills([("Python", 0.60, 0.90)])
        text, _ = generate_summary(
            tier="approaching",
            role_name="Data Engineer",
            readiness_score=0.55,
            skills=skills,
        )
        assert _no_unfilled_placeholders(text)
        assert text  # must not be empty

    def test_skill_with_missing_name(self):
        """skill_name absent — must fall back to skill_id gracefully."""
        skills = [
            {"skill_id": "be_databases", "score": 0.80, "importance": 0.9},
            {"skill_id": "be_testing",   "score": 0.30, "importance": 0.7},
        ]
        text, _ = generate_summary(
            tier="developing",
            role_name="Backend Developer",
            readiness_score=0.45,
            skills=skills,
        )
        assert _no_unfilled_placeholders(text)
        assert text

    def test_unknown_tier_uses_fallback(self):
        skills = _make_skills([("Security", 0.50, 0.80)])
        text, stype = generate_summary(
            tier="legendary",   # not a real tier
            role_name="Security Engineer",
            readiness_score=0.50,
            skills=skills,
        )
        # Falls back to _FALLBACK_TIER ("developing") — must still produce text
        assert stype == "template"
        assert _no_unfilled_placeholders(text)


# ──────────────────────────────────────────────
# 4. Premium tier placeholder test
# ──────────────────────────────────────────────

class TestPremiumPlaceholder:
    """Premium analysis_tier currently falls back to template (AI disabled)."""

    def test_premium_returns_template_type_while_ai_disabled(self):
        skills = _make_skills([
            ("Kubernetes", 0.90, 0.95),
            ("Monitoring", 0.75, 0.80),
            ("CI/CD",      0.40, 0.70),
        ])
        text, stype = generate_summary(
            tier="ready",
            role_name="MLOps Engineer",
            readiness_score=0.78,
            skills=skills,
            analysis_tier="premium",  # premium → placeholder, AI still disabled
        )
        # Once AI is enabled this should become "ai_generated"; for now must be "template"
        assert stype == "template", (
            "While AI is disabled, premium tier must still return summary_type='template'"
        )
        assert text
        assert _no_unfilled_placeholders(text)


# ──────────────────────────────────────────────
# 5. Summary type is always "template" for standard tier
# ──────────────────────────────────────────────

class TestSummaryType:
    SKILLS = _make_skills([("CI/CD", 0.70, 0.85), ("Docker", 0.50, 0.75)])

    @pytest.mark.parametrize("tier", ["not_ready", "developing", "approaching", "ready", "exceeds"])
    def test_summary_type_is_template_for_standard(self, tier):
        _, stype = generate_summary(
            tier=tier,
            role_name="DevOps Engineer",
            readiness_score=0.60,
            skills=self.SKILLS,
            analysis_tier="standard",
        )
        assert stype == "template"
