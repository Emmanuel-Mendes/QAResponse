from flask import Flask, redirect, url_for

from server.domain.models.user.user_repository import UserRepository
from server.controllers.auth.login import login_blueprint
from server.controllers.auth.create_user import create_blueprint
from server.controllers.blog import initial_blueprint
from server.controllers.auth.recover_password import recover_password_blueprint
from server.controllers.home.home import home_blueprint
from server.database.user_data_source import db



def creat_app() -> Flask:
    try:
        app = Flask(__name__,static_folder='templates/static',)  
        
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"   

        db.init_app(app=app)
        
        app.secret_key = "sua-chave-aqui"
            
        app.register_blueprint(login_blueprint)
        app.register_blueprint(create_blueprint)
        app.register_blueprint(initial_blueprint)
        app.register_blueprint(recover_password_blueprint)
        app.register_blueprint(home_blueprint)
        
        
        with app.app_context():
            db.create_all()
        
        @app.route("/")
        def index():
            return redirect(url_for("login.login"))
        
    except Exception as e:
        print("Exception: ", e)
    return app
    
if __name__ == "__main__":
    creat_app().run(debug=True)