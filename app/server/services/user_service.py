"""
Docstring for app.server.service.user_service
"""

# External imports
import uuid
from datetime import datetime

from app.app import bcrypt

# Internal imports
from app.server.domain.models.user.user import User
from app.server.domain.models.user.user_repository import UserService
from app.server.enum.enum_user import UserType
from app.server.helper.response import Response


def register_user(data: dict) -> Response:
    """
    Docstring for register_user

    :param data: Description
    :type data: dict
    :return: Description
    :rtype: Response
    """
    user_obj = User

    user_obj.name = data["name"]
    user_obj.email = data["email"]
    password = data["password"]
    password_confirm = data["password_confirm"]
    user_obj.phone = data["phone"]

    name_is_none = user_obj.name is None or user_obj.name.strip() == ""
    if name_is_none:
        return Response.error(error="Nome é obrigatório")

    email_is_none = user_obj.email is None or user_obj.email.strip() == ""
    if email_is_none:
        return Response.error(error="Email é obrigatório")

    phone_is_none = user_obj.phone is None or user_obj.phone.strip() == ""
    if phone_is_none:
        return Response.error(error="Telefone é obrigatório")

    password_is_none = password is None or password.strip() == ""
    password_confirm_is_none = password_confirm is None or password_confirm.strip() == " "
    if password_is_none or password_confirm_is_none:
        return Response.error(error="Senha é obrigatório")

    if password != password_confirm:
        return Response.error(error="Senhas não coincidem")

    user_obj.data_created = datetime.now()
    user_obj.data_update = datetime.now()
    user_obj.user_id = uuid.uuid4()
    user_obj.status_user = True
    user_obj.user_type = UserType.NORMAL.value
    user_obj.password = bcrypt.generate_password_hash(password).decode("utf-8")

    insert_user = UserService.add_user(user_request=user_obj)

    if insert_user.status:
        return Response.success(data="success")
    return Response.error(error=insert_user.error_data)
