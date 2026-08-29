"""
Scoring Engine.
Implements the exact mathematical algorithms from engine.json to transform
evidence signals into subskill confidence, skill scores, and role readiness.

CRITICAL: This module is the SOLE authority for numeric scoring.
AI does NOT produce scores — it only detects evidence.
All formula constants and weights are dynamically read from engine.json.
"""

import logging
import re
from typing import Any

from app.services.kb_loader import KnowledgeBase
from app.services.evidence_detector import SubskillEvidenceResult

logger = logging.getLogger(__name__)


class ScoringEngine:
    """
    Deterministic scoring engine that implements dynamic engine.json formulas.

    Pipeline:
    1. Evidence → Subskill Confidence (0.0 - 1.0)
    2. Subskill Confidence → Skill Score (0.0 - 1.0)
    3. Skill Scores → Role Readiness Score (0.0 - 1.0)
    """

    def __init__(self, kb: KnowledgeBase, role_category: str, level: str):
        self.kb = kb
        self.role_category = role_category
        self.level = level
        self.role_def = kb.get_role(role_category, level)

        # -------------------------------------------------------------
        # DYNAMIC LOADING FROM engine.json
        # -------------------------------------------------------------
        engine_config = kb.scoring_engine or {}
        self.engine_version = engine_config.get("engine_version", "1.2.0")

        # Step 1: Subskill Confidence Config
        step1_rules = engine_config.get("step_1_evidence_to_subskill_confidence", {}).get("rules", {})
        self.diminishing_factor = float(step1_rules.get("diminishing_factor", 0.10))
        self.source_ceilings = dict(step1_rules.get("source_type_ceilings", {}).get("categories", {
            "github_present": 1.0,
            "assessment_present": 1.0,
            "verified_work_experience": 0.5,
            "self_reported_skills_and_summary": 0.3,
            "certifications_only": 0.2,
        }))

        # Step 2: Subskill to Skill Score Config
        step2_config = engine_config.get("step_2_subskill_to_skill_score", {})
        subskill_weights = step2_config.get("subskill_weights_in_base_score", {})
        self.target_level_weight = float(subskill_weights.get("target_level_subskills", 1.0))
        self.lower_level_weight = float(subskill_weights.get("lower_level_prerequisites", 0.8))
        self.bonus_multiplier = 0.15

        # Step 3: Role Readiness Config
        step3_config = engine_config.get("step_3_skill_to_role_readiness", {})
        boundary_table = step3_config.get("threshold_evaluation", {}).get("boundary_table", [])
        self.readiness_tiers = self._parse_boundary_table(boundary_table)

        logger.info(
            f"[ScoringEngine] Dynamically configured from engine.json (v{self.engine_version}): "
            f"diminishing_factor={self.diminishing_factor}, "
            f"target_weight={self.target_level_weight}, lower_weight={self.lower_level_weight}, "
            f"ceilings={self.source_ceilings}"
        )

    def _parse_boundary_table(self, boundary_table: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Parse readiness tier boundary table from engine.json."""
        default_tiers = [
            {"tier": "not_ready", "label": "Not Ready", "min": 0.00, "max": 0.30},
            {"tier": "developing", "label": "Developing", "min": 0.30, "max": 0.50},
            {"tier": "approaching", "label": "Approaching Ready", "min": 0.50, "max": 0.70},
            {"tier": "ready", "label": "Ready", "min": 0.70, "max": 0.85},
            {"tier": "exceeds", "label": "Exceeds Expectations", "min": 0.85, "max": 1.01},
        ]
        if not boundary_table:
            return default_tiers

        parsed = []
        label_map = {
            "not_ready": "Not Ready",
            "developing": "Developing",
            "approaching": "Approaching Ready",
            "ready": "Ready",
            "exceeds": "Exceeds Expectations",
        }

        for entry in boundary_table:
            tier_name = entry.get("tier", "")
            range_str = entry.get("range", "")
            matches = re.findall(r"(\d+\.\d+)", range_str)
            if len(matches) >= 2:
                min_val = float(matches[0])
                max_val = float(matches[1])
                # Exceeds upper bound is inclusive of 1.0
                if tier_name == "exceeds" and max_val == 1.00:
                    max_val = 1.01
                parsed.append({
                    "tier": tier_name,
                    "label": label_map.get(tier_name, tier_name.replace("_", " ").title()),
                    "min": min_val,
                    "max": max_val,
                })
            else:
                for def_tier in default_tiers:
                    if def_tier["tier"] == tier_name:
                        parsed.append(def_tier)
                        break

        return parsed if parsed else default_tiers

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

        logger.info(
            f"[ScoringEngine Summary] Calculated Readiness: {readiness_score:.4f} "
            f"({tier_info['label']}) across {len(skill_results)} skills."
        )

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
        Formula: confidence = min(max_primary + sum(secondary × diminishing_factor), source_type_ceiling)
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

            # Secondary signals = all remaining, weighted by dynamic diminishing_factor
            secondary_sum = sum(
                s.strength * self.diminishing_factor
                for s in sorted_signals[1:]
            )

            raw_confidence = primary_strength + secondary_sum

            # Determine ceiling based on source type
            ceiling = self._determine_ceiling(sorted_signals)

            confidence = min(raw_confidence, ceiling)
            confidences[composite_key] = round(confidence, 4)

            logger.debug(
                f"[ScoringEngine Step 1] {composite_key} | signals={len(result.signals)} | "
                f"primary={primary_strength:.3f}, secondary_sum={secondary_sum:.4f} "
                f"(dim_factor={self.diminishing_factor}), raw={raw_confidence:.4f}, "
                f"ceiling={ceiling:.2f} -> final_conf={confidence:.4f}"
            )

        return confidences

    def _determine_ceiling(self, signals: list) -> float:
        """
        Determine the source type ceiling based on the strongest evidence source.
        Uses dynamic source_ceilings dictionary from engine.json.
        """
        max_strength = signals[0].strength if signals else 0.0
        source_types = {s.source for s in signals}

        # GitHub code/file evidence with sufficient strength (>= 0.5)
        if max_strength >= 0.5 and any(s in source_types for s in {"file_presence", "content_match", "dependency"}):
            return self.source_ceilings.get("github_present", 1.0)

        # README only
        if source_types == {"readme"}:
            return self.source_ceilings.get("self_reported_skills_and_summary", 0.3)

        # Weak github signals (< 0.5)
        if max_strength < 0.5:
            return self.source_ceilings.get("self_reported_skills_and_summary", 0.3)

        # Default to github ceiling
        return self.source_ceilings.get("github_present", 1.0)

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
                    # Determine weight: target level = target_level_weight (1.0), lower = lower_level_weight (0.8)
                    weight = self.target_level_weight
                    for lvl_name, lvl_data in skill_data.get("levels", {}).items():
                        lvl_idx = levels_order.index(lvl_name) if lvl_name in levels_order else 0
                        if subskill_id in lvl_data.get("expected_subskills", []) and lvl_idx < target_idx:
                            weight = self.lower_level_weight
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

            # Bonus from higher-level subskills (DENOMINATOR ISOLATION: bonus subskills only add to bonus_score)
            bonus_score = 0.0
            for subskill_id in bonus:
                composite_key = f"{skill_id}.{subskill_id}"
                confidence = confidences.get(composite_key, 0.0)
                if confidence > 0.0:
                    bonus_score += confidence * self.bonus_multiplier

            # Final skill score capped at 1.0
            skill_score = min(base_score + bonus_score, 1.0)

            logger.debug(
                f"[ScoringEngine Step 2] Skill '{skill_id}' ({skill_name}) | "
                f"expected={len(expected)}, isolated_bonus_subskills={len(bonus)} | "
                f"num={numerator:.4f}, denom={denominator:.4f} -> base={base_score:.4f}, "
                f"bonus={bonus_score:.4f} -> final_skill_score={skill_score:.4f}"
            )

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

        readiness = numerator / denominator
        logger.debug(
            f"[ScoringEngine Step 3] Aggregation: num={numerator:.4f}, denom={denominator:.4f} -> readiness={readiness:.4f}"
        )
        return readiness

    def _get_readiness_tier(self, score: float) -> dict[str, str]:
        """Determine readiness tier from score using inclusive min, exclusive max bounds."""
        for tier in self.readiness_tiers:
            if tier["min"] <= score < tier["max"]:
                return {"tier": tier["tier"], "label": tier["label"]}

        # Fallback
        return {"tier": "not_ready", "label": "Not Ready"}
