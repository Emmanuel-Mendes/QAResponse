from flask import render_template, redirect, url_for, session, Blueprint
from ..auth.login import login_required

new_project_blueprint = Blueprint("home/project/create", __name__)


@new_project_blueprint.route("/home/project/create", methods=["GET"])
@login_required
def create_get():
    try:
        if session.get("user_id") is not None:
            return render_template("home/create_project.html")
        else:
            return redirect(url_for("login.login"))
    except Exception as e:
        print("Exception: ", e)


@new_project_blueprint.route("/home/project/create", methods=["POST"])
@login_required
def create_post():
    print("Post: ")
    print(session.get)
