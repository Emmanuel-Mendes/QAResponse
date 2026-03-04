"""Módulos externos"""

import uuid
from datetime import datetime


class Project:
    """
    Class for User
    """

    def __init__(
        self,
        _title: str,
        _project_id: str = "",
        _description: str = "",
        _user_id: str = "",
        _created: bool = True,
        _publish: bool = False,
        _data_created: datetime = "",
        _data_update: datetime = "",
    ):
        self.title = _title
        self.user_id = _user_id
        self.description = _description
        self.created = _created
        self.project_id = _project_id
        self.publish = _publish
        self.data_created = _data_created
        self.data_update = _data_update

    # --- Getter and Setter title --- #
    @property
    def title(self):
        """
        Docstring for title

        :param self: Description
        """
        return getattr(self.title)

    @title.setter
    def title(self, title_value: str):
        """
        Docstring for title

        :param self: Description
        :param title_value: Description
        :type title_value: str
        """
        try:
            self.title = title_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo password") from e
        except Exception as e:
            raise ValueError("Error no campo password") from e

    # --- Getter and Setter title --- #
    @property
    def user_id(self):
        """
        Docstring for title

        :param self: Description
        """
        return getattr(self.user_id)

    @user_id.setter
    def user_id(self, user_id_value: str):
        """
        Docstring for title

        :param self: Description
        :param title_value: Description
        :type title_value: str
        """
        try:
            self.user_id = user_id_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo password") from e
        except Exception as e:
            raise ValueError("Error no campo password") from e

    # --- Getter and Setter description --- #
    @property
    def description(self):
        """
        Docstring for title

        :param self: Description
        """
        return getattr(self.description)

    @description.setter
    def description(self, description_value: str):
        """
        Docstring for title

        :param self: Description
        :param description_value: Description
        :type description_value: str
        """
        try:
            self.description = description_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo password") from e
        except Exception as e:
            raise ValueError("Error no campo password") from e

    # --- Getter and Setter created --- #
    @property
    def created(self):
        """
        Docstring for created

        :param self: Description
        """
        return getattr(self.created)

    @created.setter
    def created(self, created_value: str):
        """
        Docstring for created

        :param self: created
        :param created_value: Description
        :type created_value: str
        """
        try:
            self.created_value = created_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo informado") from e
        except Exception as e:
            raise ValueError("Error no campo informado") from e

    # --- Getter and Setter project_id --- #
    @property
    def project_id(self):
        """
        Docstring for project_id

        :param self: Description
        """
        print("Chamou essa função: ")
        return getattr(self.project_id)

    @project_id.setter
    def project_id(self):
        """
        Docstring for project_id

        :param self: project_id
        :param project_id_value: Description
        :type project_id_value: str
        """
        try:
            self.project_id = uuid.uuid4().__dict__
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo informado") from e
        except Exception as e:
            raise ValueError("Error no campo informado") from e

    # --- Getter and Setter publish --- #
    @property
    def publish(self):
        """
        Docstring for created

        :param self: Description
        """
        return getattr(self.publish)

    @publish.setter
    def publish(self, publish_value: str):
        """
        Docstring for publish

        :param self: publish
        :param publish_value: Description
        :type publish_value: str
        """
        try:
            self.publish = publish_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo informado") from e
        except Exception as e:
            raise ValueError("Error no campo informado") from e

    @property
    def data_created(self):
        """
        Docstring for data_created

        :param self: Description
        """
        return self.data_created

    @data_created.setter
    def data_created(self, data_created_value: datetime = ""):
        """
        Docstring for data_created

        :param self: Description
        :param data_created_value: Description
        :type data_created_value: datetime
        """
        try:
            if not data_created_value:
                self.data_created = datetime.now()
            else:
                self.data_created = data_created_value
        except TypeError as e:
            raise ValueError("Tipo inválido para usuário") from e
        except Exception as e:
            raise ValueError("Error no campo usuário") from e

    # --- Getter and Setter data_update --- #
    @property
    def data_update(self):
        """
        Docstring for data_update

        :param self: Description
        """
        return self.data_update

    @data_update.setter
    def data_update(self, data_update_value: datetime = ""):
        """
        Docstring for data_update

        :param self: Description
        :param data_update_value: Description
        :type data_update_value: datetime
        """
        try:
            if not data_update_value:
                self.data_update = datetime.now()
            else:
                self.data_update = data_update_value
        except TypeError as e:
            raise ValueError("Tipo inválido para atualização da data") from e
        except Exception as e:
            raise ValueError("Error para atualização da data") from e
