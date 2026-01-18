from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from functools import wraps


from ..components.error import internal_server_error
from ...domain.models.user.user_repository import UserService
from ...domain.service.user_service import UserService as userServiceDto

login_blueprint = Blueprint("login", __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            print("Entrou nesse if")
            return redirect(url_for('login.login')) 
        return f(*args, **kwargs)
    return decorated_function

@login_blueprint.route("/login", methods=["GET"])
def login(): 
    try:
        return render_template("auth/login.html")
    except Exception as e:
        print("Exceção: ",e)
        internal_server_error(e=e)

@login_blueprint.route("/login", methods=["POST"])
def login_request():
    try:        
        if request.method == "POST":        
            email = request.form.get("email")
            password = request.form.get("password")   
            email_is_none = email is None or email.strip() == ''  
            password_is_none = password is None or password.strip() == ''   
                    
            if email_is_none and not password_is_none:
                flash("Email não pode ser vazio", "error")
                return redirect(url_for('login.login'))
            if not email_is_none and password_is_none:
                flash("Senha não pode ser vazio", "error")
                return redirect(url_for('login.login'))
            if email_is_none and password_is_none:
                flash("Email e Senha não podem ser vazios", "error")
                return redirect(url_for('login.login'))        
            else:
                verify_user = UserService.verifty_user_by_email(email)
                if(verify_user.status and verify_user.data.user_id is not None):
                    password_validate = userServiceDto.verify_password_check(passoword=password, hash=verify_user.data.password) 
                    if password_validate.status:
                        session["user_id"] = verify_user.data.user_id
                        return redirect(url_for('home.home'))
                    else:   
                        session.clear()
                        flash(password_validate.error, "error")
                        return redirect(url_for('login.login')) 
                else:
                    session.clear()
                    flash(verify_user.error, "error")
                    return redirect(url_for('login.login'))   
                        
    except Exception:
        flash("Erro ao realizar login", "error")
        return redirect(url_for('login.login'))
