"""
Evidence Engine Service.
Unified multi-source evidence fusion for RoleGauge.

Fuses signals from:
1. GitHub Evidence Detector (code/manifest analysis)
2. CV Skill Matcher (claimed skills, projects, work experience)
3. CV Certification Matcher (allowlist-matched certifications)
4. Assessment System (verified questions & answers)

Applies engine.json formulas:
- Primary signal (highest strength) + diminishing secondary signals (strength × diminishing_factor)
- Multi-source type ceilings (assessment_present=1.0, github_present=1.0, verified_work_experience=0.5,
  self_reported_skills_and_summary=0.3, certifications_only=0.2)
- Assessment override rules (verified_gap overrides all prior sources → hard cap 0.0)
- Explicit calculation_trace generation for auditability and transparency.
"""

import logging
from dataclasses import dataclass, field
from typing import Any, Optional

from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.kb_loader import KnowledgeBase

logger = logging.getLogger(__name__)


@dataclass
class ContributingSource:
    """A single source contributing to a subskill's evidence pool."""
    source: str
    strength: float
    signal: str
    file_path: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "strength": round(self.strength, 4),
            "signal": self.signal,
            "file_path": self.file_path,
        }


@dataclass
class UnifiedSubskillEvidence:
    """Unified subskill evidence result across all evidence sources."""
    composite_key: str
    subskill_name: str
    final_status: str  # evidence_found | claimed | not_yet_evidenced | verified_gap
    final_confidence: float
    contributing_sources: list[ContributingSource] = field(default_factory=list)
    ceiling_applied: str = ""
    calculation_trace: str = ""
    signals: list[EvidenceSignal] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "composite_key": self.composite_key,
            "subskill_name": self.subskill_name,
            "final_status": self.final_status,
            "final_confidence": round(self.final_confidence, 4),
            "contributing_sources": [s.to_dict() for s in self.contributing_sources],
            "ceiling_applied": self.ceiling_applied,
            "calculation_trace": self.calculation_trace,
        }

    def to_subskill_evidence_result(self) -> SubskillEvidenceResult:
        """Convert to SubskillEvidenceResult for compatibility with existing ScoringEngine."""
        res = SubskillEvidenceResult(
            composite_key=self.composite_key,
            subskill_name=self.subskill_name,
            status=self.final_status,
            signals=self.signals,
            contributing_sources=[s.to_dict() for s in self.contributing_sources],
            ceiling_applied=self.ceiling_applied,
            calculation_trace=self.calculation_trace,
        )
        return res


class EvidenceEngine:
    """
    Evidence Engine: Merges multi-source evidence signals per composite key
    and calculates final confidence using mathematical rules from engine.json.
    """

    def __init__(self, kb: KnowledgeBase, role_category: str, level: str = "mid"):
        self.kb = kb
        self.role_category = role_category
        self.level = level

        # Read dynamic constants from engine.json
        engine_config = kb.scoring_engine or {}
        formula_cfg = engine_config.get("multi_signal_confidence_formula", {})
        self.diminishing_factor = float(formula_cfg.get("diminishing_factor", 0.10))

        ceilings_cfg = engine_config.get("source_type_ceilings", {})
        self.source_ceilings = {
            "assessment_present": float(ceilings_cfg.get("assessment_present", 1.0)),
            "github_present": float(ceilings_cfg.get("github_present", 1.0)),
            "verified_work_experience": float(ceilings_cfg.get("verified_work_experience", 0.5)),
            "self_reported_skills_and_summary": float(ceilings_cfg.get("self_reported_skills_and_summary", 0.3)),
            "certifications_only": float(ceilings_cfg.get("certifications_only", 0.2)),
        }

        self.override_rules = engine_config.get("assessment_scoring_and_override_rules", {})

    def merge_evidence(
        self,
        github_evidence: Optional[dict[str, SubskillEvidenceResult]] = None,
        cv_skills_evidence: Optional[dict[str, SubskillEvidenceResult]] = None,
        cv_cert_matches: Optional[list[dict[str, Any]]] = None,
        assessment_evidence: Optional[dict[str, Any]] = None,
        linkedin_evidence: Optional[dict[str, SubskillEvidenceResult]] = None,
        linkedin_cert_matches: Optional[list[dict[str, Any]]] = None,
    ) -> dict[str, UnifiedSubskillEvidence]:
        """
        Merge all evidence sources into unified subskill results.

        Args:
            github_evidence: Results from EvidenceDetector
            cv_skills_evidence: Results from CVSkillMatcher
            cv_cert_matches: Results from CertificationMatcher for CV
            assessment_evidence: Optional assessment verification signals
            linkedin_evidence: Results from LinkedInSkillMatcher
            linkedin_cert_matches: Results from CertificationMatcher for LinkedIn

        Returns:
            dict[composite_key, UnifiedSubskillEvidence]
        """
        # Step 1: Initialize unified result pool for all subskills in the role
        unified: dict[str, UnifiedSubskillEvidence] = {}
        for skill_id, skill_data in self.kb.get_skills_for_role(self.role_category).items():
            for subskill in skill_data.get("subskills", []):
                ck = f"{skill_id}.{subskill['id']}"
                unified[ck] = UnifiedSubskillEvidence(
                    composite_key=ck,
                    subskill_name=subskill.get("name", subskill["id"]),
                    final_status="not_yet_evidenced",
                    final_confidence=0.0,
                )

        # Step 2: Ingest GitHub signals
        if github_evidence:
            for ck, result in github_evidence.items():
                if ck in unified:
                    for sig in result.signals:
                        unified[ck].signals.append(sig)
                        unified[ck].contributing_sources.append(ContributingSource(
                            source=sig.source if sig.source != "content_match" else "github",
                            strength=sig.strength,
                            signal=sig.matched_text,
                            file_path=sig.file_path,
                        ))

        # Step 3: Ingest CV Skill signals
        if cv_skills_evidence:
            for ck, result in cv_skills_evidence.items():
                if ck in unified:
                    for sig in result.signals:
                        unified[ck].signals.append(sig)
                        unified[ck].contributing_sources.append(ContributingSource(
                            source=sig.source,
                            strength=sig.strength,
                            signal=sig.matched_text,
                            file_path=sig.file_path,
                        ))

        # Step 4: Ingest CV Certification signals
        if cv_cert_matches:
            for cert in cv_cert_matches:
                if cert.get("classification") == "recognized_relevant" and cert.get("matched_composite_keys"):
                    cert_name = cert.get("certificate_name", "Certification")
                    strength = float(cert.get("strength", 0.2))
                    for ck in cert["matched_composite_keys"]:
                        if ck in unified:
                            sig = EvidenceSignal(
                                source="cv_certification",
                                file_path="cv/certifications",
                                matched_text=cert_name,
                                strength=strength,
                            )
                            unified[ck].signals.append(sig)
                            unified[ck].contributing_sources.append(ContributingSource(
                                source="cv_certification",
                                strength=strength,
                                signal=cert_name,
                                file_path="cv/certifications",
                            ))

        # Step 5: Ingest LinkedIn Skill & Profile signals
        if linkedin_evidence:
            for ck, result in linkedin_evidence.items():
                if ck in unified:
                    for sig in result.signals:
                        unified[ck].signals.append(sig)
                        unified[ck].contributing_sources.append(ContributingSource(
                            source=sig.source,
                            strength=sig.strength,
                            signal=sig.matched_text,
                            file_path=sig.file_path,
                        ))

        # Step 6: Ingest LinkedIn Certification signals
        if linkedin_cert_matches:
            for cert in linkedin_cert_matches:
                if cert.get("classification") == "recognized_relevant" and cert.get("matched_composite_keys"):
                    cert_name = cert.get("certificate_name", "Certification")
                    strength = float(cert.get("strength", 0.2))
                    for ck in cert["matched_composite_keys"]:
                        if ck in unified:
                            sig = EvidenceSignal(
                                source="linkedin_certification",
                                file_path="linkedin/certifications",
                                matched_text=cert_name,
                                strength=strength,
                            )
                            unified[ck].signals.append(sig)
                            unified[ck].contributing_sources.append(ContributingSource(
                                source="linkedin_certification",
                                strength=strength,
                                signal=cert_name,
                                file_path="linkedin/certifications",
                            ))

        # Step 7: Ingest Assessment signals (if any)
        assessment_signals_map: dict[str, list[dict[str, Any]]] = {}
        if assessment_evidence:
            for ck, signals in assessment_evidence.items():
                if ck in unified:
                    if isinstance(signals, list):
                        assessment_signals_map[ck] = signals
                        for asig in signals:
                            strength = float(asig.get("strength", 1.0))
                            status = asig.get("status", "evidence_found")
                            sig = EvidenceSignal(
                                source="assessment",
                                file_path="assessment/session",
                                matched_text=asig.get("detail", "Assessment response"),
                                strength=strength,
                            )
                            unified[ck].signals.append(sig)
                            unified[ck].contributing_sources.append(ContributingSource(
                                source="assessment",
                                strength=strength,
                                signal=f"Assessment [{status}]: {asig.get('detail', '')}",
                                file_path="assessment/session",
                            ))

        # Step 8: Execute multi-signal confidence math & assessment override per composite key
        for ck, item in unified.items():
            self._calculate_subskill_confidence(item, assessment_signals_map.get(ck, []))

        logger.info(
            f"[EvidenceEngine] Merged evidence for role '{self.role_category}': "
            f"{sum(1 for u in unified.values() if u.final_status == 'evidence_found')} evidence_found, "
            f"{sum(1 for u in unified.values() if u.final_status == 'claimed')} claimed, "
            f"{sum(1 for u in unified.values() if u.final_status == 'verified_gap')} verified_gap, "
            f"{sum(1 for u in unified.values() if u.final_status == 'not_yet_evidenced')} not_yet_evidenced"
        )

        return unified

    def _calculate_subskill_confidence(
        self,
        item: UnifiedSubskillEvidence,
        assessment_signals: list[dict[str, Any]],
    ) -> None:
        """
        Calculate final confidence, status, ceiling, and trace for a single subskill.
        """
        # ── Case 1: No evidence signals at all ──
        if not item.signals:
            item.final_status = "not_yet_evidenced"
            item.final_confidence = 0.0
            item.ceiling_applied = "none"
            item.calculation_trace = "no_signals -> raw=0.0 -> ceiling=N/A -> final=0.0"
            return

        # ── Case 2: Assessment Override (verified_gap / failed question) ──
        # Check if any assessment signal is an explicit failure / gap
        is_verified_gap = False
        gap_reason = ""
        for asig in assessment_signals:
            status = asig.get("status", "")
            score = asig.get("score", None)
            if status in ("verified_gap", "incorrect_answer", "gap") or (score is not None and float(score) == 0.0):
                is_verified_gap = True
                gap_reason = asig.get("detail", "Incorrect assessment answer")
                break

        if is_verified_gap:
            item.final_status = "verified_gap"
            item.final_confidence = 0.0
            item.ceiling_applied = "assessment_override_verified_gap (0.0)"
            item.calculation_trace = (
                f"assessment_override: verified_gap ({gap_reason}) overrides all prior sources "
                f"({len(item.signals)} signals) -> final=0.0"
            )
            return

        # ── Case 3: Standard Multi-Source Confidence Calculation ──
        # Sort signals descending by strength
        sorted_signals = sorted(item.signals, key=lambda s: s.strength, reverse=True)
        primary = sorted_signals[0]
        primary_strength = primary.strength
        primary_source = primary.source

        # Secondary signals weighted by diminishing_factor (0.10)
        secondary_signals = sorted_signals[1:]
        secondary_sum = sum(s.strength * self.diminishing_factor for s in secondary_signals)
        raw_confidence = primary_strength + secondary_sum

        # Determine source type ceiling
        ceiling_name, ceiling_val = self._determine_ceiling(sorted_signals)
        final_confidence = min(raw_confidence, ceiling_val)

        item.final_confidence = round(final_confidence, 4)
        item.ceiling_applied = f"{ceiling_name} ({ceiling_val:.2f})"

        # Determine final status
        has_verified_source = any(
            s.source in {"github", "file_presence", "content_match", "dependency", "assessment"} and s.strength >= 0.5
            for s in sorted_signals
        )
        if final_confidence > 0:
            item.final_status = "evidence_found" if has_verified_source else "claimed"
        else:
            item.final_status = "not_yet_evidenced"

        # Build readable calculation trace
        if secondary_signals:
            sec_details = " + ".join(
                f"{s.strength:.2f}*{self.diminishing_factor:.2f}" for s in secondary_signals
            )
            item.calculation_trace = (
                f"primary={primary_strength:.2f} ({primary_source}) + "
                f"secondary=[{sec_details}]={secondary_sum:.3f} -> "
                f"raw={raw_confidence:.3f} -> ceiling={ceiling_val:.2f} ({ceiling_name}) -> "
                f"final={final_confidence:.3f}"
            )
        else:
            item.calculation_trace = (
                f"primary={primary_strength:.2f} ({primary_source}) -> "
                f"raw={raw_confidence:.3f} -> ceiling={ceiling_val:.2f} ({ceiling_name}) -> "
                f"final={final_confidence:.3f}"
            )

    def _determine_ceiling(self, signals: list[EvidenceSignal]) -> tuple[str, float]:
        """
        Determine source type ceiling based on the strongest available evidence source.
        Returns: (ceiling_name, ceiling_value)
        """
        sources = {s.source for s in signals}
        max_strength = signals[0].strength if signals else 0.0

        # Assessment present with high confidence
        if "assessment" in sources and max_strength >= 0.5:
            return "assessment_present", self.source_ceilings.get("assessment_present", 1.0)

        # GitHub code/manifest presence with sufficient strength (>= 0.5)
        github_sources = {"github", "file_presence", "content_match", "dependency"}
        if any(s in sources for s in github_sources) and max_strength >= 0.5:
            return "github_present", self.source_ceilings.get("github_present", 1.0)

        # Verified work experience / projects from CV or LinkedIn
        work_exp_sources = {
            "cv_experience", "cv_project", "linkedin_experience", "linkedin_project",
        }
        if any(s in sources for s in work_exp_sources):
            return "verified_work_experience", self.source_ceilings.get("verified_work_experience", 0.5)

        # Self-reported skills list, summary, or education (including LinkedIn skills/endorsements/summary/posts/recommendations)
        self_reported_sources = {
            "cv_skills_list", "cv_education", "readme", "cv_signal_pattern",
            "linkedin_summary", "linkedin_skills", "linkedin_skills_endorsements",
            "linkedin_post", "linkedin_posts_articles", "linkedin_article",
            "linkedin_recommendation", "linkedin_recommendations",
            "linkedin_signal_pattern",
        }
        if any(s in sources for s in self_reported_sources):
            return "self_reported_skills_and_summary", self.source_ceilings.get("self_reported_skills_and_summary", 0.3)

        # Certifications only
        cert_sources = {"cv_certification", "linkedin_certification"}
        if any(s in sources for s in cert_sources):
            return "certifications_only", self.source_ceilings.get("certifications_only", 0.2)

        # Default fallback
        if max_strength < 0.5:
            return "self_reported_skills_and_summary", self.source_ceilings.get("self_reported_skills_and_summary", 0.3)

        return "github_present", self.source_ceilings.get("github_present", 1.0)
