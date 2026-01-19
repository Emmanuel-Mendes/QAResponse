"""
Home controller
"""

from flask import Blueprint, redirect, render_template, session, url_for

from app.server.controllers.auth.login import login_required

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/home", methods=["GET"])
@login_required
def home():
    """
    Docstring for home
    """
    if session.get("user_id") is not None:
        return render_template("home/home.html")
    return redirect(url_for("login.login"))


@home_blueprint.route("/home", methods=["POST"])
@login_required
def home_request():
    """
    Docstring for home_request
    """
    print("Post: ")
    print(session.get)
