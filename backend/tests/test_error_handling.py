"""
Automated Test Suite for RoleGauge API Error Handling.
Tests all required HTTP error response codes and JSON error messages:
- 400: Unknown role / level, invalid UUID format
- 404: GitHub user not found, Analysis ID not found
- 429: GitHub rate limit exceeded
- 504: GitHub API timeout
"""

import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from app.main import app
from app.exceptions import GitHubUserNotFoundError, GitHubRateLimitError, GitHubTimeoutError
from app.services.kb_loader import kb


@pytest.fixture(scope="session", autouse=True)
def init_kb():
    """Ensure KB is loaded for tests."""
    kb.load()


def test_unknown_role_returns_400():
    with TestClient(app) as client:
        response = client.post(
            "/api/analyze",
            json={
                "github_username": "octocat",
                "role_id": "nonexistent_role_xyz",
                "level": "mid",
            },
        )
        assert response.status_code == 400
        data = response.json()
        assert "Unknown role" in data["detail"]
        assert "nonexistent_role_xyz" in data["detail"]


def test_invalid_level_returns_400():
    with TestClient(app) as client:
        response = client.post(
            "/api/analyze",
            json={
                "github_username": "octocat",
                "role_id": "backend",
                "level": "grandmaster",
            },
        )
        assert response.status_code == 400
        data = response.json()
        assert "Level 'grandmaster' not found" in data["detail"]


def test_invalid_uuid_in_results_returns_400():
    with TestClient(app) as client:
        response = client.get("/api/results/not-a-valid-uuid")
        assert response.status_code == 400
        data = response.json()
        assert "Invalid analysis ID format" in data["detail"]


def test_nonexistent_analysis_in_results_returns_404():
    with TestClient(app) as client:
        fake_uuid = "00000000-0000-0000-0000-000000000000"
        response = client.get(f"/api/results/{fake_uuid}")
        assert response.status_code == 404
        data = response.json()
        assert "not found" in data["detail"].lower()


def test_github_user_not_found_returns_404():
    with patch("app.routers.analyze.GitHubFetcher.fetch_user_repos", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.side_effect = GitHubUserNotFoundError("nonexistent_user_9999")
        with TestClient(app) as client:
            response = client.post(
                "/api/analyze",
                json={
                    "github_username": "nonexistent_user_9999",
                    "role_id": "backend",
                    "level": "mid",
                },
            )
            assert response.status_code == 404
            data = response.json()
            assert "GitHub user 'nonexistent_user_9999' was not found" in data["detail"]


def test_github_rate_limit_returns_429():
    with patch("app.routers.analyze.GitHubFetcher.fetch_user_repos", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.side_effect = GitHubRateLimitError("GitHub API rate limit exceeded")
        with TestClient(app) as client:
            response = client.post(
                "/api/analyze",
                json={
                    "github_username": "octocat",
                    "role_id": "backend",
                    "level": "mid",
                },
            )
            assert response.status_code == 429
            data = response.json()
            assert "rate limit exceeded" in data["detail"].lower()


def test_github_timeout_returns_504():
    with patch("app.routers.analyze.GitHubFetcher.fetch_user_repos", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.side_effect = GitHubTimeoutError("GitHub API request timed out")
        with TestClient(app) as client:
            response = client.post(
                "/api/analyze",
                json={
                    "github_username": "octocat",
                    "role_id": "backend",
                    "level": "mid",
                },
            )
            assert response.status_code == 504
            data = response.json()
            assert "timed out" in data["detail"].lower()


def test_health_check():
    with TestClient(app) as client:
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["roles_loaded"] > 0


def test_roles_endpoint():
    with TestClient(app) as client:
        response = client.get("/api/roles")
        assert response.status_code == 200
        data = response.json()
        assert "roles" in data
        role_ids = [r["category"] for r in data["roles"]]
        assert "backend" in role_ids


def test_use_ai_true_gracefully_ignored_with_ad_placements_returned(caplog):
    """
    When use_ai: true is sent, the backend logs the disabled status,
    ignores the AI flag, completes normal analysis pipeline,
    and returns advertising placement signals with ai_enrichment_available: false.
    """
    import logging
    from app.services.github_fetcher import FetchedRepo, RepoMetadata

    fake_meta = RepoMetadata(
        name="my-fastapi-app",
        full_name="testuser/my-fastapi-app",
        url="https://github.com/testuser/my-fastapi-app",
        description="FastAPI REST API",
        primary_language="Python",
        languages={"Python": 1000},
        stars=10,
        forks=2,
        topics=["api", "fastapi"],
    )
    fake_repo = FetchedRepo(
        metadata=fake_meta,
        file_tree=["main.py", "requirements.txt"],
        file_contents={
            "main.py": "from fastapi import FastAPI, APIRouter\napp = FastAPI()\nrouter = APIRouter()",
            "requirements.txt": "fastapi==0.110.0\npydantic==2.6.0\npytest==8.0.0",
        },
        dependency_files={
            "requirements.txt": "fastapi==0.110.0\npydantic==2.6.0\npytest==8.0.0",
        },
    )

    with patch("app.routers.analyze.GitHubFetcher.fetch_user_repos", new_callable=AsyncMock) as mock_fetch, \
         patch("app.routers.analyze.GitHubFetcher.fetch_specific_files", new_callable=AsyncMock) as mock_fetch_files:
        mock_fetch.return_value = [fake_repo]
        mock_fetch_files.return_value = {
            "main.py": "from fastapi import FastAPI, APIRouter\napp = FastAPI()\nrouter = APIRouter()",
            "requirements.txt": "fastapi==0.110.0\npydantic==2.6.0\npytest==8.0.0",
        }

        with caplog.at_level(logging.INFO):
            with TestClient(app) as client:
                response = client.post(
                    "/api/analyze",
                    json={
                        "github_username": "testuser",
                        "role_id": "backend",
                        "level": "mid",
                        "use_ai": True,
                    },
                )

        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()

        # Verify AI enrichment is flagged as not available
        assert data["ai_enrichment_available"] is False
        assert data["analysis_tier"] == "standard"

        # Verify advertisement placement signals
        assert "ad_placements" in data
        assert data["ad_placements"]["loading_screen"] is True
        assert data["ad_placements"]["results_sidebar_left"] is True
        assert data["ad_placements"]["results_sidebar_right"] is True

        # Verify log output confirmed AI enrichment was disabled and ignored
        assert any("AI enrichment requested but currently disabled" in record.message for record in caplog.records)

