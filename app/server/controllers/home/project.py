"""
create project controller
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.server.controllers.auth.login import login_required

project_blueprint = Blueprint("home/project", __name__)


@project_blueprint.route("/home/project", methods=["GET", "POST"])
@login_required
def project():
    """
    Docstring for create_get
    """
    if session.get("user_id") is not None:
        if request.method == "POST":
            return render_template("home/project.html")
        usuarios = [
            {"nome": "Ana", "email": "ana@email.com", "status": "Ativo"},
            {"nome": "Bruno", "email": "bruno@email.com", "status": "Inativo"},
            {"nome": "Carla", "email": "carla@email.com", "status": "Ativo"},
        ]
        return render_template("home/project.html", titulo="Lista de Usuários", lista_usuarios=usuarios)

    flash("Acesse sua conta", "dialog")
    return redirect(url_for("login.login"))
