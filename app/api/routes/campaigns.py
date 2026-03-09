"""
Campaign routes — CRUD and campaign feed for creators.
"""

from fastapi import APIRouter

router = APIRouter()


# ── Campaign CRUD (Business) ─────────────────────────
@router.post("/")
async def create_campaign():
    """Create a new campaign (business only)."""
    # TODO: Implement
    pass


@router.get("/")
async def list_campaigns():
    """List / search campaigns — the main feed for creators."""
    # TODO: Implement with query params (location, category, follower range)
    pass


@router.get("/{campaign_id}")
async def get_campaign(campaign_id: str):
    """Get full campaign details."""
    # TODO: Implement
    pass


@router.patch("/{campaign_id}")
async def update_campaign(campaign_id: str):
    """Update campaign details (owner only)."""
    # TODO: Implement
    pass


@router.delete("/{campaign_id}")
async def delete_campaign(campaign_id: str):
    """Delete / close a campaign (owner only)."""
    # TODO: Implement
    pass


# ── Campaign Applications (nested) ───────────────────
@router.get("/{campaign_id}/applications")
async def list_campaign_applications(campaign_id: str):
    """List all applications for a campaign (business only)."""
    # TODO: Implement
    pass
