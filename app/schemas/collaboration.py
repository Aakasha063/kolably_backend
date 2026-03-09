"""
Collaboration-related Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel


class CollaborationResponse(BaseModel):
    id: str
    campaign_id: str
    creator_id: str
    business_id: str
    status: str  # "active" | "content_submitted" | "completed" | "cancelled"
    content_url: str | None = None
    affiliate_url: str | None = None
    created_at: datetime
    completed_at: datetime | None = None


class ContentSubmitRequest(BaseModel):
    content_url: str
    notes: str | None = None
