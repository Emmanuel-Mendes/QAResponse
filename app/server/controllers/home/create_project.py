"""
create project controller
"""

from flask import Blueprint, redirect, render_template, session, url_for

from app.server.controllers.auth.login import login_required

new_project_blueprint = Blueprint("home/project/create", __name__)


@new_project_blueprint.route("/home/project/create", methods=["GET"])
@login_required
def create_get():
    """
    Docstring for create_get
    """
    if session.get("user_id") is not None:
        return render_template("home/create_project.html")
    return redirect(url_for("login.login"))


@new_project_blueprint.route("/home/project/create", methods=["POST"])
@login_required
def create_post():
    """
    Docstring for create_post
    """
    print("Post: ")
    print(session.get)
