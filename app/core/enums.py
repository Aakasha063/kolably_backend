"""
Application-wide enums.
"""

from enum import Enum


class UserRole(str, Enum):
    CREATOR = "creator"
    BUSINESS = "business"
    SUPERADMIN = "superadmin"
