"""
Controller blog
"""

from flask import Blueprint, redirect, render_template, session, url_for

initial_blueprint = Blueprint("blog", __name__)


@initial_blueprint.route("/blog")
def blog():
    """
    Docstring for blog
    """
    if "user" not in session:
        return redirect(url_for("login.login"))

    return render_template("base.html", user=session["user"])


@initial_blueprint.route("/blog")
def logout():
    """
    Docstring for logout
    """
    session.clear()
    return redirect(url_for("home.logout"))
