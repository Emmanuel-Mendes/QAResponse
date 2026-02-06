"""
External imports
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.server.services.user_service import register_user

create_blueprint = Blueprint("create", __name__)


@create_blueprint.route("/create", methods=["GET", "POST"])
def create_user() -> None:
    """
    Docstring for create_user
    """
    if request.method == "POST":
        response = register_user(data=request.form.to_dict())
        if response.error:
            flash(response.error_data, "error")
            return redirect(url_for("create.create_user"))
        flash("Acesse sua conta", "dialog")
        return redirect(url_for("login.login"))

    return render_template("auth/register.html")
