from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint, Response

home_blueprint = Blueprint("home", __name__)

# Usuário de exemplo (apenas para fins didáticos)

@home_blueprint.route("/home", methods=["GET"])
def home():  
    return render_template("home/home.html")

@home_blueprint.route("/home", methods=["POST"])
def homerequest():
    if request.method == "POST":        
        email = request.form.get("email")
        password = request.form.get("password")       
                
        email_is_none = email is None or email.strip() == ''  
        password_is_none = password is None or password.strip() == ''   
                
        if email_is_none and password_is_none == False:
            flash("Email não pode ser vazio", "error")
            return redirect(url_for('login.login'))
        if email_is_none == False and password_is_none:
            flash("Senha não pode ser vazio", "error")
            return redirect(url_for('login.login'))
        if email_is_none and password_is_none:
            flash("Email e Senha não podem ser vazios", "error")
            return redirect(url_for('login.login'))        
        else:
            return redirect(url_for("home.home"))
    
    return render_template("auth/login.html")

