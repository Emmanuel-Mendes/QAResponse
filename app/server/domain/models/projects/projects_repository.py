"""
Project repository
"""

from sqlalchemy.exc import SQLAlchemyError

from app.server.database.user_data_source import db as database
from app.server.domain.models.projects.projects import Project
from app.server.helper.response import Response


class ProjectRepository(database.Model):
    """
    Docstring for ProjectRepository
    """

    __tablename__ = "project"

    id = database.Column(database.Integer, primary_key=True)
    project_title = database.Column(database.String(50), nullable=True)
    project_description = database.Column(database.String(200), nullable=True)
    project_id = database.Column(database.String(100), unique=True, nullable=True)
    created_project = database.Column(database.Boolean)
    data_created = database.Column(database.String(150), nullable=True)
    data_update = database.Column(database.String(150), nullable=True)
    data_publish = database.Column(database.Boolean, nullable=True)


class ProjectServiceDatabase:
    """
    Docstring for UserService
    """

    @classmethod
    def add_project(cls, user_request: Project) -> Response:
        """
        Docstring for add_user

        :param self: Description
        :param user_request: Description
        :type user_request: User
        :return: Description
        :rtype: Response
        """
        try:
            add_project = ProjectRepository()

            add_project.project_title = user_request.title
            add_project.project_description = user_request.description
            add_project.project_id = user_request.project_id
            add_project.created_project = user_request.created
            add_project.data_created = user_request.data_created
            add_project.data_update = user_request.data_update
            add_project.data_publish = user_request.publish

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
        get_user = ProjectRepository()
        user_get = get_user.query.filter_by(email=user).first()
        if user_get is not None:
            return Response.success(data=user_get)
        else:
            return Response.error(error="Usuário ou senha errado")

    @classmethod
    def verifty_project_by_project_id(cls, id_project: Project) -> Response:
        """
        Docstring for verifty_user_by_email

        :param self: Description
        :param user: Description
        :type user: User
        :return: Description
        :rtype: Response
        """
        get_user = ProjectRepository()
        user_get = get_user.query.filter_by(project_id=id_project.project_id).first()
        if user_get is not None:
            return Response.success(data=user_get)
        else:
            return Response.error(error="Projeto não localizado")
