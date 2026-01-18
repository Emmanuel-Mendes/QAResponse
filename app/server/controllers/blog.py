from flask import render_template, redirect, url_for, session, Blueprint

initial_blueprint = Blueprint("blog", __name__)


@initial_blueprint.route("/blog")
def blog():
    if "user" not in session:
        return redirect(url_for("login.login"))

    return render_template("base.html", user=session["user"])


@initial_blueprint.route("/blog")
def logout():
    session.clear()
    return redirect(url_for("home.logout"))
