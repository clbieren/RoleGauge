"""
Knowledge Base Loader.
Reads and caches all JSON files from the knowledge-base directory.
Provides structured access to skills, evidence, roles, and scoring configuration.
"""

import json
import os
import logging
from typing import Any
from functools import lru_cache

from app.config import settings

logger = logging.getLogger(__name__)


class KnowledgeBase:
    """In-memory representation of the entire knowledge base."""

    def __init__(self):
        self.skills: dict[str, dict[str, Any]] = {}       # {role_category: {skill_id: skill_data}}
        self.evidence: dict[str, dict[str, Any]] = {}     # {role_category: {source_id: evidence_data}}
        self.roles: dict[str, dict[str, Any]] = {}        # {role_category: {level: role_data}}
        self.scoring_engine: dict[str, Any] = {}           # engine.json
        self._role_categories: list[str] = []

    def load(self, kb_path: str | None = None):
        """Load all knowledge base files from disk."""
        base_path = kb_path or settings.KB_PATH
        logger.info(f"Loading knowledge base from: {base_path}")

        # Load scoring engine
        engine_path = os.path.join(base_path, "scoring", "engine.json")
        if os.path.exists(engine_path):
            self.scoring_engine = self._load_json(engine_path)
            logger.info("Loaded scoring engine configuration")

        # Discover role categories
        skills_dir = os.path.join(base_path, "skills")
        if os.path.isdir(skills_dir):
            self._role_categories = [
                d for d in os.listdir(skills_dir)
                if os.path.isdir(os.path.join(skills_dir, d))
            ]

        for category in self._role_categories:
            self._load_skills(base_path, category)
            self._load_evidence(base_path, category)
            self._load_roles(base_path, category)

        logger.info(
            f"Knowledge base loaded: {len(self._role_categories)} roles, "
            f"{sum(len(s) for s in self.skills.values())} skills"
        )

    def _load_skills(self, base_path: str, category: str):
        """Load all skill definitions for a role category."""
        skills_dir = os.path.join(base_path, "skills", category)
        if not os.path.isdir(skills_dir):
            return

        self.skills[category] = {}
        for filename in os.listdir(skills_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(skills_dir, filename)
                data = self._load_json(filepath)
                if data and "skill_id" in data:
                    self.skills[category][data["skill_id"]] = data

    def _load_evidence(self, base_path: str, category: str):
        """Load all evidence source definitions for a role category."""
        evidence_dir = os.path.join(base_path, "evidence", category)
        if not os.path.isdir(evidence_dir):
            return

        self.evidence[category] = {}
        for filename in os.listdir(evidence_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(evidence_dir, filename)
                data = self._load_json(filepath)
                if data:
                    # Use filename stem as key (e.g. "github", "cv", "linkedin")
                    source_key = os.path.splitext(filename)[0]
                    self.evidence[category][source_key] = data

    def _load_roles(self, base_path: str, category: str):
        """Load role level definitions (junior, mid, senior)."""
        roles_dir = os.path.join(base_path, "roles", category)
        if not os.path.isdir(roles_dir):
            return

        self.roles[category] = {}
        for filename in os.listdir(roles_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(roles_dir, filename)
                data = self._load_json(filepath)
                if data and "level" in data:
                    self.roles[category][data["level"]] = data

    @staticmethod
    def _load_json(filepath: str) -> dict[str, Any]:
        """Read and parse a JSON file."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logger.error(f"Failed to load {filepath}: {e}")
            return {}

    @property
    def role_categories(self) -> list[str]:
        """List of all available role categories."""
        return self._role_categories

    def get_role(self, category: str, level: str) -> dict[str, Any] | None:
        """Get a specific role definition."""
        return self.roles.get(category, {}).get(level)

    def get_skills_for_role(self, category: str) -> dict[str, Any]:
        """Get all skill definitions for a role category."""
        return self.skills.get(category, {})

    def get_evidence_for_role(self, category: str, source: str = "github") -> dict[str, Any] | None:
        """Get evidence source definition for a role category."""
        return self.evidence.get(category, {}).get(source)

    def get_subskills_for_level(self, category: str, skill_id: str, level: str) -> dict[str, list[str]]:
        """
        Get expected and bonus subskills for a given skill and level.
        Returns: {"expected": [...], "bonus": [...]}
        """
        skill_data = self.skills.get(category, {}).get(skill_id)
        if not skill_data or "levels" not in skill_data:
            return {"expected": [], "bonus": []}

        levels_order = ["junior", "mid", "senior"]
        target_idx = levels_order.index(level) if level in levels_order else 0

        expected = []
        bonus = []

        for lvl_name, lvl_data in skill_data["levels"].items():
            lvl_idx = levels_order.index(lvl_name) if lvl_name in levels_order else 0
            subskills = lvl_data.get("expected_subskills", [])

            if lvl_idx <= target_idx:
                expected.extend(subskills)
            else:
                bonus.extend(subskills)

        return {"expected": expected, "bonus": bonus}

    def get_all_keywords_for_role(self, category: str) -> dict[str, list[str]]:
        """
        Build a mapping of composite_key → keywords for all subskills in a role.
        Returns: {"skill_id.subskill_id": ["keyword1", "keyword2", ...], ...}
        """
        keywords_map: dict[str, list[str]] = {}
        for skill_id, skill_data in self.skills.get(category, {}).items():
            for subskill in skill_data.get("subskills", []):
                composite_key = f"{skill_id}.{subskill['id']}"
                keywords_map[composite_key] = subskill.get("keywords", [])
        return keywords_map

    def get_evidence_patterns_for_role(self, category: str) -> list[dict[str, Any]]:
        """
        Get all GitHub evidence patterns from skill files for a role.
        Returns list of signal objects with pattern, strength, and maps_to.
        """
        patterns = []
        for skill_id, skill_data in self.skills.get(category, {}).items():
            github_evidence = skill_data.get("evidence", {}).get("github", [])
            for signal in github_evidence:
                patterns.append({
                    "signal": signal.get("signal", ""),
                    "detection": signal.get("detection", "content_analysis"),
                    "pattern": signal.get("pattern", ""),
                    "strength": signal.get("strength", 0.5),
                    "maps_to": signal.get("maps_to", []),
                })
        return patterns

    def get_file_tree_patterns(self, category: str) -> list[dict[str, Any]]:
        """
        Get file tree scan patterns from evidence/{category}/github.json.
        These define which files to look for in repositories.
        """
        github_evidence = self.get_evidence_for_role(category, "github")
        if not github_evidence:
            return []

        pipeline = github_evidence.get("preprocessing_pipeline", {})
        steps = pipeline.get("steps", [])

        for step in steps:
            if step.get("name") == "file_tree_scan":
                return step.get("target_files", [])

        return []

    def get_relevant_dependencies(self, category: str) -> dict[str, list[str]]:
        """
        Get relevant dependencies mapping from evidence/{category}/github.json.
        Returns: {"skill_id": ["dep1", "dep2", ...], ...}
        """
        github_evidence = self.get_evidence_for_role(category, "github")
        if not github_evidence:
            return {}

        pipeline = github_evidence.get("preprocessing_pipeline", {})
        steps = pipeline.get("steps", [])

        for step in steps:
            if step.get("name") == "dependency_extraction":
                return step.get("relevant_dependencies", {})

        return {}


# Singleton instance
kb = KnowledgeBase()
