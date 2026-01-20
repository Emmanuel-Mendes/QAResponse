"""
Docstring for app.server.utils.session
"""

from flask import session


def get_session(session_str: str = "user_id") -> bool:
    """
    Docstring for get_session

    :param session_str: Description
    :type session_str: str
    :return: Description
    :rtype: bool
    """
    session_consult = session.get(session_str)
    if session_consult is not None:
        return True
    return False
