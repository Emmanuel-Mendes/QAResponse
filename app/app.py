from flask import Flask, redirect, url_for

from server.domain.models.user.user_repository import UserRepository
from server.controllers.auth.login import login_blueprint
from server.controllers.auth.create_user import create_blueprint
from server.controllers.blog import initial_blueprint
from server.controllers.auth.recover_password import recover_password_blueprint
from server.controllers.home.home import home_blueprint
from server.controllers.home.create_project import new_project_blueprint
from server.controllers.components.error import error_blueprint
from server.database.user_data_source import db
from extensions import bcrypt
from dotenv import load_dotenv
from config import Config

load_dotenv()


def create_app() -> Flask:
    try:
        
        app = Flask(__name__,static_folder='templates/static',)  
        bcrypt.init_app(app=app)
        
        app.config.from_object(Config)   
        
        db.init_app(app=app)        
            
        app.register_blueprint(login_blueprint)
        app.register_blueprint(create_blueprint)
        app.register_blueprint(initial_blueprint)
        app.register_blueprint(recover_password_blueprint)
        app.register_blueprint(home_blueprint)        
        app.register_blueprint(new_project_blueprint)  
        app.register_blueprint(error_blueprint)    
        
        with app.app_context():
            db.create_all()
        
        @app.route("/")
        def index():
            return redirect(url_for("login.login"))
        
    except Exception as e:
        print("Exception: ", e)
    finally:
        return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)