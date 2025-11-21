from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint, Response

login_blueprint = Blueprint("login", __name__)

# Usuário de exemplo (apenas para fins didáticos)
USER_DB = {
    "name": "Thayná Carla",
    "email": "thaynacbaraujo@gmail.com",
    "password": "123456"
}


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if email == USER_DB["email"] and password == USER_DB["password"]:
            session["user"] = name
            return redirect(url_for("home.home"))
        else:
            flash("Usuário ou senha inválidos!", "error")

    return render_template("auth/login.html")

