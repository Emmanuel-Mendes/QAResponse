"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required

project_blueprint = Blueprint("project", __name__)


@project_blueprint.route("/project", methods=["GET", "POST"])
@login_required
def project():
    """
    Docstring for create_get
    """
    if session.get("user_id") is not None:
        if request.method == "POST":
            return render_template("home/project.html")
        return render_template("home/project.html")
    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))
