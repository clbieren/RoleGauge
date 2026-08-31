"""
Assessment Evaluator Service.
Rule-based keyword-match evaluation for candidate assessment answers.

NOTE: As per system architecture, numeric scoring is strictly deterministic.
Keywords and threshold percentages (correct >= 0.60, partial >= 0.30) are dynamically
loaded from engine.json (Single Source of Truth).

# TODO / Extension Point:
# Future versions may optionally invoke LLM providers (OpenAI/Gemini) to perform
# semantic nuance and code style evaluation, but the final score thresholds will
# remain governed by engine.json rules.
"""

import logging
import re
from dataclasses import dataclass, field
from typing import Any, Optional

from app.services.kb_loader import KnowledgeBase, kb

logger = logging.getLogger(__name__)


@dataclass
class EvaluationResult:
    """Evaluation output for a single question response."""
    composite_key: str
    subskill_name: str
    question: str
    question_type: str
    verdict: str  # correct | partial | incorrect
    status: str  # evidence_found | partial_answer | verified_gap
    score: float  # 1.0 | 0.5 | 0.0
    strength: float  # effective signal strength according to question type
    match_ratio: float
    matched_keywords: list[str] = field(default_factory=list)
    total_keywords: int = 0
    feedback: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "composite_key": self.composite_key,
            "subskill_name": self.subskill_name,
            "question": self.question,
            "type": self.question_type,
            "verdict": self.verdict,
            "status": self.status,
            "score": round(self.score, 4),
            "strength": round(self.strength, 4),
            "match_ratio": round(self.match_ratio, 4),
            "matched_keywords_count": len(self.matched_keywords),
            "total_keywords_count": self.total_keywords,
            "feedback": self.feedback,
        }


class AssessmentEvaluator:
    """
    Evaluates candidate assessment answers using rule-based keyword matching.
    Configuration and thresholds are loaded dynamically from engine.json.
    """

    def __init__(self, knowledge_base: KnowledgeBase | None = None):
        self.kb = knowledge_base or kb

        # Load scoring rules from engine.json
        engine_cfg = self.kb.scoring_engine or {}
        step1_rules = (
            engine_cfg.get("step_1_evidence_to_subskill_confidence", {})
            .get("rules", {})
            .get("assessment_scoring_and_override_rules", {})
        )

        thresholds = step1_rules.get("keyword_match_thresholds", {})
        self.correct_threshold = float(thresholds.get("correct_answer", 0.60))
        self.partial_threshold = float(thresholds.get("partial_answer", 0.30))

        self.correct_weights = {
            "practical_task": float(step1_rules.get("correct_answer", {}).get("practical_task", 1.0)),
            "scenario": float(step1_rules.get("correct_answer", {}).get("scenario", 0.8)),
            "conceptual": float(step1_rules.get("correct_answer", {}).get("conceptual", 0.6)),
        }

        self.partial_weights = {
            "practical_task": float(step1_rules.get("partial_answer", {}).get("practical_task", 0.5)),
            "scenario": float(step1_rules.get("partial_answer", {}).get("scenario", 0.4)),
            "conceptual": float(step1_rules.get("partial_answer", {}).get("conceptual", 0.3)),
        }

        logger.info(
            f"[AssessmentEvaluator] Loaded engine.json thresholds: "
            f"correct_threshold={self.correct_threshold:.2f}, partial_threshold={self.partial_threshold:.2f}, "
            f"correct_weights={self.correct_weights}, partial_weights={self.partial_weights}"
        )

    def evaluate_answer(
        self,
        composite_key: str,
        user_answer: str,
        question_data: dict[str, Any],
    ) -> EvaluationResult:
        """
        Evaluate a single user answer against expected answer keywords.

        Args:
            composite_key: Target subskill composite key
            user_answer: Raw text submitted by candidate
            question_data: Question definition dictionary containing:
                           - question (str)
                           - type (str)
                           - expected_answer_keywords (list[str])
                           - subskill_name (optional str)

        Returns:
            EvaluationResult with verdict, score, strength, and status
        """
        subskill_name = question_data.get("subskill_name", composite_key)
        question_text = question_data.get("question", "")
        q_type = question_data.get("type", "scenario").lower()
        expected_keywords = question_data.get("expected_answer_keywords", [])

        # Clean and normalize candidate answer
        normalized_answer = self._normalize_text(user_answer or "")

        if not normalized_answer.strip() or not expected_keywords:
            if not expected_keywords:
                # No keywords defined in question bank -> fallback default full match
                return EvaluationResult(
                    composite_key=composite_key,
                    subskill_name=subskill_name,
                    question=question_text,
                    question_type=q_type,
                    verdict="correct",
                    status="evidence_found",
                    score=1.0,
                    strength=self.correct_weights.get(q_type, 0.8),
                    match_ratio=1.0,
                    matched_keywords=[],
                    total_keywords=0,
                    feedback="No keywords defined; defaulted to accepted.",
                )
            else:
                # Empty candidate answer
                return EvaluationResult(
                    composite_key=composite_key,
                    subskill_name=subskill_name,
                    question=question_text,
                    question_type=q_type,
                    verdict="incorrect",
                    status="verified_gap",
                    score=0.0,
                    strength=0.0,
                    match_ratio=0.0,
                    matched_keywords=[],
                    total_keywords=len(expected_keywords),
                    feedback="No answer provided. Marked as verified_gap (0.00).",
                )

        # Match keywords
        matched_keywords: list[str] = []
        for kw in expected_keywords:
            if self._keyword_matches(kw, normalized_answer):
                matched_keywords.append(kw)

        total_kw = len(expected_keywords)
        match_ratio = len(matched_keywords) / total_kw if total_kw > 0 else 1.0

        # Apply engine.json scoring rules
        if match_ratio >= self.correct_threshold:
            verdict = "correct"
            status = "evidence_found"
            score = 1.0
            strength = self.correct_weights.get(q_type, 0.8)
            feedback = (
                f"Correct answer: matched {len(matched_keywords)}/{total_kw} keywords "
                f"({match_ratio * 100:.1f}% >= {self.correct_threshold * 100:.0f}%). "
                f"Status: evidence_found (signal strength: {strength:.2f})."
            )
        elif match_ratio >= self.partial_threshold:
            verdict = "partial"
            status = "partial_answer"
            score = 0.5
            strength = self.partial_weights.get(q_type, 0.4)
            feedback = (
                f"Partial answer: matched {len(matched_keywords)}/{total_kw} keywords "
                f"({match_ratio * 100:.1f}% >= {self.partial_threshold * 100:.0f}%). "
                f"Status: partial_answer (signal strength: {strength:.2f})."
            )
        else:
            verdict = "incorrect"
            status = "verified_gap"
            score = 0.0
            strength = 0.0
            feedback = (
                f"Incorrect answer: matched only {len(matched_keywords)}/{total_kw} keywords "
                f"({match_ratio * 100:.1f}% < {self.partial_threshold * 100:.0f}%). "
                f"Status: verified_gap (hard-reset confidence: 0.00)."
            )

        logger.info(
            f"[AssessmentEvaluator] Evaluated {composite_key} ({q_type}): "
            f"matched {len(matched_keywords)}/{total_kw} ({match_ratio:.2%}) -> verdict={verdict}, strength={strength}"
        )

        return EvaluationResult(
            composite_key=composite_key,
            subskill_name=subskill_name,
            question=question_text,
            question_type=q_type,
            verdict=verdict,
            status=status,
            score=score,
            strength=strength,
            match_ratio=match_ratio,
            matched_keywords=matched_keywords,
            total_keywords=total_kw,
            feedback=feedback,
        )

    def evaluate_all(
        self,
        questions_data: list[dict[str, Any]],
        user_answers: dict[str, str],
    ) -> list[EvaluationResult]:
        """
        Evaluate all submitted answers in a session.

        Args:
            questions_data: List of question dicts from AssessmentSession.questions_data
            user_answers: Map of {composite_key: answer_text}

        Returns:
            List of EvaluationResult objects
        """
        results: list[EvaluationResult] = []
        for q in questions_data:
            ck = q.get("composite_key", "")
            ans = user_answers.get(ck, "")
            res = self.evaluate_answer(ck, ans, q)
            results.append(res)
        return results

    @staticmethod
    def _normalize_text(text: str) -> str:
        """Normalize text for consistent keyword matching."""
        text = text.lower()
        # Replace punctuation characters with spaces, except alphanumeric and standard dashes/underscores
        text = re.sub(r"[^\w\s\-\+\.\/]", " ", text)
        # Collapse multiple spaces
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def _keyword_matches(self, keyword: str, normalized_answer: str) -> bool:
        """
        Check if an expected keyword matches anywhere in the normalized candidate text.
        Handles alternative options separated by slashes / parentheses.
        """
        norm_kw = self._normalize_text(keyword)
        if not norm_kw:
            return False

        # Direct full phrase match
        if norm_kw in normalized_answer:
            return True

        # Check alternative terms split by slash or ' vs ' or ' or '
        split_terms = re.split(r"\s+(?:vs|\/|or)\s+", keyword.lower())
        if len(split_terms) > 1:
            for term in split_terms:
                norm_term = self._normalize_text(term)
                if norm_term and len(norm_term) > 2 and norm_term in normalized_answer:
                    return True

        # Token set match: if keyword consists of several tokens, check if all essential tokens are present
        tokens = [t for t in norm_kw.split() if len(t) > 2 and t not in {"and", "the", "for", "with", "from"}]
        if tokens and len(tokens) >= 2:
            if all(t in normalized_answer for t in tokens):
                return True

        return False
