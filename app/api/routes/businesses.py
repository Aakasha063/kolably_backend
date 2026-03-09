"""
Business routes — profile, discovery.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_businesses():
    """List / search businesses."""
    # TODO: Implement
    pass


@router.get("/{business_id}")
async def get_business(business_id: str):
    """Get a specific business's public profile."""
    # TODO: Implement
    pass


@router.patch("/{business_id}")
async def update_business_profile(business_id: str):
    """Update business profile (own profile only)."""
    # TODO: Implement
    pass


@router.get("/{business_id}/campaigns")
async def get_business_campaigns(business_id: str):
    """List all campaigns for a business."""
    # TODO: Implement
    pass
