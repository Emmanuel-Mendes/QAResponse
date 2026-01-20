"""
project rounting
"""

from flask import Blueprint, redirect, render_template, session, url_for

from app.server.controllers.auth.login import login_required
from app.server.utils.session import get_session

projects_blueprint = Blueprint("projects", __name__)


@projects_blueprint.route("/projects", methods=["GET"])
@login_required
def projects_get():
    """
    Docstring for projects_get
    """
    if get_session() is False:
        return render_template("home/home.html")
    return redirect(url_for("login.login"))


@projects_blueprint.route("/projects", methods=["POST"])
def projects():
    """
    Docstring for projects
    """
    print("Post: ")
    print(session.get)
