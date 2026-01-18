from flask import render_template, redirect, url_for, session, Blueprint

from ..auth.login import login_required

projects_blueprint = Blueprint("projects", __name__)


@projects_blueprint.route("/projects", methods=["GET"])
@login_required
def projects_get():
    try:
        if session.get("user_id") is not None:
            return render_template("home/home.html")
        else:
            return redirect(url_for("login.login"))
    except Exception as e:
        print("Exception: ", e)


@projects_blueprint.route("/projects", methods=["POST"])
def projects():
    print("Post: ")
    print(session.get)
