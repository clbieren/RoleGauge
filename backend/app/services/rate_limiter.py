"""
Rate Limiter Service for RoleGauge Backend.
Powered by slowapi with in-memory storage (default) and Redis support (production).

Provides:
- Tiered limits for Guest (IP-based) vs Authenticated (user_id-based) requests
- Strict brute-force protection for auth endpoints (/register, /login)
- Specific rate limits for high-cost AI analysis requests (use_ai=true)
- File processing limits for CV/LinkedIn uploads
- Standard HTTP 429 response with Retry-After header and RoleGauge-compliant error payload
"""

import logging
import time
from typing import Optional

from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.config import settings
from app.services.auth_service import decode_token

logger = logging.getLogger(__name__)


def get_ip_key(request: Request) -> str:
    """
    Extract client IP address for IP-based rate limiting (e.g., brute-force protection).
    """
    ip = get_remote_address(request)
    return f"ip:{ip or 'unknown'}"


def get_rate_limit_key(request: Request) -> str:
    """
    Extract user_id if valid Bearer token is present, otherwise fallback to client IP.
    Ensures authenticated users get user-scoped limits while guests get IP-scoped limits.
    """
    auth_header = request.headers.get("Authorization") or request.headers.get("authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header[7:].strip()
        try:
            payload = decode_token(token, expected_type="access")
            user_id = payload.get("sub")
            if user_id:
                return f"user:{user_id}"
        except Exception:
            # Invalid or expired token -> fallback to IP
            pass

    return get_ip_key(request)


# Dynamic limit resolvers based on key (user: vs ip:)
def get_analyze_limit(key: str) -> str:
    """Return general analyze rate limit based on caller tier."""
    if key.startswith("user:"):
        return settings.RATE_LIMIT_AUTH_ANALYZE
    return settings.RATE_LIMIT_GUEST_ANALYZE


def get_ai_analyze_limit(key: str) -> str:
    """Return AI-specific analyze rate limit based on caller tier."""
    if key.startswith("user:"):
        return settings.RATE_LIMIT_AUTH_AI_ANALYZE
    return settings.RATE_LIMIT_GUEST_AI_ANALYZE


def get_upload_limit(key: str) -> str:
    """Return upload rate limit based on caller tier."""
    if key.startswith("user:"):
        return settings.RATE_LIMIT_AUTH_UPLOAD
    return settings.RATE_LIMIT_GUEST_UPLOAD


def is_not_ai_request(request: Request) -> bool:
    """
    Exemption check for AI rate limit:
    Returns True if request does NOT use AI (exempt from AI limit).
    Returns False if request DOES use AI (AI limit will be enforced).
    """
    # Check request state populated by middleware
    if getattr(request.state, "use_ai", False):
        return False

    # Check query param (fallback)
    if request.query_params.get("use_ai", "").lower() in ("true", "1"):
        return False

    # Check custom header (fallback)
    if request.headers.get("x-use-ai", "").lower() in ("true", "1"):
        return False

    return True


# Limiter instance
# Uses Redis storage in production if REDIS_URL is configured, else in-memory
limiter = Limiter(
    key_func=get_rate_limit_key,
    storage_uri=settings.REDIS_URL or "memory://",
)


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    """
    Custom HTTP 429 exception handler.
    Injects Retry-After and X-RateLimit headers, and returns standard JSON payload:
    {"detail": "Rate limit exceeded. Try again in X seconds."}
    """
    retry_after = 60
    headers = {}

    current_limit = getattr(request.state, "view_rate_limit", None)
    if current_limit:
        try:
            limiter_instance = request.app.state.limiter.limiter
            window_stats = limiter_instance.get_window_stats(current_limit[0], *current_limit[1])
            reset_time = 1 + window_stats[0]
            retry_after = max(1, int(reset_time - time.time()))
            headers["Retry-After"] = str(retry_after)
            headers["X-RateLimit-Limit"] = str(current_limit[0].amount)
            headers["X-RateLimit-Remaining"] = str(window_stats[1])
            headers["X-RateLimit-Reset"] = str(int(reset_time))
        except Exception as e:
            logger.debug(f"Failed to calculate window stats for rate limit headers: {e}")
            headers["Retry-After"] = "60"
    else:
        headers["Retry-After"] = "60"

    detail_msg = f"Rate limit exceeded. Try again in {retry_after} seconds."

    return JSONResponse(
        status_code=429,
        content={"detail": detail_msg},
        headers=headers,
    )
