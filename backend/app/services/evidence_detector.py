"""
Evidence Detector.
Detects evidence of subskill usage in filtered repository data.
Two modes: keyword-based (fast, no AI) and AI-assisted (deeper analysis).
Outputs composite_key → evidence mapping that feeds into the Scoring Engine.
"""

import logging
import re
from typing import Any, Optional
from dataclasses import dataclass, field

from app.services.kb_loader import KnowledgeBase
from app.services.role_filter import FilteredRepo

logger = logging.getLogger(__name__)


@dataclass
class EvidenceSignal:
    """A single piece of evidence for a subskill."""
    source: str          # "file_presence" | "content_match" | "dependency" | "readme" | "ai"
    file_path: str       # Where the evidence was found
    matched_text: str    # What was matched (keyword, pattern, etc.)
    strength: float      # Signal strength (0.0 - 1.0)


@dataclass
class SubskillEvidenceResult:
    """Aggregated evidence for a single subskill (composite key)."""
    composite_key: str
    subskill_name: str
    status: str = "not_yet_evidenced"  # evidence_found | claimed | not_yet_evidenced | verified_gap
    signals: list[EvidenceSignal] = field(default_factory=list)
    contributing_sources: list[dict[str, Any]] = field(default_factory=list)
    ceiling_applied: Optional[str] = None
    calculation_trace: Optional[str] = None

    @property
    def max_strength(self) -> float:
        """Highest signal strength found."""
        if not self.signals:
            return 0.0
        return max(s.strength for s in self.signals)

    @property
    def evidence_sources(self) -> list[str]:
        """Human-readable list of evidence sources."""
        sources = []
        for s in self.signals:
            if s.file_path and s.matched_text:
                sources.append(f"{s.file_path} -> {s.matched_text}")
            elif s.file_path:
                sources.append(s.file_path)
            else:
                sources.append(s.matched_text)
        return sources


class EvidenceDetector:
    """
    Detects evidence of subskill usage in filtered repository data.
    Uses keyword matching from skill JSON definitions and evidence patterns.
    """

    def __init__(self, kb: KnowledgeBase, role_category: str):
        self.kb = kb
        self.role_category = role_category
        self.keywords_map = kb.get_all_keywords_for_role(role_category)
        self.evidence_patterns = kb.get_evidence_patterns_for_role(role_category)

    def detect_all(self, filtered_repos: list[FilteredRepo]) -> dict[str, SubskillEvidenceResult]:
        """
        Run evidence detection across all filtered repos.
        Returns: {composite_key: SubskillEvidenceResult}
        """
        # Initialize results for ALL subskills
        results = self._initialize_results()

        for repo in filtered_repos:
            if not repo.is_relevant:
                continue

            # 1. File presence detection (patterns from evidence config)
            self._detect_file_presence(repo, results)

            # 2. Content keyword matching (from skill definitions)
            self._detect_keyword_matches(repo, results)

            # 3. Dependency-based evidence
            self._detect_dependency_evidence(repo, results)

            # 4. README content analysis
            self._detect_readme_evidence(repo, results)

        # Update statuses
        for key, result in results.items():
            if result.signals:
                result.status = "evidence_found"

        found = sum(1 for r in results.values() if r.status == "evidence_found")
        logger.info(f"Evidence detection complete: {found}/{len(results)} subskills evidenced")

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

    def _detect_file_presence(self, repo: FilteredRepo, results: dict[str, SubskillEvidenceResult]):
        """Detect evidence from file presence patterns in evidence config."""
        for pattern_info in self.evidence_patterns:
            detection_type = pattern_info.get("detection", "content_analysis")
            if detection_type != "file_presence":
                continue

            pattern = pattern_info.get("pattern", "")
            strength = pattern_info.get("strength", 0.5)
            maps_to = pattern_info.get("maps_to", [])

            # Check if any relevant files match this pattern
            sub_patterns = [p.strip() for p in pattern.split("|")]
            for file_path in repo.relevant_files:
                filename = file_path.split("/")[-1]
                for sub_pat in sub_patterns:
                    matched = False
                    if "*" in sub_pat:
                        # Glob pattern
                        import fnmatch
                        matched = fnmatch.fnmatch(filename, sub_pat) or fnmatch.fnmatch(file_path, sub_pat)
                    elif sub_pat.endswith("/"):
                        matched = sub_pat.rstrip("/") in file_path.split("/")
                    else:
                        matched = sub_pat in file_path

                    if matched:
                        for composite_key in maps_to:
                            if composite_key in results:
                                results[composite_key].signals.append(EvidenceSignal(
                                    source="file_presence",
                                    file_path=f"{repo.repo_name}/{file_path}",
                                    matched_text=sub_pat,
                                    strength=strength,
                                ))
                        break

    def _detect_keyword_matches(self, repo: FilteredRepo, results: dict[str, SubskillEvidenceResult]):
        """Detect evidence by matching keywords in file contents."""
        for file_path, content in repo.file_contents.items():
            if not content:
                continue

            for composite_key, keywords in self.keywords_map.items():
                if composite_key not in results:
                    continue

                for keyword in keywords:
                    # Case-insensitive search, but respect casing for short keywords
                    if len(keyword) <= 3:
                        # Short keywords: exact match (case-sensitive)
                        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')
                    else:
                        # Longer keywords: case-insensitive
                        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)

                    if pattern.search(content):
                        results[composite_key].signals.append(EvidenceSignal(
                            source="content_match",
                            file_path=f"{repo.repo_name}/{file_path}",
                            matched_text=keyword,
                            strength=0.6,  # Default content match strength
                        ))

        # Also check for content_analysis patterns from evidence config
        for pattern_info in self.evidence_patterns:
            detection_type = pattern_info.get("detection", "content_analysis")
            if detection_type != "content_analysis":
                continue

            pattern_str = pattern_info.get("pattern", "")
            strength = pattern_info.get("strength", 0.5)
            maps_to = pattern_info.get("maps_to", [])

            sub_patterns = [p.strip() for p in pattern_str.split("|")]

            for file_path, content in repo.file_contents.items():
                if not content:
                    continue

                for sub_pat in sub_patterns:
                    try:
                        if re.search(sub_pat, content, re.IGNORECASE):
                            for composite_key in maps_to:
                                if composite_key in results:
                                    results[composite_key].signals.append(EvidenceSignal(
                                        source="content_match",
                                        file_path=f"{repo.repo_name}/{file_path}",
                                        matched_text=sub_pat,
                                        strength=strength,
                                    ))
                            break  # One match per file per pattern group is enough
                    except re.error:
                        continue

    def _detect_dependency_evidence(self, repo: FilteredRepo, results: dict[str, SubskillEvidenceResult]):
        """Detect evidence from matched dependencies."""
        for skill_key, dep_names in repo.relevant_dependencies.items():
            for dep_name in dep_names:
                # Find which composite keys this dependency maps to
                # We need to look at the evidence patterns to find the right mapping
                matching_keys = self._find_composite_keys_for_skill(skill_key)
                for composite_key in matching_keys:
                    if composite_key in results:
                        results[composite_key].signals.append(EvidenceSignal(
                            source="dependency",
                            file_path=f"{repo.repo_name}/dependency",
                            matched_text=dep_name,
                            strength=0.5,
                        ))

    def _detect_readme_evidence(self, repo: FilteredRepo, results: dict[str, SubskillEvidenceResult]):
        """Detect evidence from README content using keywords."""
        if not repo.readme_content:
            return

        readme = repo.readme_content
        for composite_key, keywords in self.keywords_map.items():
            if composite_key not in results:
                continue

            for keyword in keywords:
                if len(keyword) <= 3:
                    pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')
                else:
                    pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)

                if pattern.search(readme):
                    results[composite_key].signals.append(EvidenceSignal(
                        source="readme",
                        file_path=f"{repo.repo_name}/README.md",
                        matched_text=keyword,
                        strength=0.3,  # README mentions are weaker evidence
                    ))

    def _find_composite_keys_for_skill(self, skill_key: str) -> list[str]:
        """Find all composite keys that belong to a skill."""
        return [
            key for key in self.keywords_map.keys()
            if key.startswith(f"{skill_key}.")
        ]
