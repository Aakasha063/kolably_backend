"""
Shared / common Pydantic schemas.
"""

from pydantic import BaseModel


class MessageResponse(BaseModel):
    """Generic message response."""
    message: str


class PaginationParams(BaseModel):
    """Standard pagination query parameters."""
    page: int = 1
    page_size: int = 20
