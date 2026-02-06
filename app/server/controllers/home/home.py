"""
Home controller
"""

from flask import Blueprint, redirect, render_template, url_for

from app.server.controllers.auth.login import login_required
from app.server.utils.session import get_session

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/home", methods=["GET"])
@login_required
def home():
    """
    Docstring for home
    """
    user_session_validate = get_session()
    if user_session_validate:
        return render_template("home/home.html")
    return redirect(url_for("login.login"))


@home_blueprint.route("/home", methods=["POST"])
@login_required
def home_request():
    """
    Docstring for home_request
    """
    return None
