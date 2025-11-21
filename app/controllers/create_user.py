from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint

create_blueprint = Blueprint("create", __name__)

@create_blueprint.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")        
        print("Teste: ",name, email, password)

    return render_template("auth/register.html")
