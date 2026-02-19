"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required

new_project_blueprint = Blueprint("project/create", __name__)


@new_project_blueprint.route("/project/create", methods=["GET", "POST"])
@login_required
def create_get():
    """
    Docstring for create_get
    """
    if session.get("user_id") is not None:
        if request.method == "POST":
            project_name = request.form.get("project_name")
            public_name = bool(request.form.get("public_project"))
            print(public_name)
            project_name_is_none = project_name is None or project_name.strip() == ""
            if project_name_is_none is True:
                flash("Nome do projeto não pode ser vazio", "error")
                return redirect(url_for("project/create.create_get"))
            return redirect(url_for("project.project"))
        return render_template("home/create_project.html")

    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))
