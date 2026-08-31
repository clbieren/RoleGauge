"""
Authentication Dependencies for FastAPI.
Provides mandatory (get_current_user) and optional (get_optional_user) dependencies.
"""

import logging
from typing import Optional
import uuid

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.db_models import User
from app.services.auth_service import decode_token

logger = logging.getLogger(__name__)

# HTTPBearer scheme with auto_error=False to allow optional token inspection
security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Mandatory authentication dependency.
    Validates the bearer access token and returns the active User object.
    Raises HTTP 401 if missing, invalid, expired, or inactive.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials

    try:
        payload = decode_token(token, expected_type="access")
        user_id_str = payload.get("sub")
        if not user_id_str:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_id = uuid.UUID(user_id_str)
    except (JWTError, ValueError) as e:
        logger.warning(f"Failed to decode access token: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await db.get(User, user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or account is deactivated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> Optional[User]:
    """
    Optional authentication dependency.
    If a valid bearer token is provided, returns the authenticated User.
    If no token is provided or the token is invalid/expired, gracefully returns None.
    This guarantees 100% backward compatibility for guest analysis workflows.
    """
    if not credentials or not credentials.credentials:
        return None

    token = credentials.credentials

    try:
        payload = decode_token(token, expected_type="access")
        user_id_str = payload.get("sub")
        if not user_id_str:
            return None
        user_id = uuid.UUID(user_id_str)
        user = await db.get(User, user_id)
        if user and user.is_active:
            return user
    except Exception as e:
        logger.debug(f"Optional token validation failed, falling back to guest mode: {e}")
        return None

    return None
