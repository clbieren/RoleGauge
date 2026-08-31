"""
RoleGauge Backend — FastAPI Application.
Entry point for the backend server.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import create_tables, dispose_engine
from app.services.kb_loader import kb

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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
from app.routers import analyze, roles, results, cv_upload, assessment  # noqa: E402

app.include_router(analyze.router)
app.include_router(roles.router)
app.include_router(results.router)
app.include_router(cv_upload.router)
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
