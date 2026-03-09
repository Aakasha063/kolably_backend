"""
Collaboration routes — managing active collaborations, content submission, completion.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_collaborations():
    """List collaborations for the current user (filtered by role)."""
    # TODO: Implement
    pass


@router.get("/{collaboration_id}")
async def get_collaboration(collaboration_id: str):
    """Get collaboration details."""
    # TODO: Implement
    pass


@router.post("/{collaboration_id}/submit")
async def submit_content(collaboration_id: str):
    """Creator submits content / post link for the collaboration."""
    # TODO: Implement
    pass


@router.patch("/{collaboration_id}/complete")
async def mark_complete(collaboration_id: str):
    """Business marks the collaboration as completed."""
    # TODO: Implement
    pass


@router.patch("/{collaboration_id}/cancel")
async def cancel_collaboration(collaboration_id: str):
    """Cancel an active collaboration."""
    # TODO: Implement
    pass
