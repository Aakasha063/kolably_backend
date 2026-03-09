"""
Security utilities — Supabase JWT verification.
"""

from jose import jwt, JWTError
from fastapi import HTTPException, status

from app.core.config import settings


def verify_supabase_token(token: str) -> dict:
    """
    Decode and verify a Supabase-issued JWT.

    Returns the decoded payload dict on success.
    Raises HTTPException on failure.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated",
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired token: {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )
