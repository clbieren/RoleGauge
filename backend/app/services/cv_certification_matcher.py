"""
CV Certification Matcher.
Strict allowlist-based matching of CV certificates against the knowledge base.
NO fuzzy matching, NO semantic/embedding similarity, NO AI interpretation.

Three-way classification:
- recognized_relevant: cert is in allowlist AND has signal_mapping pattern → contributes to score
- recognized_no_mapping: cert is in allowlist BUT no signal_mapping pattern → no score contribution
- unrecognized_excluded: cert is NOT in any allowlist → no score contribution
"""

import logging
import os
import re
from typing import Any

from app.services.kb_loader import KnowledgeBase

logger = logging.getLogger(__name__)


def _normalize_cert_name(name: str) -> str:
    """
    Normalize a certificate name for comparison.
    - Lowercase
    - Strip whitespace
    - Collapse multiple spaces
    - Remove trailing/leading punctuation
    - Remove parenthetical abbreviations (but keep them as separate lookup)
    """
    normalized = name.lower().strip()
    # Remove common noise characters
    normalized = re.sub(r'[""''\u2018\u2019\u201c\u201d]', '', normalized)
    # Collapse multiple spaces
    normalized = re.sub(r'\s+', ' ', normalized)
    # Remove trailing punctuation
    normalized = re.sub(r'[.,;:!?]+$', '', normalized)
    # Strip dashes between words to a space (for matching "Solutions Architect - Associate" vs "Solutions Architect Associate")
    normalized = re.sub(r'\s*[-–—]\s*', ' ', normalized)
    return normalized.strip()


def _generate_cert_variants(name: str) -> list[str]:
    """
    Generate normalized variants of a certificate name for matching.
    Returns multiple forms to handle common CV writing variations.
    """
    base = _normalize_cert_name(name)
    variants = {base}

    # Extract abbreviation from parentheses: "CKA (Certified Kubernetes Administrator)" → "cka"
    paren_match = re.search(r'\(([^)]+)\)', name)
    if paren_match:
        abbrev = paren_match.group(1).strip().lower()
        variants.add(abbrev)
        # Also add the name without the parenthetical
        without_paren = re.sub(r'\s*\([^)]*\)\s*', ' ', base).strip()
        without_paren = re.sub(r'\s+', ' ', without_paren)
        variants.add(without_paren)

    # If the name starts with an abbreviation like "CKA", add it
    words = base.split()
    if words and len(words[0]) <= 6 and words[0].replace('.', '').isalpha():
        variants.add(words[0])

    # Remove "certified" prefix which CVs sometimes omit
    if base.startswith("certified "):
        variants.add(base[len("certified "):])

    # Remove common filler words for looser matching
    # e.g., "aws certified solutions architect associate" → "aws solutions architect associate"
    no_certified = re.sub(r'\bcertified\b', '', base).strip()
    no_certified = re.sub(r'\s+', ' ', no_certified)
    if no_certified != base:
        variants.add(no_certified)

    return list(variants)


class CertificationIndex:
    """
    Unified certification index built from all role evidence/*/cv.json files.
    Maps normalized cert names → {role_category, signal_mapping info}.
    """

    def __init__(self):
        # {normalized_cert_variant: [{role_category, cert_original_name, category_group}]}
        self._allowlist: dict[str, list[dict[str, Any]]] = {}
        # {role_category: [signal_mapping_patterns_about_certs]}
        self._cert_signal_patterns: dict[str, list[dict[str, Any]]] = {}
        self._built = False

    def build(self, kb: KnowledgeBase) -> None:
        """
        Scan all role evidence/*/cv.json files and build the unified index.
        Expects canonical list format: [{"section": "...", ...}, ...]
        """
        self._allowlist.clear()
        self._cert_signal_patterns.clear()

        for role_category in kb.role_categories:
            cv_evidence = kb.get_evidence_for_role(role_category, "cv")
            if not cv_evidence:
                continue

            sections = cv_evidence.get("extraction_rules", {}).get("sections", [])
            for section in sections:
                if isinstance(section, dict) and section.get("section") == "certifications":
                    recognized = section.get("recognized_certifications")
                    if recognized is not None:
                        if isinstance(recognized, dict):
                            for category_group, cert_names in recognized.items():
                                if isinstance(cert_names, list):
                                    for cert_name in cert_names:
                                        self._index_cert(cert_name, role_category, category_group)
                        elif isinstance(recognized, list):
                            for cert_name in recognized:
                                self._index_cert(cert_name, role_category, "general")
                    break

            # Extract certification-related signal_mapping patterns
            signal_patterns = cv_evidence.get("signal_mapping", {}).get("patterns", [])
            for pattern in signal_patterns:
                pattern_text = pattern.get("pattern", "").lower()
                if "certif" in pattern_text or "cert " in pattern_text:
                    if role_category not in self._cert_signal_patterns:
                        self._cert_signal_patterns[role_category] = []
                    self._cert_signal_patterns[role_category].append(pattern)

        self._built = True
        total_certs = len(set(
            entry["cert_original_name"]
            for entries in self._allowlist.values()
            for entry in entries
        ))
        logger.info(
            f"[CertificationIndex] Built index: {total_certs} unique certs "
            f"across {len(self._cert_signal_patterns)} roles with signal patterns"
        )

    def _index_cert(self, cert_name: str, role_category: str, category_group: str) -> None:
        """Add a certificate to the index under all its normalized variants."""
        entry = {
            "role_category": role_category,
            "cert_original_name": cert_name,
            "category_group": category_group,
        }
        for variant in _generate_cert_variants(cert_name):
            if variant not in self._allowlist:
                self._allowlist[variant] = []
            self._allowlist[variant].append(entry)

    def lookup(self, cert_name: str) -> list[dict[str, Any]] | None:
        """
        Look up a certificate name in the index.
        Returns matching entries or None if not found.
        """
        if not self._built:
            raise RuntimeError("CertificationIndex not built. Call build() first.")

        for variant in _generate_cert_variants(cert_name):
            if variant in self._allowlist:
                return self._allowlist[variant]

        return None

    def get_cert_signal_patterns(self, role_category: str) -> list[dict[str, Any]]:
        """Get certification-related signal_mapping patterns for a role."""
        return self._cert_signal_patterns.get(role_category, [])


class CertificationMatcher:
    """
    Matches CV certificates against the knowledge base certification index.
    Produces three-way classification per the user's specification.
    """

    def __init__(self, kb: KnowledgeBase, cert_index: CertificationIndex, role_category: str):
        self.kb = kb
        self.cert_index = cert_index
        self.role_category = role_category

        # Get the base_strength for certifications from the role's cv.json
        cv_evidence = kb.get_evidence_for_role(role_category, "cv")
        self.cert_base_strength = 0.2  # default from engine.json
        if cv_evidence:
            sections = cv_evidence.get("extraction_rules", {}).get("sections", [])
            for section in sections:
                if isinstance(section, dict) and section.get("section") == "certifications":
                    self.cert_base_strength = float(section.get("base_strength", 0.2))
                    break

        # Cache signal_mapping patterns for this role
        self._cert_patterns = cert_index.get_cert_signal_patterns(role_category)

    def match_certificates(
        self, certificates: list[dict[str, str]]
    ) -> list[dict[str, Any]]:
        """
        Match a list of parsed CV certificates.

        Args:
            certificates: [{"name": "...", "provider": "..."}]

        Returns:
            [{
                "certificate_name": str,
                "classification": "recognized_relevant" | "recognized_no_mapping" | "unrecognized_excluded",
                "matched_composite_keys": [str] | None,
                "score_contribution": float,
                "strength": float,
                "matched_from_role": str | None,
                "category_group": str | None,
            }]
        """
        results: list[dict[str, Any]] = []

        for cert in certificates:
            cert_name = cert.get("name", "").strip()
            if not cert_name:
                continue

            result = self._classify_single(cert_name)
            results.append(result)

        logger.info(
            f"[CertificationMatcher] Matched {len(results)} certs for role '{self.role_category}': "
            f"{sum(1 for r in results if r['classification'] == 'recognized_relevant')} recognized_relevant, "
            f"{sum(1 for r in results if r['classification'] == 'recognized_no_mapping')} recognized_no_mapping, "
            f"{sum(1 for r in results if r['classification'] == 'unrecognized_excluded')} unrecognized_excluded"
        )

        return results

    def _classify_single(self, cert_name: str) -> dict[str, Any]:
        """Classify a single certificate."""
        # Step 1: Look up in the allowlist
        matches = self.cert_index.lookup(cert_name)

        if matches is None:
            # NOT in any role's recognized_certifications
            return {
                "certificate_name": cert_name,
                "classification": "unrecognized_excluded",
                "matched_composite_keys": None,
                "score_contribution": 0.0,
                "strength": 0.0,
                "matched_from_role": None,
                "category_group": None,
            }

        # Step 2: Cert IS in the allowlist. Check if there's a signal_mapping pattern.
        composite_keys = self._find_composite_keys_for_cert(cert_name)

        if composite_keys:
            # recognized_relevant: in allowlist AND has signal_mapping with composite keys
            strength_modifier = self._get_strength_modifier_for_cert(cert_name)
            strength = self.cert_base_strength * strength_modifier
            return {
                "certificate_name": cert_name,
                "classification": "recognized_relevant",
                "matched_composite_keys": composite_keys,
                "score_contribution": round(strength, 4),
                "strength": round(strength, 4),
                "matched_from_role": matches[0]["role_category"],
                "category_group": matches[0].get("category_group"),
            }
        else:
            # recognized_no_mapping: in allowlist but no signal_mapping pattern
            return {
                "certificate_name": cert_name,
                "classification": "recognized_no_mapping",
                "matched_composite_keys": None,
                "score_contribution": 0.0,
                "strength": 0.0,
                "matched_from_role": matches[0]["role_category"],
                "category_group": matches[0].get("category_group"),
            }

    def _find_composite_keys_for_cert(self, cert_name: str) -> list[str]:
        """
        Find composite keys that a recognized cert maps to,
        based on the signal_mapping.patterns in the role's cv.json.
        """
        cert_lower = cert_name.lower()
        cert_normalized = _normalize_cert_name(cert_name)

        for pattern in self._cert_patterns:
            pattern_text = pattern.get("pattern", "").lower()
            maps_to = pattern.get("maps_to", [])

            # Check if the cert name or its normalized form appears in the pattern text
            # or if the pattern is a general certification pattern for this cert's category
            cert_words = cert_normalized.split()
            # Check if at least 2 significant words from the cert name appear in the pattern
            significant_words = [w for w in cert_words if len(w) > 3]
            if significant_words:
                match_count = sum(1 for w in significant_words if w in pattern_text)
                if match_count >= min(2, len(significant_words)):
                    return maps_to

        return []

    def _get_strength_modifier_for_cert(self, cert_name: str) -> float:
        """Get the strength_modifier from the matching signal_mapping pattern."""
        cert_normalized = _normalize_cert_name(cert_name)

        for pattern in self._cert_patterns:
            pattern_text = pattern.get("pattern", "").lower()
            cert_words = cert_normalized.split()
            significant_words = [w for w in cert_words if len(w) > 3]
            if significant_words:
                match_count = sum(1 for w in significant_words if w in pattern_text)
                if match_count >= min(2, len(significant_words)):
                    return float(pattern.get("strength_modifier", 1.0))

        return 1.0


# Singleton index — built once at startup
_cert_index = CertificationIndex()


def get_certification_index() -> CertificationIndex:
    """Get or lazily build the certification index."""
    return _cert_index
