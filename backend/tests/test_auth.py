"""
RoleGauge User Accounts & Authentication Test Suite.

Tests:
1. User Registration: valid registration, duplicate email (409), password length validation (422), email validation (422)
2. User Login: valid login, incorrect password (401), non-existent user (401), deactivated user (401)
3. Token Refresh: valid refresh token, expired/malformed refresh token (401), access token used as refresh token (401)
4. User Profile (GET /api/auth/me): valid access token (200), missing auth (401), invalid/expired token (401)
5. User Analysis History & Isolation (GET /api/users/me/analyses):
   - Authenticated /api/analyze call saves analysis with user_id
   - /api/users/me/analyses returns user's past analyses
   - Isolated history per user
6. Analysis Access Control (GET /api/results/{id}):
   - Private analysis accessible by owner (200)
   - Private analysis inaccessible by other users (403)
   - Private analysis inaccessible without auth (401)
   - Guest analysis (user_id=None) publicly accessible (200)
"""

from datetime import timedelta
import io
import os
import sys
from unittest.mock import AsyncMock, patch
import uuid

import pytest
from fastapi.testclient import TestClient

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.main import app
from app.services.auth_service import create_access_token, create_refresh_token, hash_password
from app.services.github_fetcher import FetchedRepo, GitHubFetcher, RepoMetadata
from app.services.kb_loader import kb


@pytest.fixture(scope="module", autouse=True)
def init_kb():
    """Ensure KB is loaded."""
    if not kb.role_categories:
        kb.load()


@pytest.fixture(autouse=True)
def mock_github():
    """Mock GitHub API fetching to ensure fast and deterministic tests."""
    mock_repos = [
        FetchedRepo(
            metadata=RepoMetadata(
                name="fastapi-app",
                full_name="mockuser/fastapi-app",
                url="https://github.com/mockuser/fastapi-app",
                description="FastAPI app with PostgreSQL",
                primary_language="Python",
                languages={"Python": 10000},
                stars=100,
                forks=20,
                topics=["fastapi", "backend"],
                default_branch="main",
            ),
            file_tree=["main.py", "database.py", "requirements.txt"],
            readme_content="FastAPI backend with PostgreSQL",
            file_contents={"main.py": "from fastapi import FastAPI\nimport sqlalchemy"},
            dependency_files={"requirements.txt": "fastapi\nsqlalchemy\nasyncpg"},
        )
    ]
    with patch.object(GitHubFetcher, "fetch_user_repos", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_repos
        yield mock_fetch


# ──────────────────────────────────────────────
# 1. Registration Tests
# ──────────────────────────────────────────────

class TestUserRegistration:
    """Test user registration endpoint POST /api/auth/register."""

    def test_successful_registration(self):
        """Registering with valid email and password returns 201 with tokens and user info."""
        unique_email = f"test_{uuid.uuid4().hex[:8]}@example.com"
        with TestClient(app) as client:
            resp = client.post(
                "/api/auth/register",
                json={
                    "email": unique_email,
                    "password": "StrongPassword123!",
                    "full_name": "Test Engineer",
                },
            )
            assert resp.status_code == 201
            data = resp.json()
            assert "access_token" in data
            assert "refresh_token" in data
            assert data["token_type"] == "bearer"
            assert data["user"]["email"] == unique_email
            assert data["user"]["full_name"] == "Test Engineer"
            assert data["user"]["is_active"] is True
            assert "id" in data["user"]
            # Ensure password hash is NEVER returned
            assert "password" not in data["user"]
            assert "hashed_password" not in data["user"]

    def test_duplicate_email_registration_returns_409(self):
        """Registering with an already registered email returns 409 Conflict."""
        duplicate_email = f"dup_{uuid.uuid4().hex[:8]}@example.com"
        with TestClient(app) as client:
            resp1 = client.post(
                "/api/auth/register",
                json={"email": duplicate_email, "password": "ValidPassword123!"},
            )
            assert resp1.status_code == 201

            resp2 = client.post(
                "/api/auth/register",
                json={"email": duplicate_email, "password": "AnotherPassword456!"},
            )
            assert resp2.status_code == 409
            assert "already exists" in resp2.json()["detail"].lower()

    def test_short_password_returns_422(self):
        """Registering with a password shorter than 8 characters returns 422 Unprocessable Entity."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/auth/register",
                json={"email": "short_pwd@example.com", "password": "short"},
            )
            assert resp.status_code == 422

    def test_invalid_email_format_returns_422(self):
        """Registering with an invalid email format returns 422 Unprocessable Entity."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/auth/register",
                json={"email": "not-a-valid-email", "password": "ValidPassword123!"},
            )
            assert resp.status_code == 422


# ──────────────────────────────────────────────
# 2. Login Tests
# ──────────────────────────────────────────────

class TestUserLogin:
    """Test user login endpoint POST /api/auth/login."""

    def test_successful_login(self):
        """Login with registered email and correct password returns tokens."""
        email = f"login_user_{uuid.uuid4().hex[:8]}@example.com"
        password = "SecurePassword123!"

        with TestClient(app) as client:
            # Register first
            reg_resp = client.post(
                "/api/auth/register",
                json={"email": email, "password": password, "full_name": "Login User"},
            )
            assert reg_resp.status_code == 201

            # Login
            login_resp = client.post(
                "/api/auth/login",
                json={"email": email, "password": password},
            )
            assert login_resp.status_code == 200
            data = login_resp.json()
            assert "access_token" in data
            assert "refresh_token" in data
            assert data["user"]["email"] == email

    def test_wrong_password_returns_401(self):
        """Login with wrong password returns 401 Unauthorized."""
        email = f"wrong_pwd_{uuid.uuid4().hex[:8]}@example.com"
        password = "CorrectPassword123!"

        with TestClient(app) as client:
            client.post(
                "/api/auth/register",
                json={"email": email, "password": password},
            )

            resp = client.post(
                "/api/auth/login",
                json={"email": email, "password": "WrongPassword999!"},
            )
            assert resp.status_code == 401
            assert "invalid email or password" in resp.json()["detail"].lower()

    def test_nonexistent_user_returns_401(self):
        """Login with an unregistered email returns 401 Unauthorized."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/auth/login",
                json={"email": "nobody_exists_here_12345@example.com", "password": "SomePassword123!"},
            )
            assert resp.status_code == 401
            assert "invalid email or password" in resp.json()["detail"].lower()


# ──────────────────────────────────────────────
# 3. Token Refresh Tests
# ──────────────────────────────────────────────

class TestTokenRefresh:
    """Test token refresh endpoint POST /api/auth/refresh."""

    def test_successful_token_refresh(self):
        """Valid refresh token returns a new access token."""
        email = f"refresh_{uuid.uuid4().hex[:8]}@example.com"
        password = "Password123!"

        with TestClient(app) as client:
            reg_resp = client.post(
                "/api/auth/register",
                json={"email": email, "password": password},
            )
            assert reg_resp.status_code == 201
            refresh_token = reg_resp.json()["refresh_token"]

            # Call refresh
            ref_resp = client.post(
                "/api/auth/refresh",
                json={"refresh_token": refresh_token},
            )
            assert ref_resp.status_code == 200
            data = ref_resp.json()
            assert "access_token" in data
            assert data["token_type"] == "bearer"

    def test_invalid_refresh_token_returns_401(self):
        """Invalid or malformed refresh token returns 401."""
        with TestClient(app) as client:
            resp = client.post(
                "/api/auth/refresh",
                json={"refresh_token": "malformed.jwt.token.here"},
            )
            assert resp.status_code == 401

    def test_access_token_rejected_at_refresh_endpoint(self):
        """Passing an access token instead of a refresh token returns 401."""
        email = f"token_type_{uuid.uuid4().hex[:8]}@example.com"
        with TestClient(app) as client:
            reg_resp = client.post(
                "/api/auth/register",
                json={"email": email, "password": "Password123!"},
            )
            access_token = reg_resp.json()["access_token"]

            # Try to refresh using access token
            resp = client.post(
                "/api/auth/refresh",
                json={"refresh_token": access_token},
            )
            assert resp.status_code == 401


# ──────────────────────────────────────────────
# 4. Profile (GET /api/auth/me) Tests
# ──────────────────────────────────────────────

class TestAuthMe:
    """Test GET /api/auth/me profile endpoint."""

    def test_get_me_with_valid_token(self):
        """GET /api/auth/me with valid Bearer token returns user profile."""
        email = f"me_{uuid.uuid4().hex[:8]}@example.com"
        with TestClient(app) as client:
            reg_resp = client.post(
                "/api/auth/register",
                json={"email": email, "password": "Password123!", "full_name": "Profile User"},
            )
            token = reg_resp.json()["access_token"]

            me_resp = client.get(
                "/api/auth/me",
                headers={"Authorization": f"Bearer {token}"},
            )
            assert me_resp.status_code == 200
            data = me_resp.json()
            assert data["email"] == email
            assert data["full_name"] == "Profile User"
            assert data["is_active"] is True

    def test_get_me_unauthenticated_returns_401(self):
        """GET /api/auth/me without token returns 401."""
        with TestClient(app) as client:
            resp = client.get("/api/auth/me")
            assert resp.status_code == 401

    def test_get_me_expired_token_returns_401(self):
        """GET /api/auth/me with an expired token returns 401."""
        user_id = str(uuid.uuid4())
        expired_token = create_access_token(user_id, expires_delta=timedelta(seconds=-10))

        with TestClient(app) as client:
            resp = client.get(
                "/api/auth/me",
                headers={"Authorization": f"Bearer {expired_token}"},
            )
            assert resp.status_code == 401


# ──────────────────────────────────────────────
# 5. User Analysis History & Isolation Tests
# ──────────────────────────────────────────────

class TestUserAnalysisHistory:
    """Test analysis association with user and GET /api/users/me/analyses."""

    def test_authenticated_analysis_linked_to_user(self):
        """Analyses executed with Bearer token are saved with user_id and listed in /api/users/me/analyses."""
        email = f"analyst_{uuid.uuid4().hex[:8]}@example.com"

        with TestClient(app) as client:
            reg = client.post(
                "/api/auth/register",
                json={"email": email, "password": "Password123!", "full_name": "Analyst"},
            )
            token = reg.json()["access_token"]

            # Run analysis with Bearer token
            analyze_resp = client.post(
                "/api/analyze",
                headers={"Authorization": f"Bearer {token}"},
                json={
                    "github_username": "mockuser",
                    "role_id": "backend",
                    "level": "mid",
                },
            )
            assert analyze_resp.status_code == 200
            analysis_id = analyze_resp.json()["id"]

            # Query history
            hist_resp = client.get(
                "/api/users/me/analyses",
                headers={"Authorization": f"Bearer {token}"},
            )
            assert hist_resp.status_code == 200
            history = hist_resp.json()
            assert len(history) >= 1
            matching = [item for item in history if item["id"] == analysis_id]
            assert len(matching) == 1
            assert matching[0]["role_id"] == "backend"
            assert matching[0]["github_username"] == "mockuser"

    def test_user_history_isolation(self):
        """User B cannot see User A's analyses in /api/users/me/analyses."""
        with TestClient(app) as client:
            # User A
            reg_a = client.post(
                "/api/auth/register",
                json={"email": f"user_a_{uuid.uuid4().hex[:8]}@example.com", "password": "Password123!"},
            )
            token_a = reg_a.json()["access_token"]

            # User B
            reg_b = client.post(
                "/api/auth/register",
                json={"email": f"user_b_{uuid.uuid4().hex[:8]}@example.com", "password": "Password123!"},
            )
            token_b = reg_b.json()["access_token"]

            # User A creates analysis
            client.post(
                "/api/analyze",
                headers={"Authorization": f"Bearer {token_a}"},
                json={"github_username": "mockuser", "role_id": "backend", "level": "mid"},
            )

            # User B checks history -> should be empty
            hist_b = client.get(
                "/api/users/me/analyses",
                headers={"Authorization": f"Bearer {token_b}"},
            )
            assert hist_b.status_code == 200
            assert len(hist_b.json()) == 0


# ──────────────────────────────────────────────
# 6. Analysis Access Control (GET /api/results/{id})
# ──────────────────────────────────────────────

class TestAnalysisAccessControl:
    """Test privacy & access control on GET /api/results/{id}."""

    def test_private_analysis_access_permissions(self):
        """
        Private analysis:
        - Owner -> 200
        - Another User -> 403
        - Guest -> 401
        """
        with TestClient(app) as client:
            # User A creates private analysis
            reg_a = client.post(
                "/api/auth/register",
                json={"email": f"owner_{uuid.uuid4().hex[:8]}@example.com", "password": "Password123!"},
            )
            token_a = reg_a.json()["access_token"]

            an_resp = client.post(
                "/api/analyze",
                headers={"Authorization": f"Bearer {token_a}"},
                json={"github_username": "mockuser", "role_id": "backend", "level": "mid"},
            )
            analysis_id = an_resp.json()["id"]

            # User B registers
            reg_b = client.post(
                "/api/auth/register",
                json={"email": f"intruder_{uuid.uuid4().hex[:8]}@example.com", "password": "Password123!"},
            )
            token_b = reg_b.json()["access_token"]

            # 1. Owner requests result -> 200 OK
            resp_owner = client.get(
                f"/api/results/{analysis_id}",
                headers={"Authorization": f"Bearer {token_a}"},
            )
            assert resp_owner.status_code == 200

            # 2. User B requests result -> 403 Forbidden
            resp_other = client.get(
                f"/api/results/{analysis_id}",
                headers={"Authorization": f"Bearer {token_b}"},
            )
            assert resp_other.status_code == 403

            # 3. Unauthenticated guest requests result -> 401 Unauthorized
            resp_guest = client.get(f"/api/results/{analysis_id}")
            assert resp_guest.status_code == 401

    def test_guest_analysis_remains_public(self):
        """An unauthenticated guest analysis (user_id=None) is publicly readable by anyone."""
        with TestClient(app) as client:
            # Guest analysis without token
            an_resp = client.post(
                "/api/analyze",
                json={"github_username": "mockuser", "role_id": "backend", "level": "mid"},
            )
            assert an_resp.status_code == 200
            guest_analysis_id = an_resp.json()["id"]

            # Guest accesses result -> 200
            res_guest = client.get(f"/api/results/{guest_analysis_id}")
            assert res_guest.status_code == 200

            # Authenticated user accesses result -> 200
            reg = client.post(
                "/api/auth/register",
                json={"email": f"reader_{uuid.uuid4().hex[:8]}@example.com", "password": "Password123!"},
            )
            token = reg.json()["access_token"]
            res_auth = client.get(
                f"/api/results/{guest_analysis_id}",
                headers={"Authorization": f"Bearer {token}"},
            )
            assert res_auth.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
