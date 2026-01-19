"""
Docstring for app.server.domain.service.user_service
"""

from app.extensions import bcrypt
from app.server.helper.response import Response


class UserService:
    """
    Docstring for UserService
    """

    @classmethod
    def set_password_cript(cls, password) -> Response:
        """
        Docstring for set_password_cript

        :param self: Description
        :param password: Description
        :return: Description
        :rtype: Response
        """
        if password < 8:
            return Response.error("Tamanho da senha inferior a suportada")

        return Response.success()

    @classmethod
    def verify_password_check(cls, hash_password, passoword) -> Response:
        """
        Docstring for verify_password_check

        :param self: Description
        :param hash: Description
        :param passoword: Description
        :return: Description
        :rtype: Response
        """
        response = bcrypt.check_password_hash(password=passoword, pw_hash=hash_password)
        if response:
            return Response.success(data="success")
        return Response.error(error="Usuário ou senha inválido")
