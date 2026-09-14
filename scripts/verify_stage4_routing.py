"""
Verification Script for Stage 4 (Routing & Persistence).
Verifies:
1. Creating an analysis for a user
2. Fetching the analysis directly via GET /api/results/{id} (as requested by /results/[id])
3. Listing user's historical analyses via GET /api/users/me/analyses (as requested by /history)
4. Public/Guest access to unauthenticated analyses via GET /api/results/{id}
"""

import sys
import os
import uuid
import asyncio
import io

if sys.platform == "win32":
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test_stage4.db"
os.environ["KB_PATH"] = os.path.join(BASE_DIR, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

# Ensure backend root is on PYTHONPATH
backend_dir = os.path.join(BASE_DIR, "backend")
sys.path.insert(0, backend_dir)

from fastapi.testclient import TestClient
from app.main import app as fastapi_app
from app.database import engine, Base
from app.models.db_models import Analysis, User, SkillResult, SubskillResult
from app.services.auth_service import hash_password

async def seed_data(test_email: str):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Insert test user and analysis directly into database
    from sqlalchemy.ext.asyncio import AsyncSession
    async with AsyncSession(engine, expire_on_commit=False) as session:
        user_uuid = uuid.uuid4()
        user = User(
            id=user_uuid,
            email=test_email,
            hashed_password=hash_password("HistoryPass123!"),
            full_name="History Tester",
            is_active=True,
        )
        session.add(user)
        await session.flush()

        # User's private analysis
        user_analysis_uuid = uuid.uuid4()
        analysis_user = Analysis(
            id=user_analysis_uuid,
            user_id=user.id,
            github_username="octocat",
            role_id="backend",
            level="mid",
            readiness_score=0.785,
            readiness_tier="almost_ready",
            total_repos_scanned=5,
            relevant_repos_found=3,
            ai_provider_used="none",
        )
        session.add(analysis_user)
        await session.flush()

        skill1 = SkillResult(
            analysis_id=analysis_user.id,
            skill_id="be_api_design",
            skill_name="API Design",
            score=0.82,
            importance=0.9,
        )
        session.add(skill1)
        await session.flush()

        sub1 = SubskillResult(
            skill_result_id=skill1.id,
            composite_key="be_api_design.restful_principles",
            subskill_name="RESTful Principles",
            confidence=0.85,
            status="evidence_found",
            evidence_sources=["fastapi-app/main.py"],
            contributing_sources=[{"source": "github", "strength": 0.85, "file_path": "main.py"}],
        )
        session.add(sub1)

        # Guest public analysis (user_id=None)
        guest_analysis_uuid = uuid.uuid4()
        analysis_guest = Analysis(
            id=guest_analysis_uuid,
            user_id=None,
            github_username="torvalds",
            role_id="backend",
            level="senior",
            readiness_score=0.95,
            readiness_tier="ready",
            total_repos_scanned=10,
            relevant_repos_found=8,
            ai_provider_used="none",
        )
        session.add(analysis_guest)
        await session.commit()

        return str(user_uuid), str(user_analysis_uuid), str(guest_analysis_uuid)


def main():
    test_email = f"hist_{uuid.uuid4().hex[:8]}@example.com"
    user_id, user_analysis_id, guest_analysis_id = asyncio.run(seed_data(test_email))

    with TestClient(fastapi_app) as client:
        print("--- 1. Login to get Bearer token ---")
        login_resp = client.post("/api/auth/login", json={
            "email": test_email,
            "password": "HistoryPass123!"
        })
        assert login_resp.status_code == 200, f"Login failed: {login_resp.text}"
        token = login_resp.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        print(f"[OK] Logged in successfully. Token acquired.")

        print(f"\n--- 2. Direct fetch GET /api/results/{user_analysis_id} (used by /results/[id]) ---")
        res_resp = client.get(f"/api/results/{user_analysis_id}", headers=headers)
        assert res_resp.status_code == 200, f"Failed to fetch user analysis: {res_resp.text}"
        res_data = res_resp.json()
        assert res_data["id"] == user_analysis_id
        assert res_data["github_username"] == "octocat"
        assert res_data["readiness_score"] == 0.785
        assert len(res_data["skills"]) >= 1
        print(f"[OK] Retrieved user analysis successfully: {res_data['role_name']} - {res_data['readiness_score']}%")

        print(f"\n--- 3. Direct fetch GET /api/results/{guest_analysis_id} (guest permalink) ---")
        guest_resp = client.get(f"/api/results/{guest_analysis_id}")
        assert guest_resp.status_code == 200, f"Failed to fetch guest analysis: {guest_resp.text}"
        guest_data = guest_resp.json()
        assert guest_data["id"] == guest_analysis_id
        assert guest_data["github_username"] == "torvalds"
        print(f"[OK] Retrieved guest analysis successfully: {guest_data['github_username']} - {guest_data['readiness_score']}%")

        print(f"\n--- 4. List user history GET /api/users/me/analyses (used by /history) ---")
        hist_resp = client.get("/api/users/me/analyses", headers=headers)
        assert hist_resp.status_code == 200, f"Failed to fetch history: {hist_resp.text}"
        hist_data = hist_resp.json()
        assert len(hist_data) == 1, f"Expected 1 history item, found {len(hist_data)}"
        item = hist_data[0]
        assert item["id"] == user_analysis_id
        assert item["github_username"] == "octocat"
        assert item["readiness_tier"] == "almost_ready"
        print(f"[OK] Retrieved history successfully: Found analysis {item['id']} for {item['github_username']} ({item['role_name']})")

    print("\n==========================================")
    print("  STAGE 4 (ROUTING & PERSISTENCE) PASSED! ")
    print("==========================================")


if __name__ == "__main__":
    main()
