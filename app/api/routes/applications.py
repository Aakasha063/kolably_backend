"""
Application routes — creators apply to campaigns, businesses accept/reject.
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_application():
    """Creator applies to a campaign."""
    # TODO: Implement
    pass


@router.get("/{application_id}")
async def get_application(application_id: str):
    """Get application details."""
    # TODO: Implement
    pass


@router.patch("/{application_id}/accept")
async def accept_application(application_id: str):
    """Business accepts a creator's application."""
    # TODO: Implement
    pass


@router.patch("/{application_id}/reject")
async def reject_application(application_id: str):
    """Business rejects a creator's application."""
    # TODO: Implement
    pass


@router.get("/me/sent")
async def list_my_applications():
    """List all applications sent by the current creator."""
    # TODO: Implement
    pass
