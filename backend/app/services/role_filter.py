"""
Role-Based Filter.
Filters raw GitHub data to keep only files and dependencies relevant
to the selected role, based on evidence/{role}/github.json pipeline config.
"""

import fnmatch
import logging
import re
from typing import Any
from dataclasses import dataclass, field

from app.services.github_fetcher import FetchedRepo
from app.services.kb_loader import KnowledgeBase

logger = logging.getLogger(__name__)


@dataclass
class FilteredRepo:
    """A repository with only role-relevant data retained."""
    repo_name: str
    full_name: str
    url: str
    description: str | None = None
    primary_language: str | None = None
    languages: dict[str, int] = field(default_factory=dict)
    stars: int = 0
    forks: int = 0
    topics: list[str] = field(default_factory=list)
    is_relevant: bool = False
    relevance_reasons: list[str] = field(default_factory=list)

    # Filtered data — only role-relevant items
    relevant_files: list[str] = field(default_factory=list)       # File paths matching patterns
    matched_patterns: dict[str, list[str]] = field(default_factory=dict)  # {skill: [matched_files]}
    readme_content: str | None = None
    dependency_files: dict[str, str] = field(default_factory=dict)
    relevant_dependencies: dict[str, list[str]] = field(default_factory=dict)  # {skill: [dep_names]}
    file_contents: dict[str, str] = field(default_factory=dict)  # Contents to send to AI


class RoleFilter:
    """Filters raw GitHub data based on the selected role's evidence configuration."""

    def __init__(self, kb: KnowledgeBase, role_category: str):
        self.kb = kb
        self.role_category = role_category
        self.file_patterns = kb.get_file_tree_patterns(role_category)
        self.dep_mapping = kb.get_relevant_dependencies(role_category)

    def filter_repos(self, repos: list[FetchedRepo]) -> list[FilteredRepo]:
        """
        Filter a list of fetched repos, keeping only role-relevant data.
        Returns FilteredRepo objects sorted by relevance.
        """
        filtered = []
        for repo in repos:
            f_repo = self._filter_single_repo(repo)
            filtered.append(f_repo)

        # Sort: relevant repos first, then by number of relevant files
        filtered.sort(key=lambda r: (r.is_relevant, len(r.relevant_files)), reverse=True)
        return filtered

    def _filter_single_repo(self, repo: FetchedRepo) -> FilteredRepo:
        """Filter a single repo's data to keep only role-relevant items."""
        f_repo = FilteredRepo(
            repo_name=repo.metadata.name,
            full_name=repo.metadata.full_name,
            url=repo.metadata.url,
            description=repo.metadata.description,
            primary_language=repo.metadata.primary_language,
            languages=repo.metadata.languages,
            stars=repo.metadata.stars,
            forks=repo.metadata.forks,
            topics=repo.metadata.topics,
            readme_content=repo.readme_content,
        )

        # 1. Match file tree against role patterns
        self._match_file_patterns(repo.file_tree, f_repo)

        # 2. Match dependencies against relevant dependency lists
        self._match_dependencies(repo.dependency_files, f_repo)

        # 3. Check topics/description for role relevance
        self._check_topic_relevance(f_repo)

        # 4. Determine overall relevance
        f_repo.is_relevant = (
            len(f_repo.relevant_files) > 0
            or len(f_repo.relevant_dependencies) > 0
            or len(f_repo.relevance_reasons) > 0
        )

        return f_repo

    def _match_file_patterns(self, file_tree: list[str], f_repo: FilteredRepo):
        """Match file paths in the tree against role-specific patterns."""
        for file_path in file_tree:
            filename = file_path.split("/")[-1]
            dir_path = file_path.rsplit("/", 1)[0] if "/" in file_path else ""

            for pattern_config in self.file_patterns:
                raw_pattern = pattern_config.get("pattern", "")
                skill = pattern_config.get("skill") or pattern_config.get("skills", ["unknown"])[0] if isinstance(pattern_config.get("skills"), list) else pattern_config.get("skill", "unknown")

                # Split compound patterns (pipe-separated)
                patterns = [p.strip() for p in raw_pattern.split("|")]

                for pattern in patterns:
                    if self._matches_pattern(file_path, filename, dir_path, pattern):
                        f_repo.relevant_files.append(file_path)
                        if skill not in f_repo.matched_patterns:
                            f_repo.matched_patterns[skill] = []
                        f_repo.matched_patterns[skill].append(file_path)
                        break  # Don't double-count same file for same pattern group

        # Deduplicate
        f_repo.relevant_files = list(set(f_repo.relevant_files))

    @staticmethod
    def _matches_pattern(file_path: str, filename: str, dir_path: str, pattern: str) -> bool:
        """Check if a file matches a glob-like or regex-like pattern."""
        pattern = pattern.strip()

        # Directory pattern (ends with /)
        if pattern.endswith("/"):
            dir_name = pattern.rstrip("/")
            return dir_name in file_path.split("/")

        # Glob with wildcards
        if "*" in pattern or "?" in pattern:
            # Try matching against filename
            if fnmatch.fnmatch(filename, pattern):
                return True
            # Try matching against full path
            if fnmatch.fnmatch(file_path, pattern):
                return True
            return False

        # Regex pattern (contains backslashes indicating escaped chars)
        if "\\" in pattern:
            try:
                return bool(re.search(pattern, file_path))
            except re.error:
                return False

        # Exact filename match
        if pattern == filename:
            return True

        # Substring match for directory names
        if "/" not in pattern and pattern in file_path:
            return True

        return False

    def _match_dependencies(self, dependency_files: dict[str, str], f_repo: FilteredRepo):
        """Match extracted dependencies against role-relevant dependency lists."""
        for dep_path, content in dependency_files.items():
            f_repo.dependency_files[dep_path] = content

            # Check each dependency category
            for skill_key, dep_list in self.dep_mapping.items():
                for dep_name in dep_list:
                    dep_lower = dep_name.lower()
                    if dep_lower in content.lower():
                        if skill_key not in f_repo.relevant_dependencies:
                            f_repo.relevant_dependencies[skill_key] = []
                        if dep_name not in f_repo.relevant_dependencies[skill_key]:
                            f_repo.relevant_dependencies[skill_key].append(dep_name)
                            f_repo.relevance_reasons.append(f"Dependency '{dep_name}' -> {skill_key}")

    def _check_topic_relevance(self, f_repo: FilteredRepo):
        """Check repo topics and description for role-relevant keywords."""
        # Build a set of role-relevant terms from KB
        role_terms = set()

        # Add terms from file patterns
        for pattern_config in self.file_patterns:
            notes = pattern_config.get("notes", "")
            if notes:
                for word in notes.lower().split():
                    if len(word) > 3:
                        role_terms.add(word)

        # Check topics
        for topic in f_repo.topics:
            topic_lower = topic.lower()
            # Common game dev topics
            game_terms = {"game", "gamedev", "unity", "unreal", "godot", "game-engine", "gaming"}
            if topic_lower in game_terms or topic_lower in role_terms:
                f_repo.relevance_reasons.append(f"Topic: {topic}")

        # Check description
        if f_repo.description:
            desc_lower = f_repo.description.lower()
            for term in ["game", "api", "backend", "frontend", "devops", "ml", "data"]:
                if term in desc_lower and term in str(self.role_category).lower():
                    f_repo.relevance_reasons.append(f"Description mentions: {term}")

    def get_files_to_fetch_content(self, filtered_repos: list[FilteredRepo], max_files: int = 50) -> dict[str, list[str]]:
        """
        Determine which files need their content fetched for deeper analysis.
        Returns: {full_name: [file_paths]}
        """
        files_to_fetch: dict[str, list[str]] = {}
        total = 0

        for repo in filtered_repos:
            if not repo.is_relevant:
                continue

            repo_files = []
            for file_path in repo.relevant_files:
                if total >= max_files:
                    break

                # Skip binary/asset files
                ext = file_path.rsplit(".", 1)[-1].lower() if "." in file_path else ""
                binary_exts = {
                    "png", "jpg", "jpeg", "gif", "bmp", "ico", "svg",
                    "mp3", "wav", "ogg", "mp4", "avi", "mov",
                    "fbx", "obj", "blend", "3ds", "dae",
                    "zip", "tar", "gz", "rar", "7z",
                    "dll", "so", "exe", "bin",
                    "ttf", "otf", "woff", "woff2",
                    "pdf", "doc", "docx",
                }
                if ext in binary_exts:
                    continue

                repo_files.append(file_path)
                total += 1

            if repo_files:
                files_to_fetch[repo.full_name] = repo_files

        return files_to_fetch
