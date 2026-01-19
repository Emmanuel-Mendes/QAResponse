"""
User repository
"""

import uuid
from datetime import datetime

from app.server.enum.enum_user import UserType
from app.server.utils.user_utils import validate_email


class User:
    """
    Docstring for User
    """

    def __init__(
        self,
        _name: str,
        _password: str,
        _email: str,
        _phone: str,
        _status_user: bool = False,
        _user_id: str = "",
        _data_created: datetime = "",
        _data_update: datetime = "",
        _user_type: UserType = None,
    ):
        self.name = _name
        self.password = _password
        self.email = _email
        self.phone = _phone
        self.status_user = _status_user
        self.user_id = _user_id
        self.data_created = _data_created
        self.data_update = _data_update
        self.user_type = _user_type

    # --- Getter and Setter name --- #
    @property
    def name(self):
        """
        Docstring for name

        :param self: Description
        """
        return getattr(self.name)

    @name.setter
    def name(self, name_value: str):
        try:
            if not name_value or name_value < 3:
                raise ValueError("Tamanho inválido para o campo nome")
            else:
                self.name = name_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo password") from e
        except Exception as e:
            raise ValueError("Error no campo password") from e

    # --- Getter and Setter password --- #
    @property
    def password(self):
        """
        Docstring for password

        :param self: Description
        """
        return self.password

    @password.setter
    def password(self, password_value: str):
        """
        Docstring for password

        :param self: Description
        :param password_value: Description
        :type password_value: str
        """
        try:
            print("Chamou esse método")
            if not password_value or password_value.__len__ < 3:
                raise ValueError("Tamanho inválido para o campo password")
            else:
                self.password = password_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo password") from e
        except Exception as e:
            raise ValueError("Error no campo password") from e

    # --- Getter and Setter email --- #
    @property
    def email(self):
        """
        Docstring for email

        :param self: Description
        """
        return self.email

    @email.setter
    def email(self, email_value: str):
        """
        Docstring for email

        :param self: Description
        :param email_value: Description
        :type email_value: str
        """
        try:
            if not email_value or email_value < 3:
                raise ValueError("Tamanho inválido para o campo email")
            if not validate_email(email=email_value):
                raise ValueError("Email inválido")
            else:
                self.email = email_value
        except TypeError as e:
            raise ValueError("Tipo inválido para o campo email") from e
        except Exception as e:
            raise ValueError("Error no campo email") from e

    # --- Getter and Setter status_user --- #

    @property
    def status_user(self):
        """
        Docstring for status_user

        :param self: Description
        """
        return self.phone

    @status_user.setter
    def status_user(self, status_user_value: bool):
        """
        Docstring for status_user

        :param self: Description
        :param status_user_value: Description
        :type status_user_value: bool
        """
        try:
            if not status_user_value:
                raise ValueError("Campo vazio")
            else:
                self.phone = status_user_value
        except TypeError as e:
            raise ValueError("Tipo inválido para status") from e
        except Exception as e:
            raise ValueError("Error no campo status") from e

    # --- Getter and Setter user_id --- #

    @property
    def user_id(self):
        """
        Docstring for user_id

        :param self: Description
        """
        return self.phone

    @user_id.setter
    def user_id(self):
        """
        Docstring for user_id

        :param self: Description
        """
        try:
            self.user_id = uuid.uuid4()
        except TypeError as e:
            raise ValueError("Tipo inválido para status") from e
        except Exception as e:
            raise ValueError("Error no campo status") from e

    # --- Getter and Setter data_created --- #
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

    # --- Getter and Setter user_type --- #
    @property
    def user_type(self):
        """
        Docstring for user_type

        :param self: Description
        """
        return self.user_type

    @user_type.setter
    def user_type(self, user_type_value: UserType):
        try:
            if not user_type_value:
                self.user_type = UserType.NORMAL
            else:
                self.data_update = user_type_value
        except TypeError as e:
            raise ValueError("Tipo inválido para atualização da data") from e
        except Exception as e:
            raise ValueError("Error para atualização da data") from e
