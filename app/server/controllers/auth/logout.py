"""
Controller blog
"""

from flask import Blueprint, redirect, session, url_for

from app.server.controllers.auth.login import login_required

initial_blueprint = Blueprint("logout", __name__)


@initial_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    """
    Docstring for logout
    """
    print(session.on_update.__dict__)
    session.clear()
    return redirect(url_for("login.login"))
