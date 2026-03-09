"""
Chat / messaging Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel


class MessageCreateRequest(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: str
    conversation_id: str
    sender_id: str
    content: str
    created_at: datetime


class ConversationResponse(BaseModel):
    id: str
    participant_ids: list[str]
    collaboration_id: str | None = None
    last_message: str | None = None
    last_message_at: datetime | None = None
    created_at: datetime
