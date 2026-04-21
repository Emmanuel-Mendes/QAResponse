"""
project rounting
"""

import uuid

from flask import Blueprint, redirect, render_template, session, url_for

from app.server.controllers.auth.login import login_required

projects_blueprint = Blueprint("projects", __name__)


@projects_blueprint.route("/projects/<uuid:project_id>", methods=["GET"])
@login_required
def projects_get(project_id: None):
    """
    Docstring for projects_get
    """
    if session.get("user_id") is not None:
        project_id: uuid = project_id

        print(project_id)
        return render_template("project_home/project_home.html")
    return redirect(url_for("login.login"))
