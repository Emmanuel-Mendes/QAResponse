"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required
from app.server.domain.models.projects.projects_repository_by_users import ProjectUserServiceDb

project_blueprint = Blueprint("project", __name__)


@project_blueprint.route("/project", methods=["GET", "POST"])
@login_required
def project_get_post():
    """
    Docstring for create_get
    """

    dados_usuarios = [
        {"id": 1, "title": "Alice Souza", "description": "Desenvolvedora"},
        {"id": 2, "title": "Bruno Lima", "description": "Designer"},
        {"id": 3, "title": "Emmanuel", "description": "QA"},
        {"id": 4, "title": "Thayná", "description": "Biologa"},
    ]
    if session.get("user_id") is not None:
        if request.method == "POST":
            return render_template("home/project.html")
        user = session.get("user_id")
        print(user)
        get_project_by_user = ProjectUserServiceDb.verify_project_by_user_id(user=user)

        print(get_project_by_user.data)

        return render_template("home/project.html", projects=dados_usuarios)
    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))
