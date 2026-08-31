"""
RoleGauge Database Models.
SQLAlchemy ORM models for storing analysis results.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Float, Text, DateTime, ForeignKey, Integer, JSON, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Analysis(Base):
    """Top-level analysis record for a GitHub user + role + level combination."""
    __tablename__ = "analyses"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    github_username: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    role_id: Mapped[str] = mapped_column(String(100), nullable=False)
    level: Mapped[str] = mapped_column(String(50), nullable=False)  # junior | mid | senior
    readiness_score: Mapped[float] = mapped_column(Float, nullable=False)
    readiness_tier: Mapped[str] = mapped_column(String(50), nullable=False)  # not_ready | developing | approaching | ready | exceeds
    total_repos_scanned: Mapped[int] = mapped_column(Integer, default=0)
    relevant_repos_found: Mapped[int] = mapped_column(Integer, default=0)
    ai_provider_used: Mapped[str | None] = mapped_column(String(50), nullable=True)  # openai | gemini | none
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    skill_results: Mapped[list["SkillResult"]] = relationship(back_populates="analysis", cascade="all, delete-orphan")
    repo_data: Mapped[list["RepoData"]] = relationship(back_populates="analysis", cascade="all, delete-orphan")
    assessment_sessions: Mapped[list["AssessmentSession"]] = relationship(back_populates="analysis", cascade="all, delete-orphan")


class SkillResult(Base):
    """Score for a single skill within an analysis."""
    __tablename__ = "skill_results"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False)
    skill_id: Mapped[str] = mapped_column(String(100), nullable=False)
    skill_name: Mapped[str] = mapped_column(String(255), nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    importance: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationships
    analysis: Mapped["Analysis"] = relationship(back_populates="skill_results")
    subskill_results: Mapped[list["SubskillResult"]] = relationship(back_populates="skill_result", cascade="all, delete-orphan")


class SubskillResult(Base):
    """Evidence result for a single subskill (composite key: skill_id.subskill_id)."""
    __tablename__ = "subskill_results"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    skill_result_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("skill_results.id", ondelete="CASCADE"), nullable=False)
    composite_key: Mapped[str] = mapped_column(String(200), nullable=False)  # e.g. gd_game_engine.physics_system
    subskill_name: Mapped[str] = mapped_column(String(255), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)  # evidence_found | not_yet_evidenced | claimed | verified_gap
    evidence_sources: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # List of files/patterns/signals found
    contributing_sources: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    ceiling_applied: Mapped[str | None] = mapped_column(String(255), nullable=True)
    calculation_trace: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    skill_result: Mapped["SkillResult"] = relationship(back_populates="subskill_results")


class RepoData(Base):
    """Metadata about a scanned repository."""
    __tablename__ = "repo_data"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False)
    repo_name: Mapped[str] = mapped_column(String(255), nullable=False)
    repo_url: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    primary_language: Mapped[str | None] = mapped_column(String(100), nullable=True)
    languages: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # {lang: bytes}
    stars: Mapped[int] = mapped_column(Integer, default=0)
    forks: Mapped[int] = mapped_column(Integer, default=0)
    topics: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # List of topic strings
    is_relevant: Mapped[bool] = mapped_column(default=False)
    relevant_files_count: Mapped[int] = mapped_column(Integer, default=0)
    evidence_found: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # Composite keys found in this repo

    # Relationships
    analysis: Mapped["Analysis"] = relationship(back_populates="repo_data")


class AssessmentSession(Base):
    """Adaptive Assessment Q&A Session."""
    __tablename__ = "assessment_sessions"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False)
    role_id: Mapped[str] = mapped_column(String(100), nullable=False)
    level: Mapped[str] = mapped_column(String(50), nullable=False)
    questions_data: Mapped[dict] = mapped_column(JSON, nullable=False)  # questions & expected keywords (server-side only)
    answers_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # user answers submitted
    status: Mapped[str] = mapped_column(String(50), default="active")  # active | completed
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    analysis: Mapped["Analysis"] = relationship(back_populates="assessment_sessions")

