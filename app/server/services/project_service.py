"""
Docstring for app.server.service.user_service
"""

# External imports
import uuid
from datetime import datetime

# Internal imports
from app.server.domain.models.projects.projects import Project
from app.server.domain.models.projects.projects_repository import ProjectServiceDatabase
from app.server.domain.models.projects.projects_repository_by_users import ProjectByUserServiceDatabase
from app.server.helper.response import Response


def register_project(data, user_information) -> Response:
    """
    Docstring for register_user

    :param data: Description
    :type data: dict
    :return: Description
    :rtype: Response
    """
    try:
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

        insert_project = ProjectServiceDatabase.add_project(user_request=project_obj)
        if insert_project.status:
            project_bind_user(project_obj)
            return Response.success(data="success")
        return Response.error(error=insert_project.error_data)

    except Exception:
        return Response.error(error="Error interno, tente novamente")


def project_bind_user(data) -> Response:
    try:
        project_by_user = ProjectByUserServiceDatabase.add_project_by_user(user_request=data)

        if project_by_user.success:
            return Response.success(data="success")
        return Response.error(error=project_by_user.error_data)

    except Exception:
        return Response.error(error="Error interno, tente novamente")
