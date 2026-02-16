"""
External imports
"""

import logging

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError

from app.config import Config
from app.extensions import bcrypt
from app.server.database.user_data_source import db

# Carrega as variáveis de ambiente antes de tudo
load_dotenv()


def create_app() -> Flask:
    # pylint: disable=import-outside-toplevel
    """
    Factory para criação do Flask App
    """
    app_setup = Flask(
        __name__,
        static_folder="templates/static",
    )

    # 1. Configuração do App
    app_setup.config.from_object(Config)

    # 2. Inicialização de Extensões
    bcrypt.init_app(app_setup)
    db.init_app(app_setup)

    # 3. Importação e Registro de Blueprints
    # Usamos importação local para evitar Circular Imports
    try:
        from app.server.controllers.auth.create_user import create_blueprint
        from app.server.controllers.auth.login import login_blueprint
        from app.server.controllers.auth.recover_password import (
            recover_password_blueprint,
        )
        from app.server.controllers.blog import initial_blueprint
        from app.server.controllers.components.error import error_blueprint
        from app.server.controllers.home.create_project import new_project_blueprint
        from app.server.controllers.home.home import home_blueprint
        from app.server.controllers.home.project import project_blueprint

        app_setup.register_blueprint(login_blueprint)
        app_setup.register_blueprint(create_blueprint)
        app_setup.register_blueprint(initial_blueprint)
        app_setup.register_blueprint(recover_password_blueprint)
        app_setup.register_blueprint(home_blueprint)
        app_setup.register_blueprint(new_project_blueprint)
        app_setup.register_blueprint(error_blueprint)
        app_setup.register_blueprint(project_blueprint)

    except ImportError as import_error:
        print(f"Erro crítico ao importar Blueprints: {import_error}")
        raise import_error

    # 4. Contexto do Banco de Dados
    with app_setup.app_context():
        # IMPORTANTE: Importe seus modelos aqui para o SQLAlchemy encontrá-los
        # Altere para o caminho correto onde seus Models (User, etc) estão
        try:
            db.create_all()
        except SQLAlchemyError as sql_error:
            logging.exception(sql_error)

    # 5. Rota Principal
    @app_setup.route("/")
    def index():
        # Verifique se o nome do blueprint é 'login' e a função é 'login'
        return redirect(url_for("login.login"))

    return app_setup
