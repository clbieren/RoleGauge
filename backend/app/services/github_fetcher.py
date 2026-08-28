"""
GitHub REST API Fetcher.
Fetches public repository data for a given GitHub username.
Handles rate limiting, pagination, and content extraction.
"""

import base64
import logging
import re
from typing import Any
from dataclasses import dataclass, field

import httpx

from app.config import settings

logger = logging.getLogger(__name__)


@dataclass
class RepoMetadata:
    """Parsed repository metadata from GitHub API."""
    name: str
    full_name: str
    url: str
    description: str | None = None
    primary_language: str | None = None
    languages: dict[str, int] = field(default_factory=dict)
    stars: int = 0
    forks: int = 0
    topics: list[str] = field(default_factory=list)
    created_at: str | None = None
    pushed_at: str | None = None
    default_branch: str = "main"
    is_fork: bool = False
    size: int = 0  # KB


@dataclass
class FetchedRepo:
    """Complete fetched data for a single repository."""
    metadata: RepoMetadata
    file_tree: list[str] = field(default_factory=list)       # All file paths in repo
    readme_content: str | None = None
    file_contents: dict[str, str] = field(default_factory=dict)  # {path: content}
    dependency_files: dict[str, str] = field(default_factory=dict)  # {filename: content}


class GitHubFetcher:
    """Async GitHub REST API client for fetching public repository data."""

    DEPENDENCY_FILES = [
        "package.json", "pom.xml", "build.gradle", "build.gradle.kts",
        "requirements.txt", "pyproject.toml", "setup.py", "Pipfile",
        "go.mod", "Cargo.toml", "Gemfile", "composer.json",
        "Packages/manifest.json",  # Unity
        "project.godot",  # Godot
    ]

    def __init__(self, token: str | None = None):
        self.token = token or settings.GITHUB_TOKEN
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "RoleGauge/0.1",
        }
        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"

        self._rate_remaining: int = -1
        self._rate_limit: int = -1

    async def fetch_user_repos(self, username: str) -> list[FetchedRepo]:
        """
        Fetch all public repositories for a user and their detailed data.
        Returns a list of FetchedRepo objects with metadata, file trees, READMEs, etc.
        """
        async with httpx.AsyncClient(
            base_url=settings.GITHUB_API_BASE,
            headers=self.headers,
            timeout=30.0,
        ) as client:
            # Step 1: Get repo list
            repos_meta = await self._fetch_repo_list(client, username)
            logger.info(f"Found {len(repos_meta)} repos for {username}")

            # Step 2: Fetch details for each repo
            fetched_repos = []
            for meta in repos_meta:
                if self._rate_remaining == 0:
                    logger.warning("GitHub API rate limit reached, stopping.")
                    break

                try:
                    repo = await self._fetch_repo_details(client, meta)
                    fetched_repos.append(repo)
                except Exception as e:
                    logger.error(f"Failed to fetch details for {meta.full_name}: {e}")
                    # Still include with just metadata
                    fetched_repos.append(FetchedRepo(metadata=meta))

            return fetched_repos

    async def _fetch_repo_list(self, client: httpx.AsyncClient, username: str) -> list[RepoMetadata]:
        """Fetch paginated list of public repos."""
        repos: list[RepoMetadata] = []
        page = 1
        per_page = 100

        while len(repos) < settings.GITHUB_MAX_REPOS:
            response = await client.get(
                f"/users/{username}/repos",
                params={
                    "type": "owner",
                    "sort": "updated",
                    "direction": "desc",
                    "per_page": per_page,
                    "page": page,
                },
            )
            self._update_rate_info(response)

            if response.status_code == 404:
                raise ValueError(f"GitHub user '{username}' not found")
            response.raise_for_status()

            data = response.json()
            if not data:
                break

            for repo in data:
                if repo.get("private"):
                    continue
                repos.append(RepoMetadata(
                    name=repo["name"],
                    full_name=repo["full_name"],
                    url=repo["html_url"],
                    description=repo.get("description"),
                    primary_language=repo.get("language"),
                    stars=repo.get("stargazers_count", 0),
                    forks=repo.get("forks_count", 0),
                    topics=repo.get("topics", []),
                    created_at=repo.get("created_at"),
                    pushed_at=repo.get("pushed_at"),
                    default_branch=repo.get("default_branch", "main"),
                    is_fork=repo.get("fork", False),
                    size=repo.get("size", 0),
                ))

            if len(data) < per_page:
                break
            page += 1

        return repos[:settings.GITHUB_MAX_REPOS]

    async def _fetch_repo_details(self, client: httpx.AsyncClient, meta: RepoMetadata) -> FetchedRepo:
        """Fetch detailed data for a single repo: file tree, README, languages."""
        repo = FetchedRepo(metadata=meta)

        # Fetch languages
        repo.metadata.languages = await self._fetch_languages(client, meta.full_name)

        # Fetch file tree
        repo.file_tree = await self._fetch_file_tree(client, meta.full_name, meta.default_branch)

        # Fetch README
        repo.readme_content = await self._fetch_readme(client, meta.full_name)

        # Fetch dependency files (only if they exist in the file tree)
        for dep_file in self.DEPENDENCY_FILES:
            matching_paths = [p for p in repo.file_tree if p.endswith(dep_file)]
            for path in matching_paths[:2]:  # Max 2 matches per dep type
                content = await self._fetch_file_content(client, meta.full_name, path)
                if content:
                    repo.dependency_files[path] = content

        return repo

    async def _fetch_languages(self, client: httpx.AsyncClient, full_name: str) -> dict[str, int]:
        """Fetch language distribution for a repo."""
        try:
            response = await client.get(f"/repos/{full_name}/languages")
            self._update_rate_info(response)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            logger.warning(f"Failed to fetch languages for {full_name}: {e}")
        return {}

    async def _fetch_file_tree(self, client: httpx.AsyncClient, full_name: str, branch: str) -> list[str]:
        """Fetch recursive file tree using Git Trees API."""
        try:
            response = await client.get(
                f"/repos/{full_name}/git/trees/{branch}",
                params={"recursive": "1"},
            )
            self._update_rate_info(response)

            if response.status_code == 200:
                data = response.json()
                return [
                    item["path"]
                    for item in data.get("tree", [])
                    if item.get("type") == "blob"
                ]
        except Exception as e:
            logger.warning(f"Failed to fetch file tree for {full_name}: {e}")
        return []

    async def _fetch_readme(self, client: httpx.AsyncClient, full_name: str) -> str | None:
        """Fetch and decode README content."""
        try:
            response = await client.get(f"/repos/{full_name}/readme")
            self._update_rate_info(response)

            if response.status_code == 200:
                data = response.json()
                content = data.get("content", "")
                encoding = data.get("encoding", "base64")
                if encoding == "base64" and content:
                    return base64.b64decode(content).decode("utf-8", errors="replace")
        except Exception as e:
            logger.warning(f"Failed to fetch README for {full_name}: {e}")
        return None

    async def _fetch_file_content(self, client: httpx.AsyncClient, full_name: str, path: str) -> str | None:
        """Fetch and decode a single file's content."""
        try:
            response = await client.get(f"/repos/{full_name}/contents/{path}")
            self._update_rate_info(response)

            if response.status_code == 200:
                data = response.json()
                size = data.get("size", 0)
                if size > settings.GITHUB_MAX_FILE_SIZE:
                    logger.info(f"Skipping {path} in {full_name}: too large ({size} bytes)")
                    return None

                content = data.get("content", "")
                encoding = data.get("encoding", "base64")
                if encoding == "base64" and content:
                    return base64.b64decode(content).decode("utf-8", errors="replace")
        except Exception as e:
            logger.warning(f"Failed to fetch {path} in {full_name}: {e}")
        return None

    async def fetch_specific_files(
        self,
        full_name: str,
        file_paths: list[str],
    ) -> dict[str, str]:
        """
        Fetch content for specific files from a repo.
        Used after filtering to get content of relevant files for AI analysis.
        """
        results: dict[str, str] = {}
        async with httpx.AsyncClient(
            base_url=settings.GITHUB_API_BASE,
            headers=self.headers,
            timeout=30.0,
        ) as client:
            for path in file_paths:
                if self._rate_remaining == 0:
                    logger.warning("Rate limit reached during file fetch")
                    break
                content = await self._fetch_file_content(client, full_name, path)
                if content:
                    results[path] = content
        return results

    def _update_rate_info(self, response: httpx.Response):
        """Update rate limit tracking from response headers."""
        remaining = response.headers.get("X-RateLimit-Remaining")
        limit = response.headers.get("X-RateLimit-Limit")
        if remaining:
            self._rate_remaining = int(remaining)
        if limit:
            self._rate_limit = int(limit)

    @property
    def rate_info(self) -> dict[str, int]:
        return {"remaining": self._rate_remaining, "limit": self._rate_limit}


def extract_username(input_str: str) -> str:
    """
    Extract GitHub username from various input formats:
    - "username"
    - "https://github.com/username"
    - "github.com/username"
    - "https://github.com/username/"
    """
    input_str = input_str.strip().rstrip("/")

    # URL pattern
    match = re.match(r"(?:https?://)?github\.com/([a-zA-Z0-9\-]+)", input_str)
    if match:
        return match.group(1)

    # Plain username (alphanumeric + hyphens)
    if re.match(r"^[a-zA-Z0-9\-]+$", input_str):
        return input_str

    raise ValueError(f"Cannot extract GitHub username from: {input_str}")
