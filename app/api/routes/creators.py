"""
Creator routes — profile, discovery, portfolio.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_creators():
    """List / search creators with filters (location, niche, follower range)."""
    # TODO: Implement with query params for filtering
    pass


@router.get("/{creator_id}")
async def get_creator(creator_id: str):
    """Get a specific creator's public profile."""
    # TODO: Implement
    pass


@router.patch("/{creator_id}")
async def update_creator_profile(creator_id: str):
    """Update creator profile (own profile only)."""
    # TODO: Implement
    pass


@router.get("/{creator_id}/portfolio")
async def get_creator_portfolio(creator_id: str):
    """Get a creator's portfolio posts."""
    # TODO: Implement
    pass


@router.post("/{creator_id}/portfolio")
async def add_portfolio_item(creator_id: str):
    """Add a portfolio item to the creator's profile."""
    # TODO: Implement
    pass


@router.delete("/{creator_id}/portfolio/{item_id}")
async def delete_portfolio_item(creator_id: str, item_id: str):
    """Remove a portfolio item."""
    # TODO: Implement
    pass
