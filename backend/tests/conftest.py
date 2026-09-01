import os
import sys
import pytest

# Ensure backend directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Set test environment variables
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["KB_PATH"] = os.path.join(os.path.dirname(BASE_DIR), "knowledge-base")
os.environ["AI_PROVIDER"] = "none"


@pytest.fixture(autouse=True)
def reset_rate_limiter():
    """Reset rate limiter state before and after each test to prevent test cross-contamination."""
    try:
        from app.services.rate_limiter import limiter
        limiter.reset()
    except Exception:
        pass
    yield
    try:
        from app.services.rate_limiter import limiter
        limiter.reset()
    except Exception:
        pass
