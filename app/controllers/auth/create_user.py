from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint

create_blueprint = Blueprint("create", __name__)

@create_blueprint.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password") 
        password_confirm = request.form.get("password_confirm")
        phone = request.form.get("phone")
        
        
        name_is_none = name is None or name.strip() == '' 
        if name_is_none:
            flash("Nome não pode ser vazio", "error")
            return redirect(url_for('create.create_user'))
        
        email_is_none = email is None or email.strip() == ''  
        if email_is_none:
            flash("Email não pode ser vazio", "error")
            return redirect(url_for('create.create_user'))
        
        password_is_none = password is None or password.strip() == ''
        password_confirm_is_none = password_confirm is None or password_confirm.strip() == '' 
        if password_is_none or password_confirm_is_none:
            flash("Senha não pode ser vazio", "error")
            return redirect(url_for('create.create_user'))
               
              
        phone_is_none = phone is None or phone.strip() == ''             
        if phone_is_none:
            flash("Telefone não pode ser vazio", "error")
            return redirect(url_for('create.create_user'))
            

    return render_template("auth/register.html")
