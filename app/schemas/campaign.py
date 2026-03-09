"""
Campaign-related Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel


class CampaignCreateRequest(BaseModel):
    title: str
    description: str
    deliverables: str
    offer: str
    creator_category: str
    follower_range_min: int | None = None
    follower_range_max: int | None = None
    location: str
    deadline: datetime | None = None


class CampaignUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    deliverables: str | None = None
    offer: str | None = None
    creator_category: str | None = None
    follower_range_min: int | None = None
    follower_range_max: int | None = None
    location: str | None = None
    deadline: datetime | None = None


class CampaignResponse(BaseModel):
    id: str
    business_id: str
    title: str
    description: str
    deliverables: str
    offer: str
    creator_category: str
    follower_range_min: int | None = None
    follower_range_max: int | None = None
    location: str
    deadline: datetime | None = None
    status: str  # "active" | "closed" | "completed"
    created_at: datetime
