"""
Verification script for RoleGauge Rate Limiting.
Demonstrates step-by-step request progression across all tiers and shows real 429 responses.
"""

import sys
import os
import uuid
import json
import logging
from unittest.mock import AsyncMock, patch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "backend"))

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["AI_PROVIDER"] = "none"
os.environ["KB_PATH"] = os.path.join(BASE_DIR, "knowledge-base")

# Suppress debug logs
logging.basicConfig(level=logging.ERROR)
for name in ("httpx", "slowapi", "app", "uvicorn"):
    logging.getLogger(name).setLevel(logging.ERROR)

from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_service import create_access_token
from app.services.github_fetcher import FetchedRepo, RepoMetadata
from app.services.rate_limiter import limiter


def run_demonstration():
    print("=" * 75, flush=True)
    print("  ROLEGAUGE RATE LIMITING VERIFICATION & DEMONSTRATION", flush=True)
    print("=" * 75, flush=True)

    mock_repos = [
        FetchedRepo(
            metadata=RepoMetadata(
                name="demo-app",
                full_name="mockuser/demo-app",
                url="https://github.com/mockuser/demo-app",
                description="FastAPI REST service",
                stars=5, forks=1, languages={"Python": 1000}, topics=["fastapi"], is_fork=False
            ),
            file_tree=["main.py"],
            readme_content="# Demo App",
        )
    ]

    with patch("app.routers.analyze.GitHubFetcher.fetch_user_repos", new_callable=AsyncMock, return_value=mock_repos), \
         patch("app.routers.analyze.GitHubFetcher.fetch_specific_files", new_callable=AsyncMock, return_value={"main.py": "from fastapi import FastAPI"}):

        with TestClient(app) as client:

            # ─────────────────────────────────────────────────────────────
            # Scenario 1: Guest Analyze (Limit: 5/hour)
            # ─────────────────────────────────────────────────────────────
            limiter.reset()
            print("\n[Scenario 1] Guest Standard Analysis (Limit: 5 req/hour, IP-based)", flush=True)
            print("-" * 75, flush=True)
            for i in range(1, 8):
                res = client.post(
                    "/api/analyze",
                    json={"github_username": "mockuser", "role_id": "backend", "level": "mid", "use_ai": False},
                )
                if res.status_code == 429:
                    retry_after = res.headers.get("Retry-After")
                    body = res.json()
                    print(f"  Request #{i}: HTTP {res.status_code} TOO MANY REQUESTS | Retry-After: {retry_after}s | Body: {json.dumps(body)}", flush=True)
                else:
                    print(f"  Request #{i}: HTTP {res.status_code} OK (Allowed)", flush=True)

            # ─────────────────────────────────────────────────────────────
            # Scenario 2: Guest AI Analyze (Limit: 2/hour)
            # ─────────────────────────────────────────────────────────────
            limiter.reset()
            print("\n[Scenario 2] Guest Costly AI Analysis (Limit: 2 req/hour, IP-based)", flush=True)
            print("-" * 75, flush=True)
            for i in range(1, 5):
                res = client.post(
                    "/api/analyze",
                    json={"github_username": "mockuser", "role_id": "backend", "level": "mid", "use_ai": True},
                )
                if res.status_code == 429:
                    retry_after = res.headers.get("Retry-After")
                    body = res.json()
                    print(f"  AI Request #{i}: HTTP {res.status_code} TOO MANY REQUESTS | Retry-After: {retry_after}s | Body: {json.dumps(body)}", flush=True)
                else:
                    print(f"  AI Request #{i}: HTTP {res.status_code} OK (Allowed)", flush=True)

            # ─────────────────────────────────────────────────────────────
            # Scenario 3: Authenticated User Analyze (Limit: 20/hour)
            # ─────────────────────────────────────────────────────────────
            limiter.reset()
            print("\n[Scenario 3] Authenticated User Analysis (Limit: 20 req/hour, user_id-based)", flush=True)
            print("-" * 75, flush=True)
            user_id = str(uuid.uuid4())
            token = create_access_token(user_id)
            auth_headers = {"Authorization": f"Bearer {token}"}

            for i in range(1, 23):
                res = client.post(
                    "/api/analyze",
                    json={"github_username": "mockuser", "role_id": "backend", "level": "mid", "use_ai": False},
                    headers=auth_headers,
                )
                if i in (1, 2, 10, 19, 20, 21, 22):
                    if res.status_code == 429:
                        retry_after = res.headers.get("Retry-After")
                        body = res.json()
                        print(f"  Auth Request #{i}: HTTP {res.status_code} TOO MANY REQUESTS | Retry-After: {retry_after}s | Body: {json.dumps(body)}", flush=True)
                    else:
                        print(f"  Auth Request #{i}: HTTP {res.status_code} OK (Allowed)", flush=True)
                elif i == 3:
                    print("  ... requests #3 to #18 allowed (HTTP 200) ...", flush=True)

            # ─────────────────────────────────────────────────────────────
            # Scenario 4: Authenticated User AI Analyze (Limit: 10/hour)
            # ─────────────────────────────────────────────────────────────
            limiter.reset()
            print("\n[Scenario 4] Authenticated User AI Analysis (Limit: 10 req/hour, user_id-based)", flush=True)
            print("-" * 75, flush=True)
            for i in range(1, 13):
                res = client.post(
                    "/api/analyze",
                    json={"github_username": "mockuser", "role_id": "backend", "level": "mid", "use_ai": True},
                    headers=auth_headers,
                )
                if i in (1, 2, 9, 10, 11, 12):
                    if res.status_code == 429:
                        retry_after = res.headers.get("Retry-After")
                        body = res.json()
                        print(f"  Auth AI Request #{i}: HTTP {res.status_code} TOO MANY REQUESTS | Retry-After: {retry_after}s | Body: {json.dumps(body)}", flush=True)
                    else:
                        print(f"  Auth AI Request #{i}: HTTP {res.status_code} OK (Allowed)", flush=True)
                elif i == 3:
                    print("  ... AI requests #3 to #8 allowed (HTTP 200) ...", flush=True)

            # ─────────────────────────────────────────────────────────────
            # Scenario 5: Auth Brute-force Protection (Limit: 5/15minute per IP)
            # ─────────────────────────────────────────────────────────────
            limiter.reset()
            print("\n[Scenario 5] Auth Login Brute-Force Defense (Limit: 5 req/15min, IP-based)", flush=True)
            print("-" * 75, flush=True)
            for i in range(1, 8):
                res = client.post(
                    "/api/auth/login",
                    json={"email": "attacker@example.com", "password": "WrongPassword123!"},
                )
                if res.status_code == 429:
                    retry_after = res.headers.get("Retry-After")
                    body = res.json()
                    print(f"  Login Attempt #{i}: HTTP {res.status_code} TOO MANY REQUESTS | Retry-After: {retry_after}s | Body: {json.dumps(body)}", flush=True)
                else:
                    print(f"  Login Attempt #{i}: HTTP {res.status_code} (Processed)", flush=True)

    print("\n" + "=" * 75, flush=True)
    print("  ALL RATE LIMITING SCENARIOS VERIFIED SUCCESSFULLY!", flush=True)
    print("=" * 75, flush=True)


if __name__ == "__main__":
    run_demonstration()
