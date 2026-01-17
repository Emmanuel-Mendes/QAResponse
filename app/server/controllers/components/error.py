from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint, Response


error_blueprint = Blueprint("error", __name__)

@error_blueprint.errorhandler(404)
def page_not_found(e):
    # Note que retornamos o template E o código 404 explicitamente
    return render_template('/components/errors/404.html'), 404

@error_blueprint.errorhandler(500)
def internal_server_error(e):
    return render_template('/components/errors/500.html'), 500