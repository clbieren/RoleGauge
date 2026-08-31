"""
LinkedIn Skill Matcher.
Matches parsed LinkedIn profile data (skills, experience, summary, projects,
recommendations, posts) against knowledge base composite keys for a target role.

Produces 'claimed' status signals — never 'evidence_found'.
Strengths are derived from knowledge-base/evidence/{role}/linkedin.json:
- skills_endorsements: 0.15
- headline_summary: 0.20
- experience: 0.40
- projects: 0.30
- recommendations: 0.30
- posts_articles: 0.30
"""

import logging
import re
from typing import Any

from app.services.evidence_detector import EvidenceSignal, SubskillEvidenceResult
from app.services.kb_loader import KnowledgeBase

logger = logging.getLogger(__name__)


class LinkedInSkillMatcher:
    """
    Matches LinkedIn-extracted skills, experience, summary, projects, recommendations,
    and posts against knowledge base composite keys for a specific role.

    All matches produce status='claimed' (never 'evidence_found').
    Strengths are derived from linkedin.json base_strength × strength_modifier.
    """

    def __init__(self, kb: KnowledgeBase, role_category: str):
        self.kb = kb
        self.role_category = role_category
        self.keywords_map = kb.get_all_keywords_for_role(role_category)

        # Default section strengths according to RoleGauge engine specification
        self._section_strengths: dict[str, float] = {
            "skills_endorsements": 0.15,
            "headline_summary": 0.20,
            "experience": 0.40,
            "projects": 0.30,
            "recommendations": 0.30,
            "certifications": 0.20,
        }

        # Load role-specific evidence from linkedin.json
        linkedin_evidence = kb.get_evidence_for_role(role_category, "linkedin")
        self.signal_patterns: list[dict[str, Any]] = []

        if linkedin_evidence:
            self.signal_patterns = linkedin_evidence.get("signal_mapping", {}).get("patterns", [])
            # Read dynamic section base_strengths from extraction_rules.sections
            # Note: posts_articles is deliberately omitted / inactive
            sections = linkedin_evidence.get("extraction_rules", {}).get("sections", [])
            for section in sections:
                if isinstance(section, dict):
                    section_name = section.get("section", "")
                    if section_name and section_name != "posts_articles":
                        self._section_strengths[section_name] = float(section.get("base_strength", self._section_strengths.get(section_name, 0.2)))

    def match_all(
        self,
        parsed_linkedin: dict[str, Any],
    ) -> dict[str, SubskillEvidenceResult]:
        """
        Run skill matching against the parsed LinkedIn profile data.

        Inputs from parsed_linkedin:
        - skills: list[str] — flat skill / endorsement names
        - experience: list[{raw, title, company, description}]
        - personal_info: {summary, headline, ...}
        - projects: list[{name, description, skills_mentioned}]
        - recommendations: list[{recommender, text}]

        Returns: {composite_key: SubskillEvidenceResult}
        """
        # Initialize empty results for all subskills in the role
        results = self._initialize_results()

        # 1. Match skills_endorsements entries against keywords
        skills_list = parsed_linkedin.get("skills", [])
        self._match_skills_list(skills_list, results)

        # 2. Match experience descriptions & titles against keywords
        experience = parsed_linkedin.get("experience", [])
        self._match_experience(experience, results)

        # 3. Match headline & summary against keywords
        personal_info = parsed_linkedin.get("personal_info", {})
        self._match_summary_and_headline(personal_info, results)

        # 4. Match project mentions & descriptions
        projects = parsed_linkedin.get("projects", [])
        self._match_projects(projects, results)

        # 5. Match recommendations text against keywords
        recommendations = parsed_linkedin.get("recommendations", [])
        self._match_recommendations(recommendations, results)

        # 6. Match signal_mapping.patterns from linkedin.json
        self._match_signal_patterns(parsed_linkedin, results)

        # Update statuses: any result with signals → "claimed"
        for key, result in results.items():
            if result.signals:
                result.status = "claimed"

        found = sum(1 for r in results.values() if r.status == "claimed")
        logger.info(
            f"[LinkedInSkillMatcher] Matched {found}/{len(results)} subskills "
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
        base_strength = self._section_strengths.get("skills_endorsements", 0.15)

        for skill_name in skills:
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
                            source="linkedin_skills",
                            file_path="linkedin/skills",
                            matched_text=skill_name,
                            strength=base_strength,
                        ))
                        break

    def _match_experience(
        self,
        experience: list[dict[str, str]],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match experience descriptions and titles against subskill keywords."""
        base_strength = self._section_strengths.get("experience", 0.40)

        for exp in experience:
            description = exp.get("description", "") or exp.get("raw", "")
            title = exp.get("title", "Unknown Position")
            full_text = f"{title} {description}"

            if full_text.strip():
                self._scan_text_for_keywords(
                    full_text, results,
                    source="linkedin_experience",
                    file_path=f"linkedin/experience/{title}",
                    base_strength=base_strength,
                )

    def _match_summary_and_headline(
        self,
        personal_info: dict[str, str],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match headline and summary against subskill keywords."""
        base_strength = self._section_strengths.get("headline_summary", 0.20)
        summary = personal_info.get("summary", "")
        headline = personal_info.get("headline", "")
        text = f"{headline} {summary}".strip()

        if text:
            self._scan_text_for_keywords(
                text, results,
                source="linkedin_summary",
                file_path="linkedin/summary",
                base_strength=base_strength,
            )

    def _match_projects(
        self,
        projects: list[dict[str, Any]],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match project skills_mentioned and descriptions against subskill keywords."""
        base_strength = self._section_strengths.get("projects", 0.30)

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
                                source="linkedin_project",
                                file_path=f"linkedin/projects/{project_name}",
                                matched_text=f"{skill_name} (in project: {project_name})",
                                strength=base_strength,
                            ))
                            break

            # Also scan project description for keyword mentions
            if description:
                self._scan_text_for_keywords(
                    description, results,
                    source="linkedin_project",
                    file_path=f"linkedin/projects/{project_name}",
                    base_strength=base_strength,
                )

    def _match_recommendations(
        self,
        recommendations: list[dict[str, str]],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """Match recommendations text against subskill keywords."""
        base_strength = self._section_strengths.get("recommendations", 0.30)

        for rec in recommendations:
            recommender = rec.get("recommender", "Peer / Lead")
            text = rec.get("text", "")
            if text:
                self._scan_text_for_keywords(
                    text, results,
                    source="linkedin_recommendation",
                    file_path=f"linkedin/recommendations/{recommender}",
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
                    break

    def _match_signal_patterns(
        self,
        parsed_linkedin: dict[str, Any],
        results: dict[str, SubskillEvidenceResult],
    ) -> None:
        """
        Match LinkedIn profile content against signal_mapping.patterns from linkedin.json.
        Uses base_strength × strength_modifier for signal strength.
        """
        all_skills_text = " ".join(parsed_linkedin.get("skills", []))
        all_project_text = " ".join(
            f"{p.get('name', '')} {p.get('description', '')} {' '.join(p.get('skills_mentioned', []))}"
            for p in parsed_linkedin.get("projects", [])
        )
        all_exp_text = " ".join(
            exp.get("description", "") or exp.get("raw", "") or exp.get("title", "")
            for exp in parsed_linkedin.get("experience", [])
        )
        summary_text = f"{parsed_linkedin.get('personal_info', {}).get('headline', '')} {parsed_linkedin.get('personal_info', {}).get('summary', '')}"
        recs_text = " ".join(r.get("text", "") for r in parsed_linkedin.get("recommendations", []))

        combined_text = f"{all_skills_text} {all_project_text} {all_exp_text} {summary_text} {recs_text}".lower()

        for pattern_info in self.signal_patterns:
            pattern_text = pattern_info.get("pattern", "").lower()
            maps_to = pattern_info.get("maps_to", [])
            strength_modifier = float(pattern_info.get("strength_modifier", 1.0))

            # Skip certification-only patterns (handled by CertificationMatcher)
            if "certification" in pattern_text and "without project" in pattern_text:
                continue

            key_terms = self._extract_key_terms(pattern_text)
            if not key_terms:
                continue

            matches = sum(1 for term in key_terms if term in combined_text)
            if matches >= min(2, len(key_terms)):
                base = self._section_strengths.get("skills_endorsements", 0.15)
                strength = base * strength_modifier

                for composite_key in maps_to:
                    if composite_key in results:
                        results[composite_key].signals.append(EvidenceSignal(
                            source="linkedin_signal_pattern",
                            file_path="linkedin/signal_mapping",
                            matched_text=pattern_info.get("pattern", ""),
                            strength=round(strength, 4),
                        ))

    @staticmethod
    def _extract_key_terms(pattern_text: str) -> list[str]:
        """Extract meaningful technology/concept terms from a signal pattern description."""
        filler = {
            "describes", "mentions", "lists", "has", "built", "building",
            "with", "using", "and", "or", "for", "the", "in", "a", "an",
            "of", "to", "from", "by", "that", "this", "their", "which",
            "only", "also", "without", "project", "evidence", "specific",
            "activities", "section", "experience", "work", "linkedin",
            "skills", "endorsement", "endorsements", "job", "explicitly",
        }
        words = pattern_text.lower().split()
        terms = [w.strip(".,;:()[]'\"") for w in words if w.strip(".,;:()[]'\"") not in filler and len(w) > 2]
        return terms
