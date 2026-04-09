"""
Auth-related Pydantic schemas — request/response models for all auth endpoints.
"""

from pydantic import BaseModel, EmailStr, Field


# ── Signup Requests ───────────────────────────────────
class CreatorSignupRequest(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    city: str
    instagram_handle: str
    niche: str
    follower_count: int = Field(..., ge=0)
    profile_photo_url: str | None = None


class BusinessSignupRequest(BaseModel):
    business_name: str
    owner_name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    business_category: str
    city: str
    address: str
    business_description: str | None = None


# ── Login ─────────────────────────────────────────────
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ── Token Refresh ────────────────────────────────────
class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ── Password Reset ────────────────────────────────────
class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    access_token: str
    new_password: str = Field(..., min_length=8)


# ── Responses ─────────────────────────────────────────
class AuthTokenResponse(BaseModel):
    """Returned on signup, login, and token refresh."""

    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str = "bearer"
    user: dict | None = None  # profile + role info


class MessageResponse(BaseModel):
    """Generic success message."""

    message: str


# ── Profile Update ────────────────────────────────────
class UpdateProfileRequest(BaseModel):
    """Fields that can be updated for either Creator or Business."""

    # Common
    city: str | None = None

    # Creator specific
    name: str | None = None
    username: str | None = None
    instagram_handle: str | None = None
    niche: str | None = None
    follower_count: int | None = Field(None, ge=0)
    profile_photo_url: str | None = None

    # Business specific
    business_name: str | None = None
    owner_name: str | None = None
    business_category: str | None = None
    address: str | None = None
    business_description: str | None = None
