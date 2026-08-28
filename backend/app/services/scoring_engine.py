"""
Scoring Engine.
Implements the exact mathematical algorithms from engine.json to transform
evidence signals into subskill confidence, skill scores, and role readiness.

CRITICAL: This module is the SOLE authority for numeric scoring.
AI does NOT produce scores — it only detects evidence.
"""

import logging
from typing import Any

from app.services.kb_loader import KnowledgeBase
from app.services.evidence_detector import SubskillEvidenceResult

logger = logging.getLogger(__name__)


class ScoringEngine:
    """
    Deterministic scoring engine that implements engine.json formulas.

    Pipeline:
    1. Evidence → Subskill Confidence (0.0 - 1.0)
    2. Subskill Confidence → Skill Score (0.0 - 1.0)
    3. Skill Scores → Role Readiness Score (0.0 - 1.0)
    """

    # Source type ceilings from engine.json
    SOURCE_CEILINGS = {
        "github_present": 1.0,
        "assessment_present": 1.0,
        "verified_work_experience": 0.5,
        "self_reported_skills_and_summary": 0.3,
        "certifications_only": 0.2,
    }

    # Diminishing factor for secondary signals
    DIMINISHING_FACTOR = 0.10

    # Subskill weights in base_score calculation
    TARGET_LEVEL_WEIGHT = 1.0
    LOWER_LEVEL_WEIGHT = 0.8

    # Bonus multiplier for higher-level subskills
    BONUS_MULTIPLIER = 0.15

    # Readiness tiers (inclusive min, exclusive max, except top)
    READINESS_TIERS = [
        {"tier": "not_ready", "label": "Not Ready", "min": 0.00, "max": 0.30},
        {"tier": "developing", "label": "Developing", "min": 0.30, "max": 0.50},
        {"tier": "approaching", "label": "Approaching Ready", "min": 0.50, "max": 0.70},
        {"tier": "ready", "label": "Ready", "min": 0.70, "max": 0.85},
        {"tier": "exceeds", "label": "Exceeds Expectations", "min": 0.85, "max": 1.01},
    ]

    def __init__(self, kb: KnowledgeBase, role_category: str, level: str):
        self.kb = kb
        self.role_category = role_category
        self.level = level
        self.role_def = kb.get_role(role_category, level)

    def calculate_all(
        self, evidence: dict[str, SubskillEvidenceResult]
    ) -> dict[str, Any]:
        """
        Run the full scoring pipeline.
        Returns: {
            "readiness_score": float,
            "readiness_tier": str,
            "readiness_label": str,
            "skills": [{skill_id, skill_name, score, importance, subskills: [...]}]
        }
        """
        if not self.role_def:
            raise ValueError(f"Role definition not found: {self.role_category}/{self.level}")

        # Step 1: Calculate subskill confidences
        confidences = self._step1_evidence_to_confidence(evidence)

        # Step 2: Calculate skill scores
        skill_results = self._step2_confidence_to_skill_scores(confidences, evidence)

        # Step 3: Calculate readiness score
        readiness_score = self._step3_skill_to_readiness(skill_results)
        tier_info = self._get_readiness_tier(readiness_score)

        return {
            "readiness_score": round(readiness_score, 4),
            "readiness_tier": tier_info["tier"],
            "readiness_label": tier_info["label"],
            "skills": skill_results,
        }

    def _step1_evidence_to_confidence(
        self, evidence: dict[str, SubskillEvidenceResult]
    ) -> dict[str, float]:
        """
        Step 1: Transform evidence signals into subskill confidence (0.0 - 1.0).
        Formula: confidence = min(max_primary + sum(secondary × diminishing), ceiling)
        """
        confidences: dict[str, float] = {}

        for composite_key, result in evidence.items():
            if not result.signals:
                confidences[composite_key] = 0.0
                continue

            # Sort signals by strength (descending)
            sorted_signals = sorted(result.signals, key=lambda s: s.strength, reverse=True)

            # Primary signal = highest strength
            primary_strength = sorted_signals[0].strength

            # Secondary signals = all remaining
            secondary_sum = sum(
                s.strength * self.DIMINISHING_FACTOR
                for s in sorted_signals[1:]
            )

            raw_confidence = primary_strength + secondary_sum

            # Determine ceiling based on source type
            ceiling = self._determine_ceiling(sorted_signals)

            confidence = min(raw_confidence, ceiling)
            confidences[composite_key] = round(confidence, 4)

        return confidences

    def _determine_ceiling(self, signals: list) -> float:
        """
        Determine the source type ceiling based on the strongest evidence source.
        GitHub code = 1.0 (if strong signal >= 0.5)
        """
        max_strength = signals[0].strength if signals else 0.0
        source_types = {s.source for s in signals}

        # GitHub code/file evidence with sufficient strength
        if max_strength >= 0.5 and any(s in source_types for s in {"file_presence", "content_match"}):
            return self.SOURCE_CEILINGS["github_present"]

        # Dependency evidence
        if "dependency" in source_types and max_strength >= 0.5:
            return self.SOURCE_CEILINGS["github_present"]

        # README only
        if source_types == {"readme"}:
            return self.SOURCE_CEILINGS["self_reported_skills_and_summary"]

        # Weak github signals
        if max_strength < 0.5:
            return self.SOURCE_CEILINGS["self_reported_skills_and_summary"]

        # Default to github ceiling
        return self.SOURCE_CEILINGS["github_present"]

    def _step2_confidence_to_skill_scores(
        self,
        confidences: dict[str, float],
        evidence: dict[str, SubskillEvidenceResult],
    ) -> list[dict[str, Any]]:
        """
        Step 2: Aggregate subskill confidences into skill scores.
        Respects denominator isolation: bonus subskills never enter denominator.
        """
        if not self.role_def:
            return []

        skill_results = []
        skills_config = self.role_def.get("skills", [])

        for skill_config in skills_config:
            skill_id = skill_config["skill_id"]
            importance = skill_config.get("importance", 0.5)

            # Get expected vs bonus subskills for this level
            level_info = self.kb.get_subskills_for_level(self.role_category, skill_id, self.level)
            expected = level_info["expected"]
            bonus = level_info["bonus"]

            skill_data = self.kb.get_skills_for_role(self.role_category).get(skill_id, {})
            skill_name = skill_data.get("name", skill_id)

            # Calculate base_score from expected subskills
            numerator = 0.0
            denominator = 0.0
            subskill_details = []

            # Determine which subskills are at target level vs lower prerequisites
            levels_order = ["junior", "mid", "senior"]
            target_idx = levels_order.index(self.level) if self.level in levels_order else 0

            for subskill in skill_data.get("subskills", []):
                subskill_id = subskill["id"]
                composite_key = f"{skill_id}.{subskill_id}"
                confidence = confidences.get(composite_key, 0.0)
                evidence_result = evidence.get(composite_key)

                is_expected = subskill_id in expected
                is_bonus = subskill_id in bonus

                if is_expected:
                    # Determine weight: target level = 1.0, lower = 0.8
                    weight = self.TARGET_LEVEL_WEIGHT
                    # Check if this subskill is from a lower level
                    for lvl_name, lvl_data in skill_data.get("levels", {}).items():
                        lvl_idx = levels_order.index(lvl_name) if lvl_name in levels_order else 0
                        if subskill_id in lvl_data.get("expected_subskills", []) and lvl_idx < target_idx:
                            weight = self.LOWER_LEVEL_WEIGHT
                            break

                    numerator += confidence * weight
                    denominator += weight

                subskill_details.append({
                    "composite_key": composite_key,
                    "subskill_name": subskill.get("name", subskill_id),
                    "confidence": round(confidence, 4),
                    "status": evidence_result.status if evidence_result else "not_yet_evidenced",
                    "evidence_sources": evidence_result.evidence_sources[:10] if evidence_result else [],
                    "is_expected": is_expected,
                    "is_bonus": is_bonus,
                })

            # Base score
            base_score = numerator / denominator if denominator > 0 else 0.0

            # Bonus from higher-level subskills
            bonus_score = 0.0
            for subskill_id in bonus:
                composite_key = f"{skill_id}.{subskill_id}"
                confidence = confidences.get(composite_key, 0.0)
                if confidence > 0.0:
                    bonus_score += confidence * self.BONUS_MULTIPLIER

            # Final skill score
            skill_score = min(base_score + bonus_score, 1.0)

            skill_results.append({
                "skill_id": skill_id,
                "skill_name": skill_name,
                "score": round(skill_score, 4),
                "importance": importance,
                "base_score": round(base_score, 4),
                "bonus_score": round(bonus_score, 4),
                "subskills": subskill_details,
            })

        return skill_results

    def _step3_skill_to_readiness(self, skill_results: list[dict[str, Any]]) -> float:
        """
        Step 3: Combine skill scores with importance weights into readiness score.
        Formula: readiness = sum(score × importance) / sum(importance)
        """
        numerator = sum(s["score"] * s["importance"] for s in skill_results)
        denominator = sum(s["importance"] for s in skill_results)

        if denominator == 0:
            return 0.0

        return numerator / denominator

    def _get_readiness_tier(self, score: float) -> dict[str, str]:
        """Determine readiness tier from score using inclusive min, exclusive max."""
        for tier in self.READINESS_TIERS:
            if tier["min"] <= score < tier["max"]:
                return {"tier": tier["tier"], "label": tier["label"]}

        # Fallback (should not happen)
        return {"tier": "not_ready", "label": "Not Ready"}
