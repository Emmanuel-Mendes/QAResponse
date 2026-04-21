"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required
from app.server.domain.models.projects.projects_repository_by_users import ProjectUserServiceDb

project_blueprint = Blueprint("project", __name__)


@project_blueprint.route("/project", methods=["GET"])
@login_required
def project_get_post():
    """
    Docstring for create_get
    """

    if session.get("user_id") is not None:
        if request.method == "POST":
            return render_template("home/project.html")
        user = session.get("user_id")
        get_project_by_user = ProjectUserServiceDb.verify_project_by_user_id(user_id=user)

        return render_template("home/project.html", projects=get_project_by_user.data)
    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))


@project_blueprint.route("/project/<uuid:project_id>", methods=["POST"])
@login_required
def project_post(project_id):
    """
    Docstring for projects
    """
    print("Chegou nessa função")
    return redirect(url_for("home.home"))
