from enum import Enum

class Error(Enum):
    USER_NOT_CREATED = 1
    USER_ALREADY_CREATED = 2
    INTERNAL_ERROR = 3
    SERVER_ERROR = 4
    MISSING_FIELDS = 5