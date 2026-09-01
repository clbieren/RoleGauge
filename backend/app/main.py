"""
RoleGauge Backend — FastAPI Application.
Entry point for the backend server.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.database import create_tables, dispose_engine
from app.services.kb_loader import kb
from app.services.rate_limiter import limiter, rate_limit_exceeded_handler

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle events."""
    # Startup
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")

    # Load knowledge base
    kb.load()
    logger.info(f"Knowledge base loaded: {len(kb.role_categories)} roles")

    # Create database tables
    await create_tables()
    logger.info("Database tables created/verified")

    yield

    # Shutdown
    await dispose_engine()
    logger.info("Application shutdown complete")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="GitHub profile analysis for role-based skill assessment",
    lifespan=lifespan,
)

# Rate Limiter setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)


@app.middleware("http")
async def rate_limit_context_middleware(request: Request, call_next):
    """Pre-parse use_ai flag for analyze endpoint to support synchronous rate limiting."""
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


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
from app.routers import analyze, roles, results, cv_upload, linkedin_upload, assessment, auth, users  # noqa: E402

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(analyze.router)
app.include_router(roles.router)
app.include_router(results.router)
app.include_router(cv_upload.router)
app.include_router(linkedin_upload.router)
app.include_router(assessment.router)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "roles_loaded": len(kb.role_categories),
        "ai_provider": settings.AI_PROVIDER,
    }
