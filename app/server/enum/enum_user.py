"""
Docstring for app.server.enum.enum_user
"""
from enum import Enum


class UserType(Enum):
    """
    Docstring for UserType
    """
    ADMIN = 3
    MANAGER = 2
    NORMAL = 1


class UserStatus(Enum):
    """
    Docstring for UserStatus
    """
    USER_CREATED = "user_created"
    USER_PENDING = "user_pending"
    USER_ALREADY_CREATED = "user_already_created"
    BLOCKED_USER = "blocked_user"
    USER_NOT_CREATED = "user_not_created"
