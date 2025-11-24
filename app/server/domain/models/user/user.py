from datetime import datetime
import uuid

from utils.user_utils import validate_email
from enum.enum_user import User_type

class User:
    def __init__(self,
                 _id,
                 _name: str,
                 _password: str,
                 _email: str,
                 _phone: str,
                 _status_user: bool = False,
                 _user_id: str = uuid.uuid4(),
                 _data_created: datetime = datetime.now(),
                 _data_update: datetime = datetime.now(),
                 _user_type: User_type = User_type.normal.value,                 
                 ):
        
        self.id = id
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
        return self.name
    
    @name.setter
    def name(self, name_value:str):
        try:
            if not name_value or name_value < 3:
                raise ValueError("Tamanho inválido para o campo nome")
            else:
                self.name = name_value
        except TypeError:
            raise ValueError("Tipo inválido para o campo password")
        except Exception:
            raise ValueError("Error no campo password")     
            
            
    # --- Getter and Setter password --- #  
    @property    
    def password(self):
        return self.password
    
    @password.setter
    def password(self, password_value:str):
        try:
            if not password_value or password_value < 3:
                raise ValueError("Tamanho inválido para o campo password")
            else:
                self.password = password_value                   
        except TypeError:
            raise ValueError("Tipo inválido para o campo password")
        except Exception:
            raise ValueError("Error no campo password")          
        
    # --- Getter and Setter email --- #  
    @property    
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email_value:str):
        try:
            if not email_value or email_value < 3:
                raise ValueError("Tamanho inválido para o campo email")
            if not validate_email(email=email_value):
                raise ValueError("Email inválido")                
            else:
                self.email = email_value                   
        except TypeError:
            raise ValueError("Tipo inválido para o campo email")
        except Exception:
            raise ValueError("Error no campo email")         
        
    # --- Getter and Setter status_user --- #  
    @property    
    def status_user(self):
        return self.phone
    
    @status_user.setter
    def status_user(self, status_user_value:bool):
        try:
            if not status_user_value:
                raise ValueError("Campo vazio")
            else:
                self.phone = status_user_value                   
        except TypeError:
            raise ValueError("Tipo inválido para status")
        except Exception:
            raise ValueError("Error no campo status")   
        
    # --- Getter and Setter data_created --- #  
    @property    
    def data_created(self):
        return self.data_created
    
    @data_created.setter
    def data_created(self, data_created_value:str):
        try:
            if not data_created_value:
                raise ValueError("Campo vazio")
            else:
                self.data_created = data_created_value                  
        except TypeError:
            raise ValueError("Tipo inválido para usuário")
        except Exception:
            raise ValueError("Error no campo usuário")  
        
                     
    # --- Getter and Setter data_update --- #  
    @property    
    def data_update(self):
        return self.data_update
    
    @data_update.setter
    def data_update(self, data_update_value:str):
        try:
            if not data_update_value:
                raise ValueError("Campo vazio")
            else:
                self.data_update = data_update_value                   
        except TypeError:
            raise ValueError("Tipo inválido para atualização da data")
        except Exception:
            raise ValueError("Error para atualização da data")  
        
    # --- Getter and Setter user_type --- #  
    @property    
    def user_type(self):
        return self.user_type
    
    @user_type.setter
    def user_type(self, user_type_value:User_type):
        try:
            if not user_type_value:
                raise ValueError("Campo vazio")
            else:
                self.data_update = user_type_value                   
        except TypeError:
            raise ValueError("Tipo inválido para atualização da data")
        except Exception:
            raise ValueError("Error para atualização da data")  
             
