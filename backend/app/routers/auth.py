"""
Authentication Router.
Provides endpoints for user registration, login, token refresh, and profile retrieval.

Endpoints:
- POST /api/auth/register -> Register a new user account (returns tokens & user info)
- POST /api/auth/login    -> Login with email & password (returns tokens & user info)
- POST /api/auth/refresh  -> Generate a new access token using a refresh token
- GET  /api/auth/me       -> Retrieve current authenticated user profile
"""

import logging
import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from jose import JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.db_models import User
from app.models.schemas import (
    TokenRefreshRequest,
    TokenRefreshResponse,
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse,
)
from app.services.auth_service import (
    create_access_token,
    create_tokens,
    decode_token,
    hash_password,
    verify_password,
)
from app.services.rate_limiter import get_ip_key, limiter

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user account",
)
@limiter.limit(settings.RATE_LIMIT_AUTH_BRUTE_FORCE, key_func=get_ip_key)
async def register(
    request: Request,
    req: UserRegisterRequest,
    db: AsyncSession = Depends(get_db),
) -> TokenResponse:
    """
    Register a new user with email, password, and optional full name.
    Returns JWT access & refresh tokens along with user profile information.
    """
    normalized_email = req.email.strip().lower()

    # Check if user with same email already exists
    stmt = select(User).where(User.email == normalized_email)
    res = await db.execute(stmt)
    existing_user = res.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email address already exists.",
        )

    # Hash password and create user record
    hashed = hash_password(req.password)
    new_user = User(
        email=normalized_email,
        hashed_password=hashed,
        full_name=req.full_name.strip() if req.full_name else None,
        is_active=True,
    )
    db.add(new_user)
    await db.flush()

    tokens = create_tokens(str(new_user.id))

    user_resp = UserResponse(
        id=str(new_user.id),
        email=new_user.email,
        full_name=new_user.full_name,
        is_active=new_user.is_active,
        created_at=new_user.created_at,
    )

    logger.info(f"User registered successfully: {new_user.email} (id={new_user.id})")

    return TokenResponse(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        token_type="bearer",
        user=user_resp,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login with email and password",
)
@limiter.limit(settings.RATE_LIMIT_AUTH_BRUTE_FORCE, key_func=get_ip_key)
async def login(
    request: Request,
    req: UserLoginRequest,
    db: AsyncSession = Depends(get_db),
) -> TokenResponse:
    """
    Authenticate with email and password.
    Returns fresh access & refresh tokens.
    """
    normalized_email = req.email.strip().lower()

    stmt = select(User).where(User.email == normalized_email)
    res = await db.execute(stmt)
    user = res.scalar_one_or_none()

    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is deactivated.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    tokens = create_tokens(str(user.id))

    user_resp = UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active,
        created_at=user.created_at,
    )

    logger.info(f"User logged in successfully: {user.email} (id={user.id})")

    return TokenResponse(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        token_type="bearer",
        user=user_resp,
    )


@router.post(
    "/refresh",
    response_model=TokenRefreshResponse,
    summary="Refresh access token using a refresh token",
)
async def refresh_token(
    req: TokenRefreshRequest,
    db: AsyncSession = Depends(get_db),
) -> TokenRefreshResponse:
    """
    Validate a refresh token and return a new access token.
    """
    try:
        payload = decode_token(req.refresh_token, expected_type="refresh")
        user_id_str = payload.get("sub")
        if not user_id_str:
            raise ValueError("Missing 'sub' claim")
        user_id = uuid.UUID(user_id_str)
    except (JWTError, ValueError) as e:
        logger.warning(f"Invalid refresh token: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await db.get(User, user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or account is deactivated.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    new_access_token = create_access_token(str(user.id))

    return TokenRefreshResponse(
        access_token=new_access_token,
        token_type="bearer",
    )


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user profile",
)
async def get_me(
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    """
    Retrieve profile details of the currently authenticated user.
    """
    return UserResponse(
        id=str(current_user.id),
        email=current_user.email,
        full_name=current_user.full_name,
        is_active=current_user.is_active,
        created_at=current_user.created_at,
    )
