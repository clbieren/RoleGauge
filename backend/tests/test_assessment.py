"""
Comprehensive Test Suite for Real Assessment Module.
Tests AssessmentSelector, AssessmentEvaluator, and API endpoints (start & submit).
Verifies:
1. Question selection prioritization based on assessment.json trigger conditions.
2. Dynamic rule-based keyword evaluation (correct, partial, incorrect/verified_gap).
3. Public question safety: expected_answer_keywords strictly omitted from responses.
4. Correct answer increases subskill confidence and overall role readiness score.
5. Assessment override proof: Incorrect answer hard-resets confidence to 0.00 (verified_gap)
   even when strong prior GitHub evidence (0.70) exists.
"""

import io
import os
import sys
from unittest.mock import AsyncMock, patch

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

import pytest
from fastapi.testclient import TestClient

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.main import app
from app.services.assessment_evaluator import AssessmentEvaluator
from app.services.assessment_selector import AssessmentSelector
from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.evidence_engine import EvidenceEngine
from app.services.kb_loader import KnowledgeBase, kb
from app.services.scoring_engine import ScoringEngine


@pytest.fixture(scope="module", autouse=True)
def init_kb():
    """Ensure Knowledge Base is loaded."""
    kb.load()
    return kb


# ──────────────────────────────────────────────
# 1. Assessment Selector Unit Tests
# ──────────────────────────────────────────────

class TestAssessmentSelector:
    """Test question selection and prioritization rules."""

    def test_selector_prioritizes_not_yet_evidenced_expected_subskills(self, init_kb):
        """Expected subskills with confidence=0.0 must have higher priority than evidenced ones."""
        selector = AssessmentSelector(init_kb)
        subskills_evidence = {
            "be_databases.relational_modeling": {"confidence": 0.0, "status": "not_yet_evidenced"},
            "be_databases.sql_querying": {"confidence": 0.90, "status": "evidence_found"},
        }

        selected = selector.select_questions(
            role_id="backend",
            level="mid",
            subskills_evidence=subskills_evidence,
            max_questions=10,
        )

        assert len(selected) > 0
        # Check that relational_modeling is ranked before sql_querying
        keys = [q.composite_key for q in selected]
        assert "be_databases.relational_modeling" in keys
        rel_idx = keys.index("be_databases.relational_modeling")
        if "be_databases.sql_querying" in keys:
            sql_idx = keys.index("be_databases.sql_querying")
            assert rel_idx < sql_idx

    def test_selector_prioritizes_voluntary_requests(self, init_kb):
        """Voluntary composite keys must receive top priority."""
        selector = AssessmentSelector(init_kb)
        voluntary_key = "be_databases.indexing_optimization"

        selected = selector.select_questions(
            role_id="backend",
            level="mid",
            subskills_evidence={},
            voluntary_composite_keys=[voluntary_key],
            max_questions=5,
        )

        assert len(selected) > 0
        assert selected[0].composite_key == voluntary_key
        assert selected[0].priority_score >= 100.0

    def test_selector_omits_keywords_in_public_dict(self, init_kb):
        """SelectedQuestion.to_public_dict() must strictly omit expected_answer_keywords."""
        selector = AssessmentSelector(init_kb)
        selected = selector.select_questions(role_id="backend", level="mid", max_questions=3)

        assert len(selected) > 0
        for q in selected:
            pub = q.to_public_dict()
            assert "expected_answer_keywords" not in pub
            assert "question" in pub
            assert "composite_key" in pub
            assert "type" in pub

    def test_selector_caps_max_questions(self, init_kb):
        """Max questions limit must be respected."""
        selector = AssessmentSelector(init_kb)
        selected = selector.select_questions(role_id="backend", level="mid", max_questions=4)
        assert len(selected) <= 4


# ──────────────────────────────────────────────
# 2. Assessment Evaluator Unit Tests
# ──────────────────────────────────────────────

class TestAssessmentEvaluator:
    """Test rule-based keyword matching and threshold decisions from engine.json."""

    def test_evaluator_correct_answer(self, init_kb):
        """Matching >= 60% keywords yields correct verdict and evidence_found status."""
        evaluator = AssessmentEvaluator(init_kb)
        question_data = {
            "question": "Explain N+1 query problem and how to resolve it.",
            "type": "scenario",
            "expected_answer_keywords": [
                "N+1 query problem",
                "lazy loading default",
                "eager loading",
                "JOIN FETCH",
                "batch loading",
            ],
        }
        # Provide an answer matching 4 of 5 keywords (80% >= 60%)
        candidate_answer = (
            "The N+1 query problem occurs due to lazy loading default behavior. "
            "To fix it, use eager loading with JOIN FETCH or batch loading."
        )

        res = evaluator.evaluate_answer("be_databases.orm_data_mappers", candidate_answer, question_data)

        assert res.verdict == "correct"
        assert res.status == "evidence_found"
        assert res.score == 1.0
        assert res.strength == pytest.approx(0.8)  # scenario correct weight from engine.json
        assert res.match_ratio >= 0.60
        assert len(res.matched_keywords) >= 4

    def test_evaluator_partial_answer(self, init_kb):
        """Matching 30%-59% keywords yields partial verdict and partial_answer status."""
        evaluator = AssessmentEvaluator(init_kb)
        question_data = {
            "question": "Explain N+1 query problem and how to resolve it.",
            "type": "scenario",
            "expected_answer_keywords": [
                "N+1 query problem",
                "lazy loading default",
                "eager loading",
                "JOIN FETCH",
                "batch loading",
            ],
        }
        # Provide an answer matching 2 of 5 keywords (40% in [30%, 60%))
        candidate_answer = "This happens when there is an N+1 query problem, solved by eager loading."

        res = evaluator.evaluate_answer("be_databases.orm_data_mappers", candidate_answer, question_data)

        assert res.verdict == "partial"
        assert res.status == "partial_answer"
        assert res.score == 0.5
        assert res.strength == pytest.approx(0.4)  # scenario partial weight from engine.json
        assert 0.30 <= res.match_ratio < 0.60

    def test_evaluator_incorrect_answer_verified_gap(self, init_kb):
        """Matching < 30% keywords yields incorrect verdict and verified_gap status."""
        evaluator = AssessmentEvaluator(init_kb)
        question_data = {
            "question": "Explain N+1 query problem and how to resolve it.",
            "type": "scenario",
            "expected_answer_keywords": [
                "N+1 query problem",
                "lazy loading default",
                "eager loading",
                "JOIN FETCH",
                "batch loading",
            ],
        }
        # Provide an irrelevant/incorrect answer matching 0 keywords (0% < 30%)
        candidate_answer = "You just add an index on the primary key and restart the server."

        res = evaluator.evaluate_answer("be_databases.orm_data_mappers", candidate_answer, question_data)

        assert res.verdict == "incorrect"
        assert res.status == "verified_gap"
        assert res.score == 0.0
        assert res.strength == 0.0
        assert res.match_ratio < 0.30

    def test_evaluator_empty_answer(self, init_kb):
        """Empty answer automatically receives verified_gap and 0.0 score."""
        evaluator = AssessmentEvaluator(init_kb)
        question_data = {
            "question": "Explain ACID properties.",
            "type": "conceptual",
            "expected_answer_keywords": ["atomicity", "consistency", "isolation", "durability"],
        }

        res = evaluator.evaluate_answer("be_databases.transactions_acid", "", question_data)
        assert res.verdict == "incorrect"
        assert res.status == "verified_gap"
        assert res.score == 0.0


# ──────────────────────────────────────────────
# 3. Router Integration & End-to-End Tests
# ──────────────────────────────────────────────

class TestAssessmentRouterIntegration:
    """Test POST /api/assessment/start and POST /api/assessment/submit workflows."""

    def test_assessment_start_and_submit_correct_flow(self):
        """
        Flow:
        1. Start assessment for role='backend', level='junior'
        2. Submit correct answer for the first question
        3. Verify updated analysis has evidence_found and score increase
        """
        with TestClient(app) as client:
            # 1. Start assessment with a voluntary composite key
            target_key = "be_databases.sql_querying"
            start_resp = client.post(
                "/api/assessment/start",
                json={
                    "github_username": "candidate_test_1",
                    "role_id": "backend",
                    "level": "junior",
                    "voluntary_composite_keys": [target_key],
                    "max_questions": 3,
                },
            )
            assert start_resp.status_code == 200
            start_data = start_resp.json()
            session_id = start_data["assessment_session_id"]
            questions = start_data["questions"]

            assert len(questions) > 0
            first_q = questions[0]
            assert first_q["composite_key"] == target_key
            assert "expected_answer_keywords" not in first_q

            # 2. Submit high-quality answer matching expected keywords for sql_querying
            submit_resp = client.post(
                "/api/assessment/submit",
                json={
                    "assessment_session_id": session_id,
                    "answers": {
                        target_key: (
                            "We use DENSE_RANK() and ROW_NUMBER() with PARTITION BY and an OVER clause "
                            "inside a Common Table Expression (CTE) and filter WHERE rank <= 3."
                        )
                    },
                },
            )
            assert submit_resp.status_code == 200
            submit_data = submit_resp.json()

            assert submit_data["assessment_session_id"] == session_id
            evals = submit_data["evaluations"]
            assert len(evals) > 0
            target_eval = next((e for e in evals if e["composite_key"] == target_key), None)
            assert target_eval is not None
            assert target_eval["verdict"] == "correct"
            assert target_eval["status"] == "evidence_found"

            updated_analysis = submit_data["updated_analysis"]
            assert updated_analysis["readiness_score"] > 0.0

    def test_assessment_override_replaces_strong_github_evidence(self):
        """
        CRITICAL OVERRIDE TEST:
        1. Subskill starts with strong GitHub evidence (confidence = 0.70).
        2. Candidate answers question INCORRECTLY in assessment.
        3. Subskill confidence is HARD SET to 0.00 (verified_gap), overriding GitHub evidence.
        """
        test_key = "be_databases.relational_modeling"

        # Initialize EvidenceEngine with simulated strong GitHub evidence
        engine = EvidenceEngine(kb, "backend", "junior")
        github_signals = {
            test_key: SubskillEvidenceResult(
                composite_key=test_key,
                subskill_name="Relational Modeling",
                status="evidence_found",
                signals=[
                    EvidenceSignal(
                        source="file_presence",
                        file_path="src/models/order.py",
                        matched_text="Order and OrderItem relational schema",
                        strength=0.70,
                    )
                ],
            )
        }

        # Step A: Pre-assessment state
        unified_pre = engine.merge_evidence(github_evidence=github_signals)
        assert unified_pre[test_key].final_confidence == 0.70
        assert unified_pre[test_key].final_status == "evidence_found"

        # Step B: Candidate answers incorrectly in assessment
        failed_assessment_signals = {
            test_key: [
                {
                    "status": "verified_gap",
                    "score": 0.0,
                    "strength": 0.0,
                    "detail": "Incorrect answer: 0/6 keywords matched. Candidate failed relational modeling challenge.",
                }
            ]
        }

        # Step C: Multi-source merge with Assessment override
        unified_post = engine.merge_evidence(
            github_evidence=github_signals,
            assessment_evidence=failed_assessment_signals,
        )

        # Assertions proving Assessment is the final arbiter of truth
        res_post = unified_post[test_key]
        assert res_post.final_confidence == 0.00, "Confidence must be hard reset to 0.00 on assessment failure"
        assert res_post.final_status == "verified_gap", "Status must be verified_gap"
        assert "assessment_override_verified_gap" in res_post.ceiling_applied
        assert "assessment_override: verified_gap" in res_post.calculation_trace

        # Step D: ScoringEngine verifies denominator isolation and penalty
        scoring_engine = ScoringEngine(kb, "backend", "junior")
        scoring_pre = scoring_engine.calculate_all({k: v.to_subskill_evidence_result() for k, v in unified_pre.items()})
        scoring_post = scoring_engine.calculate_all({k: v.to_subskill_evidence_result() for k, v in unified_post.items()})

        assert scoring_post["readiness_score"] < scoring_pre["readiness_score"]


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
