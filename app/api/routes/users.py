"""
User routes — shared operations for both account types.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
async def get_current_user():
    """Get the currently authenticated user's profile."""
    # TODO: Implement
    pass


@router.patch("/me")
async def update_current_user():
    """Update the currently authenticated user's base profile."""
    # TODO: Implement
    pass


@router.delete("/me")
async def delete_current_user():
    """Deactivate / delete the current user's account."""
    # TODO: Implement
    pass
