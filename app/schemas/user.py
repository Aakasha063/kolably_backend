"""
User-related Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.core.enums import UserRole


class UserInToken(BaseModel):
    """Decoded user from Supabase JWT + profile lookup."""

    id: str  # profiles.id
    auth_id: str  # auth.users.id (JWT "sub")
    email: str
    role: UserRole
    is_active: bool


class UserResponse(BaseModel):
    """Public user profile response."""

    id: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime
