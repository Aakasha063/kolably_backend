"""
Auth service — Facade over Supabase Auth.

All Supabase-specific logic is contained here. If we migrate to another
auth provider, only this file changes — routes and frontend stay untouched.
"""

from fastapi import HTTPException, status
from supabase_auth.errors import AuthApiError

from app.core.supabase import get_supabase_client, get_supabase_admin_client
from app.schemas.auth import (
    CreatorSignupRequest,
    BusinessSignupRequest,
    LoginRequest,
)


# ─── Signup ───────────────────────────────────────────

async def signup_creator(data: CreatorSignupRequest) -> dict:
    """
    1. Create auth user via Supabase with role='creator' in metadata
    2. Trigger auto-creates profiles row
    3. Insert creators row with profile data
    4. Return session tokens + user info
    """
    supabase = get_supabase_client()

    # 1. Create auth user
    try:
        auth_response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password,
                "options": {
                    "data": {"role": "creator"},
                },
            }
        )
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    if not auth_response.user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Signup failed — user not created",
        )

    auth_id = str(auth_response.user.id)

    # 2. Get the auto-created profile
    admin_client = get_supabase_admin_client()
    profile_result = (
        admin_client.table("profiles")
        .select("*")
        .eq("auth_id", auth_id)
        .single()
        .execute()
    )

    if not profile_result.data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Profile creation trigger failed",
        )

    profile_id = profile_result.data["id"]

    # 3. Insert creator profile
    creator_data = {
        "profile_id": profile_id,
        "name": data.name,
        "username": data.username,
        "city": data.city,
        "niche": data.niche,
        "follower_count": data.follower_count,
        "instagram_handle": data.instagram_handle,
        "profile_photo_url": data.profile_photo_url,
    }

    admin_client.table("creators").insert(creator_data).execute()

    # 4. Build response
    session = auth_response.session
    return {
        "access_token": session.access_token if session else None,
        "refresh_token": session.refresh_token if session else None,
        "token_type": "bearer",
        "user": {
            "id": profile_id,
            "email": data.email,
            "role": "creator",
            "creator": {
                "name": data.name,
                "username": data.username,
                "city": data.city,
                "niche": data.niche,
            },
        },
    }


async def signup_business(data: BusinessSignupRequest) -> dict:
    """
    1. Create auth user via Supabase with role='business' in metadata
    2. Trigger auto-creates profiles row
    3. Insert businesses row with profile data
    4. Return session tokens + user info
    """
    supabase = get_supabase_client()

    # 1. Create auth user
    try:
        auth_response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password,
                "options": {
                    "data": {"role": "business"},
                },
            }
        )
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    if not auth_response.user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Signup failed — user not created",
        )

    auth_id = str(auth_response.user.id)

    # 2. Get the auto-created profile
    admin_client = get_supabase_admin_client()
    profile_result = (
        admin_client.table("profiles")
        .select("*")
        .eq("auth_id", auth_id)
        .single()
        .execute()
    )

    if not profile_result.data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Profile creation trigger failed",
        )

    profile_id = profile_result.data["id"]

    # 3. Insert business profile
    business_data = {
        "profile_id": profile_id,
        "business_name": data.business_name,
        "owner_name": data.owner_name,
        "category": data.business_category,
        "city": data.city,
        "address": data.address,
        "description": data.business_description,
    }

    admin_client.table("businesses").insert(business_data).execute()

    # 4. Build response
    session = auth_response.session
    return {
        "access_token": session.access_token if session else None,
        "refresh_token": session.refresh_token if session else None,
        "token_type": "bearer",
        "user": {
            "id": profile_id,
            "email": data.email,
            "role": "business",
            "business": {
                "business_name": data.business_name,
                "owner_name": data.owner_name,
                "city": data.city,
                "category": data.business_category,
            },
        },
    }


# ─── Login ────────────────────────────────────────────

async def login(data: LoginRequest) -> dict:
    """
    1. Authenticate via Supabase
    2. Load profile + check email verified + check active
    3. Return tokens + user info
    """
    supabase = get_supabase_client()

    try:
        auth_response = supabase.auth.sign_in_with_password(
            {
                "email": data.email,
                "password": data.password,
            }
        )
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )

    if not auth_response.user or not auth_response.session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Check email verification
    if not auth_response.user.email_confirmed_at:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email not verified. Please check your inbox.",
        )

    # Load profile
    auth_id = str(auth_response.user.id)
    admin_client = get_supabase_admin_client()
    profile_result = (
        admin_client.table("profiles")
        .select("*")
        .eq("auth_id", auth_id)
        .single()
        .execute()
    )

    if not profile_result.data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found",
        )

    profile = profile_result.data

    if not profile.get("is_active", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated",
        )

    session = auth_response.session
    return {
        "access_token": session.access_token,
        "refresh_token": session.refresh_token,
        "token_type": "bearer",
        "user": {
            "id": profile["id"],
            "email": profile["email"],
            "role": profile["role"],
            "is_active": profile["is_active"],
        },
    }


# ─── Token Refresh ────────────────────────────────────

async def refresh_session(refresh_token: str) -> dict:
    """Refresh via Supabase and return new token pair."""
    supabase = get_supabase_client()

    try:
        auth_response = supabase.auth.refresh_session(refresh_token)
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )

    if not auth_response.session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to refresh session",
        )

    session = auth_response.session
    return {
        "access_token": session.access_token,
        "refresh_token": session.refresh_token,
        "token_type": "bearer",
    }


# ─── Logout ───────────────────────────────────────────

async def logout(access_token: str) -> dict:
    """Sign out via Supabase — invalidates the session."""
    supabase = get_supabase_client()

    try:
        supabase.auth.sign_out(access_token)
    except AuthApiError:
        pass  # Best-effort logout

    return {"message": "Logged out successfully"}


# ─── Password Reset ──────────────────────────────────

async def forgot_password(email: str) -> dict:
    """Trigger Supabase password reset email."""
    supabase = get_supabase_client()

    try:
        supabase.auth.reset_password_email(email)
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    return {"message": "Password reset link sent to your email"}


async def reset_password(access_token: str, new_password: str) -> dict:
    """Update password via Supabase using the reset token."""
    supabase = get_supabase_client()

    try:
        supabase.auth.set_session(access_token, "")
        supabase.auth.update_user({"password": new_password})
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    return {"message": "Password updated successfully"}


# ─── Get Current User Profile ─────────────────────────

async def get_user_profile(auth_id: str) -> dict:
    """Load full profile + role-specific data for the current user."""
    admin_client = get_supabase_admin_client()

    # Get base profile
    profile_result = (
        admin_client.table("profiles")
        .select("*")
        .eq("auth_id", auth_id)
        .single()
        .execute()
    )

    if not profile_result.data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    profile = profile_result.data
    response = {**profile}

    # Load role-specific data
    if profile["role"] in ("creator", "superadmin"):
        creator_result = (
            admin_client.table("creators")
            .select("*")
            .eq("profile_id", profile["id"])
            .maybe_single()
            .execute()
        )
        if creator_result.data:
            response["creator"] = creator_result.data

    if profile["role"] in ("business", "superadmin"):
        business_result = (
            admin_client.table("businesses")
            .select("*")
            .eq("profile_id", profile["id"])
            .maybe_single()
            .execute()
        )
        if business_result.data:
            response["business"] = business_result.data

    return response
