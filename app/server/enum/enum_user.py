from enum import Enum

class User_type(Enum):
    admin   = 3
    manager = 2
    normal  = 1
    
    
class User_status(Enum):
    user_created            = "user_created"
    user_pending            = "user_pending"
    user_already_created    = "user_already_created"
    blocked_user            = "blocked_user"
    user_not_created        = "user_not_created"
    