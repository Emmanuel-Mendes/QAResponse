from flask import Flask, redirect, url_for
from server.controllers.auth.login import login_blueprint
from server.controllers.auth.create_user import create_blueprint
from server.controllers.blog import initial_blueprint
from server.controllers.auth.recover_password import recover_password_blueprint


def creat_app() -> Flask:
    app = Flask(__name__)     
    app.register_blueprint(login_blueprint)
    app.register_blueprint(create_blueprint)
    app.register_blueprint(initial_blueprint)
    app.register_blueprint(recover_password_blueprint)
    app.secret_key = "sua-chave-aqui"
    
    @app.route("/")
    def index():
        return redirect(url_for("login.login"))
    
    return app
    
if __name__ == "__main__":
    creat_app().run(debug=True)