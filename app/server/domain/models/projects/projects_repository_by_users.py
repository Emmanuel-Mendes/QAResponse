"""
Project repository
"""

from sqlalchemy.exc import SQLAlchemyError

from app.server.database.user_data_source import db as database
from app.server.domain.models.projects.projects import Project
from app.server.helper.response import Response


class ProjectByUserRepository(database.Model):
    """
    Docstring for ProjectRepository
    """

    __tablename__ = "project_bind_user"

    id = database.Column(database.Integer, primary_key=True)
    project_id = database.Column(database.String(50), nullable=True)
    user_id = database.Column(database.String(150), nullable=True)
    created_user_project = database.Column(database.Boolean)


class ProjectByUserServiceDatabase:
    """
    Docstring for UserService
    """

    @classmethod
    def add_project_by_user(cls, user_request: Project) -> Response:
        """
        Docstring for add_user

        :param self: Description
        :param user_request: Description
        :type user_request: User
        :return: Description
        :rtype: Response
        """
        try:
            add_project = ProjectByUserRepository()

            add_project.project_id = user_request.project_id
            add_project.created_user_project = user_request.created
            add_project.user_id = user_request.user_id

            database.session.add(instance=add_project)
            database.session.commit()
            return Response.success(data="Success")
        except TypeError as e:
            print("TypeErro: ", e)
        except SQLAlchemyError as e:
            print("Error banco de dado: ", e)
            return Response.error(error="Erro interno, tente novamente")

    @classmethod
    def verifty_project_by_email(cls, user: Project) -> Response:
        """
        Docstring for verifty_user_by_email

        :param self: Description
        :param user: Description
        :type user: User
        :return: Description
        :rtype: Response
        """
        get_user = ProjectByUserRepository()
        user_get = get_user.query.filter_by(email=user).first()
        if user_get is not None:
            return Response.success(data=user_get)
        else:
            return Response.error(error="Usuário ou senha errado")
