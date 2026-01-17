from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint, Response
from ..auth.login import login_required
from ...controllers.components.error import internal_server_error

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/home", methods=["GET"])
@login_required
def home():  
    try:
        if session.get('user_id') is not None:
            return render_template("home/home.html")
        else:         
            return redirect(url_for('login.login'))   
    except Exception as e:
        internal_server_error(e=e)
    except RuntimeError as e:
        print("Caiu nesse error: ", e)

@home_blueprint.route("/home", methods=["POST"])
@login_required
def home_request(): 
    print("Post: ")
    print(session.get)      
