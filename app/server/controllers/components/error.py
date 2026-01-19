"""
Docstring for app.server.controllers.components.error
"""

from flask import Blueprint, render_template

error_blueprint = Blueprint("error", __name__)


@error_blueprint.errorhandler(404)
def page_not_found():
    """
    Docstring for page_not_found
    """
    # Note que retornamos o template E o código 404 explicitamente
    return render_template("/components/errors/404.html"), 404


@error_blueprint.errorhandler(500)
def internal_server_error():
    """
    Docstring for internal_server_error
    """
    return render_template("/components/errors/500.html"), 500
