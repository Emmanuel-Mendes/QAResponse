"""
Project repository
"""

from sqlalchemy.exc import SQLAlchemyError

from app.server.database.user_data_source import db as database
from app.server.domain.models.projects.projects import Project
from app.server.domain.models.user.user import User
from app.server.helper.response import Response


class ProjectUseRepository(database.Model):
    """
    Docstring for ProjectRepository
    """

    __tablename__ = "project_bind_user"

    user_id = database.Column(database.Uuid, database.ForeignKey('users.user_id'), primary_key=True)
    project_id = database.Column(database.Uuid, database.ForeignKey('projects.project_id'), primary_key=True)
    created_user_project = database.Column(database.Boolean)

    is_author = database.Column(database.Boolean, default=False, nullable=False, index=True)
    joined_at = database.Column(database.DateTime, default=database.func.now())

    # Back-populates para navegação bidirecional
    user = database.relationship("UserRepository", back_populates="project_memberships")
    project = database.relationship("ProjectRepository", back_populates="user_memberships")


class ProjectUserServiceDb:
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
            # add_project = ProjectUseRepository()

            """
            add_project.project_id = user_request.project_id
            add_project.created_user_project = user_request.created
            add_project.user_id = user_request.user_id
            """

            user_link = ProjectUserServiceDb(
                user_id=user_request.user_id, 
                project_id=user_request.project_id, 
                is_author=user_request.created
            )
            database.session.add(instance=user_link)
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
        get_user = ProjectUseRepository()
        user_get = get_user.query.filter_by(email=user).first()
        if user_get is not None:
            return Response.success(data=user_get)
        else:
            return Response.error(error="Usuário ou senha errado")

    @classmethod
    def verify_project_by_user_id(cls, user: User) -> Response:
        """
        Docstring for verifty_user_by_email

        :param self: Description
        :param user: Description
        :type user: User
        :return: Description
        :rtype: Response
        """
        try:
            get_project = ProjectUseRepository()
            # user_get = get_project.query.filter_by(user_id=user).all()

            resultado = get_project.query(get_project.c.project_id).filter(get_project.c.user_id == 1).all()

            print(resultado)
            if resultado is not None:
                return Response.success(data=resultado)
            else:
                return Response.error(error="Usuário ou senha errado")

        except AttributeError as e:
            print("AttributeError: ", e)
            return Response.error(error="Erro interno, tente novamente")
        except TypeError as e:
            print("TypeErro: ", e)
            return Response.error(error="Erro interno, tente novamente")
        except SQLAlchemyError as e:
            print("Error banco de dado: ", e)
            return Response.error(error="Erro interno, tente novamente")
