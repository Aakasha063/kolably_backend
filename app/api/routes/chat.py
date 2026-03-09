"""
Chat / messaging routes.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/conversations")
async def list_conversations():
    """List all chat conversations for the current user."""
    # TODO: Implement
    pass


@router.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get messages in a conversation."""
    # TODO: Implement
    pass


@router.post("/conversations/{conversation_id}/messages")
async def send_message(conversation_id: str):
    """Send a message in a conversation."""
    # TODO: Implement
    pass
