"""
Test Suite for RoleGauge Rate Limiting.
Verifies tiered rate limits, brute-force protection on auth endpoints,
cost-sensitive use_ai rate limiting, user/IP isolation, Retry-After headers,
and 429 error responses conforming to RoleGauge standards.
"""

import os
import sys
import uuid
import pytest
from unittest.mock import patch
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
os.environ.setdefault("AI_PROVIDER", "none")
os.environ.setdefault("KB_PATH", os.path.join(os.path.dirname(BASE_DIR), "knowledge-base"))

from app.config import settings
from app.services.auth_service import create_access_token
from app.services.rate_limiter import (
    get_ai_analyze_limit,
    get_analyze_limit,
    get_ip_key,
    get_rate_limit_key,
    get_upload_limit,
    is_not_ai_request,
    rate_limit_exceeded_handler,
)


def create_test_app():
    """Create an isolated test FastAPI application with rate limiting configured."""
    test_limiter = Limiter(
        key_func=get_rate_limit_key,
        storage_uri="memory://",
    )

    app = FastAPI()
    app.state.limiter = test_limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

    @app.middleware("http")
    async def rate_limit_context_middleware(request: Request, call_next):
        if request.url.path.endswith("/analyze") and request.method == "POST":
            content_type = request.headers.get("content-type", "").lower()
            if "application/json" in content_type:
                try:
                    body_bytes = await request.body()
                    if body_bytes:
                        import json
                        data = json.loads(body_bytes)
                        if data.get("use_ai") in (True, "true", "True", 1, "1"):
                            request.state.use_ai = True
                except Exception:
                    pass
            elif "multipart/form-data" in content_type:
                if request.query_params.get("use_ai", "").lower() in ("true", "1") or request.headers.get("x-use-ai", "").lower() in ("true", "1"):
                    request.state.use_ai = True
        return await call_next(request)

    @app.post("/api/analyze")
    @test_limiter.limit(get_analyze_limit, key_func=get_rate_limit_key)
    @test_limiter.limit(get_ai_analyze_limit, key_func=get_rate_limit_key, exempt_when=is_not_ai_request)
    async def mock_analyze(request: Request):
        return {"status": "analyzed"}

    @app.post("/api/auth/login")
    @test_limiter.limit(settings.RATE_LIMIT_AUTH_BRUTE_FORCE, key_func=get_ip_key)
    async def mock_login(request: Request):
        return {"status": "logged_in"}

    @app.post("/api/auth/register")
    @test_limiter.limit(settings.RATE_LIMIT_AUTH_BRUTE_FORCE, key_func=get_ip_key)
    async def mock_register(request: Request):
        return {"status": "registered"}

    @app.post("/api/cv/upload")
    @test_limiter.limit(get_upload_limit, key_func=get_rate_limit_key)
    async def mock_cv_upload(request: Request):
        return {"status": "uploaded"}

    @app.post("/api/linkedin/upload")
    @test_limiter.limit(get_upload_limit, key_func=get_rate_limit_key)
    async def mock_linkedin_upload(request: Request):
        return {"status": "uploaded"}

    return app, test_limiter


# ═══════════════════════════════════════════════════════════════════
# 1. Guest Analyze Rate Limit Tests (5/hour)
# ═══════════════════════════════════════════════════════════════════

class TestGuestAnalyzeRateLimit:

    def test_guest_analyze_limit_exceeded_at_6th_request(self):
        """Guest gets 5 requests per hour. 6th request returns 429."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.100")

        # Requests 1 to 5 should succeed (status 200)
        for i in range(1, 6):
            res = client.post("/api/analyze", json={"use_ai": False})
            assert res.status_code == 200, f"Request {i} failed unexpectedly with status {res.status_code}"

        # 6th request must exceed rate limit
        res6 = client.post("/api/analyze", json={"use_ai": False})
        assert res6.status_code == 429, f"Request 6 should be 429, got {res6.status_code}"

        # Check response body and Retry-After header
        body = res6.json()
        assert "detail" in body
        assert "Rate limit exceeded" in body["detail"]
        assert "Retry-After" in res6.headers
        assert int(res6.headers["Retry-After"]) > 0


# ═══════════════════════════════════════════════════════════════════
# 2. Guest AI Analyze Rate Limit Tests (2/hour)
# ═══════════════════════════════════════════════════════════════════

class TestGuestAIAnalyzeRateLimit:

    def test_guest_ai_analyze_stricter_limit(self):
        """Guest gets only 2 AI requests per hour. 3rd AI request returns 429."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.101")

        # 2 AI requests succeed
        res1 = client.post("/api/analyze", json={"use_ai": True})
        assert res1.status_code == 200
        res2 = client.post("/api/analyze", json={"use_ai": True})
        assert res2.status_code == 200

        # 3rd AI request exceeds AI limit (2/hr)
        res3 = client.post("/api/analyze", json={"use_ai": True})
        assert res3.status_code == 429, f"Expected 429 for 3rd AI request, got {res3.status_code}"
        assert "Retry-After" in res3.headers


# ═══════════════════════════════════════════════════════════════════
# 3. Authenticated User Analyze Rate Limit Tests (20/hour & 10/hour AI)
# ═══════════════════════════════════════════════════════════════════

class TestAuthUserAnalyzeRateLimit:

    def test_auth_user_higher_analyze_limit(self):
        """Authenticated user has 20/hr limit (higher than guest 5/hr)."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.102")

        user_id = str(uuid.uuid4())
        token = create_access_token(user_id)
        headers = {"Authorization": f"Bearer {token}"}

        # Authenticated user can make 20 non-AI requests
        for i in range(1, 21):
            res = client.post("/api/analyze", json={"use_ai": False}, headers=headers)
            assert res.status_code == 200, f"Auth request {i} failed with status {res.status_code}"

        # 21st request hits the limit
        res21 = client.post("/api/analyze", json={"use_ai": False}, headers=headers)
        assert res21.status_code == 429

    def test_auth_user_ai_limit(self):
        """Authenticated user gets 10 AI requests per hour. 11th request returns 429."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.103")

        user_id = str(uuid.uuid4())
        token = create_access_token(user_id)
        headers = {"Authorization": f"Bearer {token}"}

        # 10 AI requests succeed
        for i in range(1, 11):
            res = client.post("/api/analyze", json={"use_ai": True}, headers=headers)
            assert res.status_code == 200, f"Auth AI request {i} failed with {res.status_code}"

        # 11th AI request exceeds AI limit (10/hr)
        res11 = client.post("/api/analyze", json={"use_ai": True}, headers=headers)
        assert res11.status_code == 429


# ═══════════════════════════════════════════════════════════════════
# 4. Brute-force Protection on Auth Endpoints (5/15minute per IP)
# ═══════════════════════════════════════════════════════════════════

class TestAuthBruteForceProtection:

    def test_login_brute_force_blocked_after_5_attempts(self):
        """POST /api/auth/login limits to 5 attempts per 15 minutes per IP."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.104")

        # 5 login attempts processed
        for i in range(1, 6):
            res = client.post("/api/auth/login", json={"email": "hacker@test.com", "password": "wrong"})
            assert res.status_code == 200, f"Attempt {i} failed with {res.status_code}"

        # 6th attempt blocked by rate limiter
        res6 = client.post("/api/auth/login", json={"email": "hacker@test.com", "password": "wrong"})
        assert res6.status_code == 429
        assert "Retry-After" in res6.headers

    def test_register_brute_force_blocked_after_5_attempts(self):
        """POST /api/auth/register limits to 5 attempts per 15 minutes per IP."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.105")

        for i in range(1, 6):
            res = client.post("/api/auth/register", json={"email": f"u{i}@test.com", "password": "pass"})
            assert res.status_code == 200

        res6 = client.post("/api/auth/register", json={"email": "u6@test.com", "password": "pass"})
        assert res6.status_code == 429


# ═══════════════════════════════════════════════════════════════════
# 5. User and IP Isolation Tests
# ═══════════════════════════════════════════════════════════════════

class TestUserAndIPIsolation:

    def test_different_users_do_not_affect_each_other(self):
        """User A exhausting quota does not block User B."""
        app, _ = create_test_app()
        client = TestClient(app)

        user_a = str(uuid.uuid4())
        user_b = str(uuid.uuid4())
        token_a = create_access_token(user_a)
        token_b = create_access_token(user_b)

        headers_a = {"Authorization": f"Bearer {token_a}"}
        headers_b = {"Authorization": f"Bearer {token_b}"}

        # User A exhausts all 20 requests
        for _ in range(20):
            res = client.post("/api/analyze", json={"use_ai": False}, headers=headers_a)
            assert res.status_code == 200

        # User A 21st request is blocked
        res_a_blocked = client.post("/api/analyze", json={"use_ai": False}, headers=headers_a)
        assert res_a_blocked.status_code == 429

        # User B can still make requests without interference
        res_b = client.post("/api/analyze", json={"use_ai": False}, headers=headers_b)
        assert res_b.status_code == 200

    def test_authenticated_user_isolated_from_guest_ip_limit(self):
        """Guest exhausts IP quota, but authenticated user on same IP can still make requests."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.106")

        # Guest on this IP makes 5 requests and gets blocked on 6th
        for _ in range(5):
            client.post("/api/analyze", json={"use_ai": False})
        res_guest_blocked = client.post("/api/analyze", json={"use_ai": False})
        assert res_guest_blocked.status_code == 429

        # Authenticated user on the same client IP can still analyze because key is user-scoped
        user_id = str(uuid.uuid4())
        token = create_access_token(user_id)
        res_auth = client.post("/api/analyze", json={"use_ai": False}, headers={"Authorization": f"Bearer {token}"})
        assert res_auth.status_code == 200


# ═══════════════════════════════════════════════════════════════════
# 6. Upload Endpoint Rate Limits (10/hr guest, 30/hr auth)
# ═══════════════════════════════════════════════════════════════════

class TestUploadRateLimit:

    def test_guest_cv_upload_limit_10_per_hour(self):
        """Guest CV upload limit is 10/hour."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.107")

        for i in range(1, 11):
            res = client.post("/api/cv/upload")
            assert res.status_code == 200, f"CV Upload {i} failed"

        res11 = client.post("/api/cv/upload")
        assert res11.status_code == 429

    def test_guest_linkedin_upload_limit_10_per_hour(self):
        """Guest LinkedIn upload limit is 10/hour."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.108")

        for i in range(1, 11):
            res = client.post("/api/linkedin/upload")
            assert res.status_code == 200, f"LinkedIn Upload {i} failed"

        res11 = client.post("/api/linkedin/upload")
        assert res11.status_code == 429

    def test_auth_user_upload_limit_30_per_hour(self):
        """Authenticated user upload limit is 30/hour."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.109")

        user_id = str(uuid.uuid4())
        token = create_access_token(user_id)
        headers = {"Authorization": f"Bearer {token}"}

        for i in range(1, 31):
            res = client.post("/api/cv/upload", headers=headers)
            assert res.status_code == 200, f"Auth CV upload {i} failed"

        res31 = client.post("/api/cv/upload", headers=headers)
        assert res31.status_code == 429


# ═══════════════════════════════════════════════════════════════════
# 7. Error Format and Headers Validation
# ═══════════════════════════════════════════════════════════════════

class TestRateLimitFormatAndHeaders:

    def test_error_response_structure_and_headers(self):
        """Verify 429 response structure, Retry-After, and X-RateLimit headers."""
        app, _ = create_test_app()
        client = TestClient(app, base_url="http://192.168.1.110")

        # Exhaust limit
        for _ in range(5):
            client.post("/api/analyze", json={"use_ai": False})

        res = client.post("/api/analyze", json={"use_ai": False})
        assert res.status_code == 429

        # Verify JSON body detail
        data = res.json()
        assert "detail" in data
        assert data["detail"].startswith("Rate limit exceeded. Try again in ")
        assert data["detail"].endswith(" seconds.")

        # Verify HTTP Headers
        assert "Retry-After" in res.headers
        assert "X-RateLimit-Limit" in res.headers
        assert "X-RateLimit-Remaining" in res.headers
        assert "X-RateLimit-Reset" in res.headers
        assert res.headers["X-RateLimit-Remaining"] == "0"


# ═══════════════════════════════════════════════════════════════════
# 8. Storage Abstraction & Config
# ═══════════════════════════════════════════════════════════════════

class TestStorageConfiguration:

    def test_in_memory_default_storage(self):
        """When REDIS_URL is not set, limiter uses memory://."""
        with patch.object(settings, "REDIS_URL", None):
            lim = Limiter(key_func=get_rate_limit_key, storage_uri=settings.REDIS_URL or "memory://")
            assert lim._storage_uri == "memory://"
