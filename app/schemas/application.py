"""
Application-related Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel


class ApplicationCreateRequest(BaseModel):
    campaign_id: str
    message: str | None = None
    instagram_handle: str | None = None
    example_content_url: str | None = None


class ApplicationResponse(BaseModel):
    id: str
    campaign_id: str
    creator_id: str
    message: str | None = None
    instagram_handle: str | None = None
    example_content_url: str | None = None
    status: str  # "pending" | "accepted" | "rejected"
    created_at: datetime
