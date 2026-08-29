"""
RoleGauge Database Setup.
Async SQLAlchemy engine and session management.

NOTE: PostgreSQL is strictly REQUIRED for Production environments.
SQLite (sqlite+aiosqlite:///) is supported solely as an isolated fixture
for local unit/integration tests and development environments without Docker.
"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# Configure engine kwargs according to dialect
engine_kwargs = {"echo": settings.DEBUG}
if "sqlite" not in settings.DATABASE_URL.lower():
    engine_kwargs.update({
        "pool_size": 10,
        "max_overflow": 20,
    })

engine = create_async_engine(
    settings.DATABASE_URL,
    **engine_kwargs,
)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency that yields a database session."""
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def create_tables():
    """Create all tables. Used during development startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def dispose_engine():
    """Dispose the engine on shutdown."""
    await engine.dispose()
