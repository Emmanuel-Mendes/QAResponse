"""
Docstring for app.server.enum.enum_user
"""

from enum import Enum


class ProjectType(Enum):
    """
    Docstring for Project
    """

    ADMIN = 3
    MANAGER = 2
    NORMAL = 1


class ProjectStatus(Enum):
    """
    Docstring for Project
    """

    PROJECT_CREATED = "user_created"
    PROJECT_PENDING = "user_pending"
    PROJECT_ALREADY_CREATED = "user_already_created"
    PROJECT_USER = "blocked_user"
    PROJECT_NOT_CREATED = "user_not_created"
