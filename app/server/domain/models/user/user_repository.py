import uuid

from ....database.user_data_source import db as database
from ....enum.enum_user import User_status
from ....helper.response import Response
from .user import User


class UserRepository(database.Model):
    __tablename__ = "users"

    id = database.Column(
        database.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
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
    @classmethod
    def add_user(self, user_request: User) -> Response:
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
            return Response.success(data=User_status.user_created.value)

        except BaseException:
            return Response.error(
                error="Usuário já cadastrado", data=User_status.user_created.value
            )
        except Exception:
            return Response.error(error="Verifique os campos preenchidos")

    @classmethod
    def verifty_user_by_email(self, user: User) -> Response:
        getUser = UserRepository()
        user_get = getUser.query.filter_by(email=user).first()
        if user_get is not None:
            return Response.success(data=user_get)
        else:
            return Response.error(error="Usuário ou senha errado")

    @classmethod
    def createUser(self, user: User) -> Response:
        return False

    @classmethod
    def deleteUser(self, user: User) -> Response:
        return False
