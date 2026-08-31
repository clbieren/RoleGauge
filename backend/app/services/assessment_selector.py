"""
Assessment Selector Service.
Selects targeted technical questions for candidate assessment based on
trigger conditions defined in evidence/{role}/assessment.json:

1. not_yet_evidenced (confidence = 0.0) in target role's expected_subskills -> High priority
2. insufficient_evidence / claimed (confidence < 0.4) -> Medium priority
3. Critical skills (importance >= 0.80) with ambiguous evidence -> Priority boost
4. Voluntary candidate requests -> Top priority
"""

import logging
from dataclasses import dataclass, field
from typing import Any, Optional

from app.services.kb_loader import KnowledgeBase, kb

logger = logging.getLogger(__name__)


@dataclass
class SelectedQuestion:
    """A selected assessment question with internal evaluation metadata."""
    composite_key: str
    subskill_name: str
    skill_id: str
    question: str
    type: str  # conceptual | scenario | practical_task
    level: str  # junior | mid | senior
    expected_answer_keywords: list[str] = field(default_factory=list)
    priority_score: float = 0.0
    priority_reason: str = ""

    def to_public_dict(self) -> dict[str, Any]:
        """Convert to public dictionary, strictly omitting expected_answer_keywords."""
        return {
            "composite_key": self.composite_key,
            "subskill_name": self.subskill_name,
            "question": self.question,
            "type": self.type,
            "level": self.level,
        }

    def to_internal_dict(self) -> dict[str, Any]:
        """Convert to internal server-side dictionary including expected_answer_keywords."""
        return {
            "composite_key": self.composite_key,
            "subskill_name": self.subskill_name,
            "skill_id": self.skill_id,
            "question": self.question,
            "type": self.type,
            "level": self.level,
            "expected_answer_keywords": self.expected_answer_keywords,
            "priority_score": self.priority_score,
            "priority_reason": self.priority_reason,
        }


class AssessmentSelector:
    """
    Selects and prioritizes questions for an assessment session based on
    the candidate's current evidence state and role requirements.
    """

    def __init__(self, knowledge_base: KnowledgeBase | None = None):
        self.kb = knowledge_base or kb

    def select_questions(
        self,
        role_id: str,
        level: str = "mid",
        subskills_evidence: Optional[dict[str, Any]] = None,
        voluntary_composite_keys: Optional[list[str]] = None,
        max_questions: int = 10,
    ) -> list[SelectedQuestion]:
        """
        Select adaptive assessment questions for a candidate.

        Args:
            role_id: Target role category (e.g., 'backend', 'devops')
            level: Target seniority level ('junior', 'mid', 'senior')
            subskills_evidence: Current subskill evidence map {composite_key: {confidence, status, ...}}
                                or dict of UnifiedSubskillEvidence / SubskillEvidence
            voluntary_composite_keys: Specific composite keys requested by the candidate
            max_questions: Max number of questions to return (default 10)

        Returns:
            List of SelectedQuestion objects sorted by priority descending
        """
        subskills_evidence = subskills_evidence or {}
        voluntary_keys = set(voluntary_composite_keys or [])

        # Load role definition and assessment question bank
        role_def = self.kb.get_role(role_id, level)
        if not role_def:
            logger.warning(f"Role definition not found for {role_id}/{level}")
            return []

        assessment_data = self.kb.get_evidence_for_role(role_id, "assessment")
        if not assessment_data:
            logger.warning(f"No assessment.json found for role '{role_id}'")
            return []

        question_bank: dict[str, list[dict[str, Any]]] = assessment_data.get(
            "sample_questions_by_composite_key", {}
        )

        # Build skill importance lookup
        skill_importance_map: dict[str, float] = {}
        for s in role_def.get("skills", []):
            skill_importance_map[s["skill_id"]] = float(s.get("importance", 0.5))

        # Collect all role subskills and their level categorization
        candidate_subskills: list[dict[str, Any]] = []
        for skill_id, skill_data in self.kb.get_skills_for_role(role_id).items():
            level_info = self.kb.get_subskills_for_level(role_id, skill_id, level)
            expected_subskills = set(level_info.get("expected", []))
            bonus_subskills = set(level_info.get("bonus", []))
            importance = skill_importance_map.get(skill_id, 0.5)

            for subskill in skill_data.get("subskills", []):
                sub_id = subskill["id"]
                ck = f"{skill_id}.{sub_id}"
                sub_name = subskill.get("name", sub_id)
                is_expected = sub_id in expected_subskills
                is_bonus = sub_id in bonus_subskills

                # Extract current evidence state if available
                current_conf = 0.0
                current_status = "not_yet_evidenced"
                if ck in subskills_evidence:
                    ev = subskills_evidence[ck]
                    if isinstance(ev, dict):
                        current_conf = float(ev.get("confidence", ev.get("final_confidence", 0.0)))
                        current_status = str(ev.get("status", ev.get("final_status", "not_yet_evidenced")))
                    elif hasattr(ev, "confidence"):
                        current_conf = float(getattr(ev, "confidence", 0.0))
                        current_status = str(getattr(ev, "status", "not_yet_evidenced"))
                    elif hasattr(ev, "final_confidence"):
                        current_conf = float(getattr(ev, "final_confidence", 0.0))
                        current_status = str(getattr(ev, "final_status", "not_yet_evidenced"))

                # Check if question bank has questions for this composite key
                if ck not in question_bank or not question_bank[ck]:
                    continue

                # Calculate priority score based on trigger conditions
                priority_score, priority_reason = self._compute_priority(
                    composite_key=ck,
                    confidence=current_conf,
                    status=current_status,
                    is_expected=is_expected,
                    is_bonus=is_bonus,
                    skill_importance=importance,
                    is_voluntary=ck in voluntary_keys,
                )

                candidate_subskills.append({
                    "composite_key": ck,
                    "subskill_name": sub_name,
                    "skill_id": skill_id,
                    "confidence": current_conf,
                    "status": current_status,
                    "priority_score": priority_score,
                    "priority_reason": priority_reason,
                    "questions": question_bank[ck],
                })

        # Sort candidate subskills by priority score descending
        candidate_subskills.sort(key=lambda x: x["priority_score"], reverse=True)

        # Select the best question for each prioritized subskill
        selected: list[SelectedQuestion] = []
        for cand in candidate_subskills:
            if cand["priority_score"] <= 0:
                continue

            q_obj = self._pick_best_question(cand["questions"], target_level=level)
            if not q_obj:
                continue

            selected.append(SelectedQuestion(
                composite_key=cand["composite_key"],
                subskill_name=cand["subskill_name"],
                skill_id=cand["skill_id"],
                question=q_obj.get("question", ""),
                type=q_obj.get("type", "scenario"),
                level=q_obj.get("level", level),
                expected_answer_keywords=q_obj.get("expected_answer_keywords", []),
                priority_score=cand["priority_score"],
                priority_reason=cand["priority_reason"],
            ))

            if len(selected) >= max_questions:
                break

        logger.info(
            f"[AssessmentSelector] Selected {len(selected)} questions for role '{role_id}' (level: {level})"
        )
        return selected

    def _compute_priority(
        self,
        composite_key: str,
        confidence: float,
        status: str,
        is_expected: bool,
        is_bonus: bool,
        skill_importance: float,
        is_voluntary: bool,
    ) -> tuple[float, str]:
        """
        Compute prioritization score based on trigger conditions from assessment.json.
        """
        reasons: list[str] = []
        priority = 0.0

        # Voluntary request by candidate (highest priority)
        if is_voluntary:
            priority += 100.0
            reasons.append("voluntary_request")

        # Condition 1: not_yet_evidenced (confidence = 0.0) for required/expected subskill
        if is_expected and (status == "not_yet_evidenced" or confidence == 0.0):
            priority += 50.0
            reasons.append("not_yet_evidenced_expected")

        # Condition 2: insufficient_evidence / claimed (confidence < 0.40)
        elif status in ("claimed", "insufficient_evidence") or (0.0 < confidence < 0.40):
            priority += 30.0
            reasons.append("insufficient_evidence")

        # Condition 3: Critical skill (importance >= 0.80) with non-max confidence (< 0.70)
        if skill_importance >= 0.80 and confidence < 0.70:
            priority += 20.0 * skill_importance
            reasons.append(f"critical_skill_importance_{skill_importance:.2f}")

        # Bonus subskill penalty (focus on required subskills first unless voluntary)
        if is_bonus and not is_voluntary:
            priority -= 15.0
            reasons.append("bonus_subskill_lower_priority")

        # Already verified gap: lower priority unless voluntary (don't endlessly re-ask failed questions)
        if status == "verified_gap" and not is_voluntary:
            priority = 0.0
            reasons.append("already_verified_gap")

        # Already strongly evidenced (confidence >= 0.80): low priority unless voluntary
        if confidence >= 0.80 and not is_voluntary:
            priority = 5.0
            reasons.append("already_evidenced_strong")

        reason_str = ", ".join(reasons) if reasons else "standard"
        return round(priority, 2), reason_str

    def _pick_best_question(
        self,
        questions: list[dict[str, Any]],
        target_level: str,
    ) -> dict[str, Any] | None:
        """
        Pick the most appropriate question from the list for the given target level.
        Preference order:
        1. Exact level match
        2. Closest level (mid -> junior/senior, junior -> mid, senior -> mid)
        """
        if not questions:
            return None

        # Exact match
        for q in questions:
            if q.get("level", "").lower() == target_level.lower():
                return q

        # Fallback hierarchy
        levels_order = ["junior", "mid", "senior"]
        target_idx = levels_order.index(target_level) if target_level in levels_order else 1

        # Search nearest level
        sorted_by_distance = sorted(
            questions,
            key=lambda q: abs(
                (levels_order.index(q.get("level", "mid").lower())
                 if q.get("level", "").lower() in levels_order else 1)
                - target_idx
            )
        )
        return sorted_by_distance[0] if sorted_by_distance else questions[0]
