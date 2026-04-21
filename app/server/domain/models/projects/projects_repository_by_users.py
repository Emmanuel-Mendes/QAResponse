"""
Project repository
"""

import uuid
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from app.server.database.user_data_source import db as database
from app.server.domain.models.projects.projects import Project
from app.server.domain.models.projects.projects_repository import ProjectRepository
from app.server.domain.models.user.user import User
from app.server.helper.response import Response


class ProjectUseRepository(database.Model):
    """
    Docstring for ProjectRepository
    """

    __tablename__ = "project_bind_user"

    bind_id = database.Column(
        database.Uuid, unique=True, nullable=True, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id = database.Column(database.Uuid, database.ForeignKey("users.user_id"))
    project_id = database.Column(database.Uuid, database.ForeignKey("projects.project_id"))
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
            print(f" --- {datetime.now()} Vinculando projeto a usuário --- \n")
            new_user = user_request.user_id
            print(f" --- {datetime.now()} user_id {new_user} --- \n")

            new_project = user_request.project_id
            print(f" --- {datetime.now()} project_id {new_project} --- \n")

            user_link = ProjectUseRepository(user_id=new_user, project_id=new_project, is_author=user_request.created)
            print(f" --- {datetime.now()} user_link: {user_link.__dict__}--- \n")

            database.session.add(instance=user_link)
            database.session.commit()
            return Response.success(data="Success")
        except TypeError as e:
            print(f" --- {datetime.now()} Erro TypeError ao vincular projeto a usuário: {e} --- \n")
            return Response.error(error="Erro interno, tente novamente")
        except SQLAlchemyError as e:
            print(f" --- {datetime.now()} Erro SQLAlchemyError ao vincular projeto a usuário: {e} --- \n")
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
        return Response.error(error="Usuário ou senha errado")

    @classmethod
    def verify_project_by_user_id(cls, user_id: User) -> Response:
        """
        Docstring for verifty_user_by_email

        :param self: Description
        :param user: Description
        :type user: User
        :return: Description
        :rtype: Response
        """
        try:
            resultado = (
                database.session.query(
                    ProjectRepository.project_id, ProjectRepository.project_title, ProjectRepository.project_description
                )
                .join(ProjectUseRepository)
                .filter(ProjectUseRepository.user_id == user_id)
                .all()
            )
            print(f"n --- {datetime.now()} - Resultado: {[r._asdict() for r in resultado]}--- \n")

            if resultado is not None:
                return Response.success(data=[r._asdict() for r in resultado])
            print(f"\n --- {datetime.now()} - Projeto não encontrado: {resultado} --- \n")
            return Response.error(error="Informações erradas")

        except AttributeError as e:
            print(f"\n --- {datetime.now()} - Repository AttributeError: {e} --- \n")
            return Response.error(error="Erro interno, tente novamente")
        except TypeError as e:
            print(f"\n --- {datetime.now()} - Repository TypeError: {e} --- \n")
            return Response.error(error="Erro interno, tente novamente")
        except SQLAlchemyError as e:
            print(f"\n --- {datetime.now()} - Repository SQLAlchemyError: {e} --- \n")
            return Response.error(error="Erro interno, tente novamente")
