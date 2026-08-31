"""
End-to-End User Accounts & Authentication Verification Script for RoleGauge.

Demonstrates:
(1) User Registration (POST /api/auth/register) -> Token issuance, User UUID generation.
(2) User Login (POST /api/auth/login) -> Password verification against bcrypt hash, token creation.
(3) Authenticated User Profile (GET /api/auth/me) -> Access token validation via Bearer header.
(4) Authenticated Analysis Execution (POST /api/analyze) -> Analysis record linked directly to user_id in DB.
(5) User Analysis History (GET /api/users/me/analyses) -> Historical retrieval isolated to authenticated user.
(6) Access Control & Authorization (GET /api/results/{id}):
    - Creator/Owner access -> 200 OK
    - Other Authenticated User -> 403 Forbidden
    - Unauthenticated Guest -> 401 Unauthorized
    - Guest Analysis (user_id=None) -> 200 OK for everyone
(7) Token Refresh (POST /api/auth/refresh) -> Fresh access token generation via refresh token.
"""

from datetime import timedelta
import io
import json
import os
import sys
from unittest.mock import AsyncMock, patch
import uuid

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(PROJECT_ROOT, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["KB_PATH"] = os.path.join(PROJECT_ROOT, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

from fastapi.testclient import TestClient
from app.main import app
from app.services.github_fetcher import FetchedRepo, GitHubFetcher, RepoMetadata
from app.services.kb_loader import kb


def _mock_github_repos():
    return [
        FetchedRepo(
            metadata=RepoMetadata(
                name="cloud-microservice",
                full_name="alexmercer/cloud-microservice",
                url="https://github.com/alexmercer/cloud-microservice",
                description="High throughput event-driven microservice in Python with FastAPI & PostgreSQL",
                primary_language="Python",
                languages={"Python": 15000, "SQL": 5000},
                stars=250,
                forks=45,
                topics=["fastapi", "postgresql", "kafka", "microservices"],
                default_branch="main",
            ),
            file_tree=["main.py", "database.py", "models/user.py", "schema.sql", "requirements.txt"],
            readme_content="# Cloud Microservice\nEvent-driven microservice using Kafka and PostgreSQL.",
            file_contents={
                "main.py": "from fastapi import FastAPI\nimport asyncpg\napp = FastAPI()",
                "database.py": "import asyncpg\nasync def get_connection(): pass",
                "schema.sql": "CREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(255));",
            },
            dependency_files={"requirements.txt": "fastapi>=0.115.0\nasyncpg>=0.29.0\naiokafka>=0.11.0\npytest>=8.0.0"},
        )
    ]


def main():
    print("=" * 80)
    print("ROLEGAUGE USER AUTHENTICATION & ANALYSIS LINKING — E2E VERIFICATION")
    print("=" * 80)

    kb.load()

    with patch.object(GitHubFetcher, "fetch_user_repos", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = _mock_github_repos()

        with TestClient(app) as client:
            # ──────────────────────────────────────────────────────────────────────────
            # 1. User Registration (POST /api/auth/register)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 1: User Registration (POST /api/auth/register)")
            print("-" * 80)

            user_email = f"alex.mercer_{uuid.uuid4().hex[:6]}@example.com"
            user_password = "SecureDevPassword2026!"
            full_name = "Alex Mercer"

            reg_payload = {
                "email": user_email,
                "password": user_password,
                "full_name": full_name,
            }
            print(f"[REQUEST] Registering: email='{user_email}', name='{full_name}', password='{'*' * len(user_password)}'")

            reg_resp = client.post("/api/auth/register", json=reg_payload)
            assert reg_resp.status_code == 201, f"Registration failed: {reg_resp.text}"
            reg_data = reg_resp.json()

            user_id = reg_data["user"]["id"]
            access_token = reg_data["access_token"]
            refresh_token = reg_data["refresh_token"]

            print(f"[RESPONSE] HTTP {reg_resp.status_code} Created")
            print(f"  • User ID: {user_id}")
            print(f"  • Email: {reg_data['user']['email']}")
            print(f"  • Full Name: {reg_data['user']['full_name']}")
            print(f"  • is_active: {reg_data['user']['is_active']}")
            print(f"  • Access Token (JWT): {access_token[:35]}...{access_token[-15:]}")
            print(f"  • Refresh Token (JWT): {refresh_token[:35]}...{refresh_token[-15:]}")

            # ──────────────────────────────────────────────────────────────────────────
            # 2. User Login (POST /api/auth/login)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 2: User Login (POST /api/auth/login)")
            print("-" * 80)

            login_payload = {"email": user_email, "password": user_password}
            print(f"[REQUEST] Logging in with email='{user_email}'")

            login_resp = client.post("/api/auth/login", json=login_payload)
            assert login_resp.status_code == 200, f"Login failed: {login_resp.text}"
            login_data = login_resp.json()

            print(f"[RESPONSE] HTTP {login_resp.status_code} OK")
            print(f"  • Authenticated User ID: {login_data['user']['id']}")
            print(f"  • Fresh Access Token: {login_data['access_token'][:35]}...")

            # ──────────────────────────────────────────────────────────────────────────
            # 3. User Profile Retrieval (GET /api/auth/me)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 3: Authenticated User Profile (GET /api/auth/me)")
            print("-" * 80)

            auth_headers = {"Authorization": f"Bearer {access_token}"}
            me_resp = client.get("/api/auth/me", headers=auth_headers)
            assert me_resp.status_code == 200, f"Get profile failed: {me_resp.text}"
            me_data = me_resp.json()

            print(f"[RESPONSE] HTTP {me_resp.status_code} OK")
            print(f"  • Profile ID: {me_data['id']}")
            print(f"  • Email: {me_data['email']}")
            print(f"  • Name: {me_data['full_name']}")
            print(f"  • Created At: {me_data['created_at']}")

            # ──────────────────────────────────────────────────────────────────────────
            # 4. Authenticated Analysis Execution (POST /api/analyze with Bearer Token)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 4: Authenticated Analysis (POST /api/analyze with Bearer Token)")
            print("-" * 80)

            analyze_payload = {
                "github_username": "alexmercer",
                "role_id": "backend",
                "level": "mid",
            }
            print(f"[REQUEST] Running analysis for role='backend' (mid) with Authorization header")

            an_resp = client.post("/api/analyze", json=analyze_payload, headers=auth_headers)
            assert an_resp.status_code == 200, f"Analysis failed: {an_resp.text}"
            an_data = an_resp.json()

            analysis_id = an_data["id"]
            print(f"[RESPONSE] HTTP {an_resp.status_code} OK")
            print(f"  • Generated Analysis ID: {analysis_id}")
            print(f"  • Role: {an_data['role_name']} ({an_data['level']})")
            print(f"  • Readiness Score: {an_data['readiness_score']:.4f} ({an_data['readiness_tier']} - {an_data['readiness_label']})")
            print(f"  • Scanned Repos: {an_data['total_repos_scanned']}, Relevant: {an_data['relevant_repos_found']}")

            # ──────────────────────────────────────────────────────────────────────────
            # 5. User Analysis History (GET /api/users/me/analyses)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 5: User History Verification (GET /api/users/me/analyses)")
            print("-" * 80)

            hist_resp = client.get("/api/users/me/analyses", headers=auth_headers)
            assert hist_resp.status_code == 200, f"Get history failed: {hist_resp.text}"
            hist_data = hist_resp.json()

            print(f"[RESPONSE] HTTP {hist_resp.status_code} OK — Found {len(hist_data)} recorded analyses:")
            for item in hist_data:
                print(f"  • [ID: {item['id']}] User: {item['github_username']} | Role: {item['role_name']} | Score: {item['readiness_score']:.4f} ({item['readiness_tier']}) | Date: {item['created_at']}")

            assert any(item["id"] == analysis_id for item in hist_data), "Analysis not found in user history!"
            print(f"[OK] Verified: Analysis {analysis_id} is persisted and linked to user {user_id}")

            # ──────────────────────────────────────────────────────────────────────────
            # 6. Privacy & Access Control (GET /api/results/{id})
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 6: Privacy & Access Control Verification (GET /api/results/{id})")
            print("-" * 80)

            # Register User B (Intruder)
            user_b_email = f"intruder_{uuid.uuid4().hex[:6]}@example.com"
            reg_b = client.post(
                "/api/auth/register",
                json={"email": user_b_email, "password": "IntruderPassword123!", "full_name": "Intruder User"},
            )
            token_b = reg_b.json()["access_token"]

            # 6a. Owner access
            owner_resp = client.get(f"/api/results/{analysis_id}", headers=auth_headers)
            print(f"[TEST 6a - Owner Access] Status: HTTP {owner_resp.status_code} (Expected: 200) -> SUCCESS")
            assert owner_resp.status_code == 200

            # 6b. Other user access (User B)
            other_resp = client.get(f"/api/results/{analysis_id}", headers={"Authorization": f"Bearer {token_b}"})
            print(f"[TEST 6b - Other User Access] Status: HTTP {other_resp.status_code} Forbidden (Detail: '{other_resp.json()['detail']}') -> SUCCESS")
            assert other_resp.status_code == 403

            # 6c. Unauthenticated guest access
            guest_resp = client.get(f"/api/results/{analysis_id}")
            print(f"[TEST 6c - Guest Access to Private Analysis] Status: HTTP {guest_resp.status_code} Unauthorized (Detail: '{guest_resp.json()['detail']}') -> SUCCESS")
            assert guest_resp.status_code == 401

            # 6d. Public guest analysis
            guest_an_resp = client.post("/api/analyze", json=analyze_payload)
            guest_an_id = guest_an_resp.json()["id"]
            guest_read_resp = client.get(f"/api/results/{guest_an_id}")
            print(f"[TEST 6d - Guest Analysis Public Access] Status: HTTP {guest_read_resp.status_code} OK (Expected: 200) -> SUCCESS")
            assert guest_read_resp.status_code == 200

            # ──────────────────────────────────────────────────────────────────────────
            # 7. Token Refresh (POST /api/auth/refresh)
            # ──────────────────────────────────────────────────────────────────────────
            print("\n" + "-" * 80)
            print("STEP 7: Token Refresh Flow (POST /api/auth/refresh)")
            print("-" * 80)

            ref_resp = client.post("/api/auth/refresh", json={"refresh_token": refresh_token})
            assert ref_resp.status_code == 200, f"Refresh failed: {ref_resp.text}"
            new_access_token = ref_resp.json()["access_token"]

            # Verify new access token works
            verify_me = client.get("/api/auth/me", headers={"Authorization": f"Bearer {new_access_token}"})
            assert verify_me.status_code == 200
            print(f"[RESPONSE] HTTP {ref_resp.status_code} OK")
            print(f"  • New Access Token: {new_access_token[:35]}...")
            print(f"  • Verified against /api/auth/me: Email={verify_me.json()['email']}")

    print("\n" + "=" * 80)
    print("ALL USER AUTHENTICATION & ANALYSIS LINKING E2E VERIFICATIONS PASSED!")
    print("=" * 80)


if __name__ == "__main__":
    main()
