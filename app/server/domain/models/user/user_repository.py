"""
User repository
"""

import uuid

from sqlalchemy.exc import SQLAlchemyError

from app.server.database.user_data_source import db as database
from app.server.enum.enum_user import UserStatus
from app.server.helper.response import Response

from .user import User


class UserRepository(database.Model):
    """
    Docstring for UserRepository
    """

    __tablename__ = "users"

    id = database.Column(database.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = database.Column(database.String(50), nullable=True)
    password = database.Column(database.String(200), nullable=True)
    email = database.Column(database.String(75), unique=True, nullable=True)
    phone = database.Column(database.String(75), nullable=True)
    status_user = database.Column(database.Boolean, nullable=True)
    user_id = database.Column(database.String(100), unique=True, nullable=True)
    data_created = database.Column(database.String(100), nullable=True)
    data_update = database.Column(database.String(100), nullable=True)
    user_type = database.Column(database.String(100), nullable=True)


class UserService:
    """
    Docstring for UserService
    """

    @classmethod
    def add_user(cls, user_request: User) -> Response:
        """
        Docstring for add_user

        :param self: Description
        :param user_request: Description
        :type user_request: User
        :return: Description
        :rtype: Response
        """
        try:
            add_user = UserRepository()

            add_user.name = user_request.name
            add_user.password = user_request.password
            add_user.email = user_request.email
            add_user.phone = user_request.phone
            add_user.status_user = user_request.status_user
            add_user.user_id = user_request.user_id
            add_user.data_created = user_request.data_created
            add_user.data_update = user_request.data_update
            add_user.user_type = user_request.user_type

            database.session.add(instance=add_user)
            database.session.commit()
            return Response.success(data=UserStatus.USER_CREATED.value)
        except SQLAlchemyError:
            return Response.error(error="Usuário já cadastrado")

    @classmethod
    def verifty_user_by_email(cls, user: User) -> Response:
        """
        Docstring for verifty_user_by_email

        :param self: Description
        :param user: Description
        :type user: User
        :return: Description
        :rtype: Response
        """
        get_user = UserRepository()
        user_get = get_user.query.filter_by(email=user).first()
        if user_get is not None:
            return Response.success(data=user_get)

        return Response.error(error="Usuário ou senha errado")
