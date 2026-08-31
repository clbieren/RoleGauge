"""
RoleGauge Backend Configuration.
Loads settings from environment variables with sensible defaults.
"""

from pydantic import field_validator
from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # --- Application ---
    APP_NAME: str = "RoleGauge"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    BACKEND_PORT: int = 8000
    FRONTEND_PORT: int = 3000

    # --- Database ---
    POSTGRES_USER: Optional[str] = "rolegauge"
    POSTGRES_PASSWORD: Optional[str] = "rolegauge"
    POSTGRES_DB: Optional[str] = "rolegauge"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = "postgresql+asyncpg://rolegauge:rolegauge@localhost:5432/rolegauge"

    # --- GitHub ---
    GITHUB_TOKEN: Optional[str] = None  # Optional PAT for higher rate limits (60 -> 5000/hr)
    GITHUB_API_BASE: str = "https://api.github.com"
    GITHUB_MAX_REPOS: int = 100  # Max repos to fetch per user
    GITHUB_MAX_FILE_SIZE: int = 500_000  # Max file size in bytes to fetch content (500KB)

    # --- AI Provider ---
    AI_PROVIDER: str = "none"  # "openai" | "gemini" | "none" (keyword-only mode)
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o-mini"
    GEMINI_API_KEY: Optional[str] = None
    GEMINI_MODEL: str = "gemini-2.0-flash"

    # --- Knowledge Base ---
    KB_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "knowledge-base")

    # --- CV Upload ---
    CV_MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10 MB
    CV_ALLOWED_EXTENSIONS: list[str] = [".pdf", ".docx"]

    # --- Authentication & JWT ---
    JWT_SECRET_KEY: str = "rolegauge-insecure-secret-key-change-in-production-32bytes"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7     # 7 days

    @field_validator("JWT_SECRET_KEY")
    @classmethod
    def validate_jwt_secret_key(cls, v: str) -> str:
        if not v or len(v.strip()) < 16:
            raise ValueError("JWT_SECRET_KEY must be at least 16 characters long for security.")
        return v

    # --- CORS ---
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    @classmethod
    def settings_customise_sources(cls, settings_cls, init_settings, env_settings, dotenv_settings, file_secret_settings):
        return init_settings, env_settings, dotenv_settings, file_secret_settings

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore",
    }


settings = Settings()
