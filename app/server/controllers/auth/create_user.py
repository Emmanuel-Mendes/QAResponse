from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from ...domain.models.user.user import User
from ...domain.models.user.user_repository import UserRepository, UserService
from ...enum.enum_user import User_type, User_status
from datetime import datetime
from flask_bcrypt import generate_password_hash
import uuid
import time

create_blueprint = Blueprint("create", __name__)

@create_blueprint.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        
        user = User
        user.name = request.form.get("name")
        user.email = request.form.get("email")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        user.phone = request.form.get("phone")        
        
        name_is_none = user.name is None or user.name.strip() == '' 
        if name_is_none:
            flash("Nome é obrigatório", "error")
            return redirect(url_for('create.create_user'))
        
        email_is_none = user.email is None or user.email.strip() == ''  
        if email_is_none:
            flash("Email é obrigatório", "error")
            return redirect(url_for('create.create_user'))   
            
        phone_is_none = user.phone is None or user.phone.strip() == ''             
        if phone_is_none:
            flash("Telefone é obrigatório", "error")
            return redirect(url_for('create.create_user'))
        
        password_is_none = password is None or password.strip() == ''
        password_confirm_is_none = password_confirm is None or password_confirm.strip() == '' 
        if password_is_none or password_confirm_is_none:
            flash("Senha é obrigatório", "error")
            session.clear()
            return redirect(url_for('create.create_user'))    
                
        if password != password_confirm:
            flash("Senhas não coincidem", "error")
            return redirect(url_for('create.create_user'))         
        else: 
            user.data_created = datetime.now()
            user.data_update = datetime.now()
            user.user_id = uuid.uuid4()
            user.status_user = True
            user.user_type = User_type.normal.value  
            user.password = generate_password_hash(password).decode('utf-8')
                            
            insert_user = UserService.add_user(user_request = user)
            if (insert_user.status):
                return redirect(url_for('login.login'))                
            else: 
                try:
                    if insert_user.data == User_status.user_created.value:      
                        flash("Usuário já cadastrado", "error")  
                        return redirect(url_for('login.login'))                     
                    else:                      
                        flash(insert_user.error, "error")
                        return redirect(url_for('create.create_user'))
                except Exception as e:
                    flash(insert_user.error, "error")
                    return redirect(url_for('create.create_user'))
                    
                
    return render_template("auth/register.html")
    
