"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required
from app.server.domain.models.user.user_repository import UserService
from app.server.services.project_service import register_project

new_project_blueprint = Blueprint("project/create", __name__)


@new_project_blueprint.route("/project/create", methods=["GET", "POST"])
@login_required
def create_get():
    """
    Docstring for create_get
    """
    if session.get("user_id") is not None:
        if request.method == "POST":
            user = UserService.verifty_user_by_user_id(user=session.get("user_id"))
            response = register_project(data=request.form, user_information=user.data)
            if response.status is False:
                flash(response.error_data, "error")
                return redirect(url_for("project/create.create_get"))
            return redirect(url_for("project.project_get_post"))
        return render_template("home/create_project.html")

    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))
