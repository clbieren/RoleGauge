"""
Verification Script for Stage 3 (Auth Wiring).
Tests backend auth flows with realistic requests:
1. POST /api/auth/register -> returns tokens and user info
2. POST /api/auth/login -> returns valid access token
3. GET /api/auth/me -> authenticates with Bearer token
4. GET /api/users/me/analyses -> lists user analyses with Bearer token
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
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test_stage3.db"
os.environ["KB_PATH"] = os.path.join(BASE_DIR, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

# Ensure backend root is on PYTHONPATH
backend_dir = os.path.join(BASE_DIR, "backend")
sys.path.insert(0, backend_dir)

from fastapi.testclient import TestClient
from app.main import app as fastapi_app
from app.database import engine, Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def main():
    asyncio.run(init_db())
    
    unique_suffix = uuid.uuid4().hex[:8]
    test_email = f"user_{unique_suffix}@example.com"
    test_password = "SecurePassword123!"
    test_name = "Stage3 Tester"

    with TestClient(fastapi_app) as client:
        print(f"--- 1. Testing Registration: {test_email} ---")
        reg_payload = {
            "email": test_email,
            "password": test_password,
            "full_name": test_name
        }
        reg_resp = client.post("/api/auth/register", json=reg_payload)
        print("Registration response status:", reg_resp.status_code)
        assert reg_resp.status_code == 201, f"Registration failed: {reg_resp.text}"
        reg_data = reg_resp.json()
        assert "access_token" in reg_data, "No access_token in registration response"
        assert "user" in reg_data, "No user in registration response"
        assert reg_data["user"]["email"] == test_email
        print("✓ Registration successful. User ID:", reg_data["user"]["id"])

        print("\n--- 2. Testing Login ---")
        login_payload = {
            "email": test_email,
            "password": test_password
        }
        login_resp = client.post("/api/auth/login", json=login_payload)
        print("Login response status:", login_resp.status_code)
        assert login_resp.status_code == 200, f"Login failed: {login_resp.text}"
        login_data = login_resp.json()
        token = login_data["access_token"]
        assert token, "Empty token received from login"
        print("✓ Login successful. Access token acquired.")

        print("\n--- 3. Testing GET /api/auth/me with Bearer token ---")
        headers = {"Authorization": f"Bearer {token}"}
        me_resp = client.get("/api/auth/me", headers=headers)
        print("Profile response status:", me_resp.status_code)
        assert me_resp.status_code == 200, f"Profile fetch failed: {me_resp.text}"
        me_data = me_resp.json()
        assert me_data["email"] == test_email
        assert me_data["full_name"] == test_name
        print(f"✓ Profile retrieved successfully: {me_data['full_name']} ({me_data['email']})")

        print("\n--- 4. Testing GET /api/users/me/analyses with Bearer token ---")
        history_resp = client.get("/api/users/me/analyses", headers=headers)
        print("History response status:", history_resp.status_code)
        assert history_resp.status_code == 200, f"History fetch failed: {history_resp.text}"
        analyses = history_resp.json()
        assert isinstance(analyses, list)
        print(f"✓ History retrieved successfully: {len(analyses)} records found.")

    print("\n==========================================")
    print("  STAGE 3 (AUTH WIRING) VERIFICATION PASSED!")
    print("==========================================")

if __name__ == "__main__":
    main()
