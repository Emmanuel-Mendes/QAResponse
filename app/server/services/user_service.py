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
    print(data)
    user_obj = User

    user_obj.name = data["name"]
    user_obj.email = data["email"]
    password = data["password"]
    password_confirm = data["password_confirm"]
    user_obj.phone = data["phone"]

    name = not user_obj.name
    if name is True:
        return Response.error(error="Nome é obrigatório")

    email_is_none = not user_obj.email
    if email_is_none:
        print("Entrou nesse segundo if")
        return Response.error(error="Email é obrigatório")

    phone_is_none = not user_obj.phone
    if phone_is_none:
        return Response.error(error="Telefone é obrigatório")

    password_is_none = not user_obj.password
    password_confirm_is_none = not user_obj.password
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
