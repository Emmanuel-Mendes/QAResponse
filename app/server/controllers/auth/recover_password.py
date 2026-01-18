from flask import render_template, request, redirect, url_for, flash, Blueprint

recover_password_blueprint = Blueprint("recover_password", __name__)


@recover_password_blueprint.route("/recover", methods=["GET"])
def recover_password():
    return render_template("auth/recover_password.html")


@recover_password_blueprint.route("/recover", methods=["POST"])
def recover_password_request():
    email = request.form.get("email_recover")

    print("Email: ", email)
    email_is_none = email is None or email.strip() == ""

    if email_is_none:
        flash("Email não pode ser vazio", "error")
        return redirect(url_for("recover_password.recover_password"))
    else:
        return redirect(url_for("recover_password.recover_password"))
