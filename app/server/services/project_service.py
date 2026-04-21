"""
Docstring for app.server.service.user_service
"""

# External imports
import uuid
from datetime import datetime

# Internal imports
from app.server.domain.models.projects.projects import Project
from app.server.domain.models.projects.projects_repository import ProjectServiceDatabase
from app.server.domain.models.projects.projects_repository_by_users import ProjectUserServiceDb
from app.server.helper.response import Response


def register_project(data, user_information) -> Response:
    """
    Docstring for register_user

    :param data: Description
    :type data: dict
    :return: Description
    :rtype: Response
    """
    project_obj = Project

    project_obj.title = data.get("project_name")
    project_obj.description = data.get("project_description")
    project_obj.publish = bool(data.get("public_project"))

    project_obj.data_created = datetime.now()
    project_obj.data_update = datetime.now()
    project_obj.project_id = uuid.uuid4()
    project_obj.created = True
    project_obj.user_id = user_information.user_id

    project_title = not project_obj.title
    if project_title is True:
        return Response.error(error="Título é obrigatório")
    print(f"\n --- {datetime.now()} Registrando projeto --- \n")

    insert_project = ProjectServiceDatabase.add_project(user_request=project_obj)
    print(f" --- {datetime.now()} Projeto registrado com {insert_project.__dict__} --- \n")

    if insert_project.status:
        print(f" --- {datetime.now()} Vinculando projeto a usuário --- \n")
        result = project_bind_user(project_obj)
        print(f" --- {datetime.now()} Resultado do vinculo {result.__dict__}--- \n")
        return Response.success(data="success")
    return Response.error(error=insert_project.error_data)


def project_bind_user(data) -> Response:
    """
    Docstring for project_bind_user

    :param data: Description
    :type data: dict
    :return: Description
    :rtype: Response
    """
    print(f" --- {datetime.now()} Service vincula projeto a usuário --- \n")
    project_by_user = ProjectUserServiceDb.add_project_by_user(user_request=data)
    print(f" --- {datetime.now()} Retorno do service: {project_bind_user.__dict__} --- \n")

    if project_by_user.success:
        return Response.success(data="success")
    return Response.error(error=project_by_user.error_data)


def consult_project_by_user(user) -> Response:
    """
    Docstring for register_user

    :param data: Description
    :type data: dict
    :return: Description
    :rtype: Response
    """

    project_by_user = ProjectUserServiceDb.verify_project_by_user_id(user_id=user)

    print(project_by_user)

    # return Response.success(data="success")
    # return Response.error(error=insert_project.error_data)
