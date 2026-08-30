"""
CV Skill Matcher.
Matches parsed CV skills and project mentions against the knowledge base
composite keys for a target role.

Produces 'claimed' status signals — never 'evidence_found'.
Uses the same keyword map and signal_mapping patterns as the existing
EvidenceDetector, but with CV-specific source types and strength rules.
"""

import logging
import re
from typing import Any

from app.services.kb_loader import KnowledgeBase
from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult

logger = logging.getLogger(__name__)


class CVSkillMatcher:
    """
    Matches CV-extracted skills and project mentions against knowledge base
    composite keys for a specific role.

    All matches produce status='claimed' (never 'evidence_found').
    Strengths are derived from cv.json base_strength × strength_modifier.
    """

    def __init__(self, kb: KnowledgeBase, role_category: str):
        self.kb = kb
        self.role_category = role_category
        self.keywords_map = kb.get_all_keywords_for_role(role_category)

        # Load signal_mapping patterns from cv.json
        cv_evidence = kb.get_evidence_for_role(role_category, "cv")
        self.signal_patterns: list[dict[str, Any]] = []
        self._section_strengths: dict[str, float] = {}

        if cv_evidence:
            self.signal_patterns = cv_evidence.get("signal_mapping", {}).get("patterns", [])
            # Cache section base_strengths
            sections = cv_evidence.get("extraction_rules", {}).get("sections", [])
            for section in sections:
                if isinstance(section, dict):
                    section_name = section.get("section", "")
                    if section_name:
                        self._section_strengths[section_name] = float(section.get("base_strength", 0.3))

    def match_all(
        self,
        parsed_cv: dict[str, Any],
    ) -> dict[str, SubskillEvidenceResult]:
        """
        Run skill matching against the parsed CV data.

        Inputs from parsed_cv:
        - skills: list[str] — flat skill names
        - projects: list[{name, description, skills_mentioned}]
        - experience: list[{raw, title, company, description}]

        Returns: {composite_key: SubskillEvidenceResult}
        """
        # Initialize empty results for all subskills in the role
        results = self._initialize_results()

        # 1. Match skills_list entries against keywords
        skills_list = parsed_cv.get("skills", [])
        self._match_skills_list(skills_list, results)

        # 2. Match project skills_mentioned
        projects = parsed_cv.get("projects", [])
        self._match_projects(projects, results)

        # 3. Match experience descriptions against signal_mapping patterns
        experience = parsed_cv.get("experience", [])
        self._match_experience_patterns(experience, results)

        # 4. Match skills_list and project mentions against signal_mapping patterns
        self._match_signal_patterns(parsed_cv, results)

        # Update statuses: any result with signals → "claimed"
        for key, result in results.items():
            if result.signals:
                result.status = "claimed"

        found = sum(1 for r in results.values() if r.status == "claimed")
        logger.info(
            f"[CVSkillMatcher] Matched {found}/{len(results)} subskills "
            f"as 'claimed' for role '{self.role_category}'"
        )

        return results

    def _initialize_results(self) -> dict[str, SubskillEvidenceResult]:
        """Create empty results for all subskills in the role."""
        results: dict[str, SubskillEvidenceResult] = {}
        for skill_id, skill_data in self.kb.get_skills_for_role(self.role_category).items():
            for subskill in skill_data.get("subskills", []):
                composite_key = f"{skill_id}.{subskill['id']}"
                results[composite_key] = SubskillEvidenceResult(
                    composite_key=composite_key,
                    subskill_name=subskill.get("name", subskill["id"]),
                )
        return results

    def _match_skills_list(
        self,
        skills: list[str],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match flat skill names against subskill keywords."""
        base_strength = self._section_strengths.get("skills_list", 0.3)

        for skill_name in skills:
            skill_lower = skill_name.lower().strip()
            if not skill_lower:
                continue

            for composite_key, keywords in self.keywords_map.items():
                if composite_key not in results:
                    continue

                for keyword in keywords:
                    keyword_lower = keyword.lower()
                    # Match if the CV skill is the keyword or contains it
                    if (skill_lower == keyword_lower or
                        keyword_lower in skill_lower or
                        skill_lower in keyword_lower):
                        results[composite_key].signals.append(EvidenceSignal(
                            source="cv_skills_list",
                            file_path="cv/skills",
                            matched_text=skill_name,
                            strength=base_strength,
                        ))
                        break  # One match per keyword set is enough

    def _match_projects(
        self,
        projects: list[dict[str, Any]],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match project skills_mentioned against subskill keywords."""
        base_strength = self._section_strengths.get("projects", 0.4)

        for project in projects:
            project_name = project.get("name", "Unknown Project")
            skills_mentioned = project.get("skills_mentioned", [])
            description = project.get("description", "")

            # Match skills_mentioned against keywords
            for skill_name in skills_mentioned:
                skill_lower = skill_name.lower().strip()
                if not skill_lower:
                    continue

                for composite_key, keywords in self.keywords_map.items():
                    if composite_key not in results:
                        continue

                    for keyword in keywords:
                        keyword_lower = keyword.lower()
                        if (skill_lower == keyword_lower or
                            keyword_lower in skill_lower or
                            skill_lower in keyword_lower):
                            results[composite_key].signals.append(EvidenceSignal(
                                source="cv_project",
                                file_path=f"cv/projects/{project_name}",
                                matched_text=f"{skill_name} (in project: {project_name})",
                                strength=base_strength,
                            ))
                            break

            # Also scan project description for keyword mentions
            if description:
                self._scan_text_for_keywords(
                    description, results,
                    source="cv_project",
                    file_path=f"cv/projects/{project_name}",
                    base_strength=base_strength,
                )

    def _match_experience_patterns(
        self,
        experience: list[dict[str, str]],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match experience descriptions against subskill keywords."""
        base_strength = self._section_strengths.get("work_experience", 0.5)

        for exp in experience:
            description = exp.get("description", "") or exp.get("raw", "")
            title = exp.get("title", "Unknown Position")

            if description:
                self._scan_text_for_keywords(
                    description, results,
                    source="cv_experience",
                    file_path=f"cv/experience/{title}",
                    base_strength=base_strength,
                )

    def _scan_text_for_keywords(
        self,
        text: str,
        results: dict[str, SubskillEvidenceResult],
        source: str,
        file_path: str,
        base_strength: float,
    ) -> None:
        """Scan a text block for subskill keyword matches."""
        for composite_key, keywords in self.keywords_map.items():
            if composite_key not in results:
                continue

            for keyword in keywords:
                if len(keyword) <= 3:
                    pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')
                else:
                    pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)

                if pattern.search(text):
                    results[composite_key].signals.append(EvidenceSignal(
                        source=source,
                        file_path=file_path,
                        matched_text=keyword,
                        strength=base_strength,
                    ))
                    break  # One keyword match per composite_key per text block

    def _match_signal_patterns(
        self,
        parsed_cv: dict[str, Any],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """
        Match CV content against signal_mapping.patterns from cv.json.
        Uses base_strength × strength_modifier for signal strength.
        """
        # Build a combined text from skills, projects, and experience
        all_skills_text = " ".join(parsed_cv.get("skills", []))
        all_project_text = " ".join(
            f"{p.get('name', '')} {p.get('description', '')} {' '.join(p.get('skills_mentioned', []))}"
            for p in parsed_cv.get("projects", [])
        )
        all_exp_text = " ".join(
            exp.get("description", "") or exp.get("raw", "")
            for exp in parsed_cv.get("experience", [])
        )
        combined_text = f"{all_skills_text} {all_project_text} {all_exp_text}".lower()

        for pattern_info in self.signal_patterns:
            pattern_text = pattern_info.get("pattern", "").lower()
            maps_to = pattern_info.get("maps_to", [])
            strength_modifier = float(pattern_info.get("strength_modifier", 1.0))

            # Skip certification-only patterns (handled by CertificationMatcher)
            if "certification" in pattern_text and "without project" in pattern_text:
                continue

            # Extract key phrases from the pattern for matching
            # Look for technology/concept mentions in the pattern
            key_terms = self._extract_key_terms(pattern_text)

            if not key_terms:
                continue

            # Check if enough key terms appear in the combined CV text
            matches = sum(1 for term in key_terms if term in combined_text)
            if matches >= min(2, len(key_terms)):
                base = self._section_strengths.get("skills_list", 0.3)
                strength = base * strength_modifier

                for composite_key in maps_to:
                    if composite_key in results:
                        results[composite_key].signals.append(EvidenceSignal(
                            source="cv_signal_pattern",
                            file_path="cv/signal_mapping",
                            matched_text=pattern_info.get("pattern", ""),
                            strength=round(strength, 4),
                        ))

    @staticmethod
    def _extract_key_terms(pattern_text: str) -> list[str]:
        """Extract meaningful technology/concept terms from a signal pattern description."""
        # Remove filler words
        filler = {
            "describes", "mentions", "lists", "has", "built", "building",
            "with", "using", "and", "or", "for", "the", "in", "a", "an",
            "of", "to", "from", "by", "that", "this", "their", "which",
            "only", "also", "without", "project", "evidence", "specific",
            "activities", "section", "experience", "work",
        }
        words = pattern_text.lower().split()
        terms = [w.strip(".,;:()[]") for w in words if w.strip(".,;:()[]") not in filler and len(w) > 2]
        return terms
