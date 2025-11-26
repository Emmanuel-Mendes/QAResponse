from .user import User
from ....helper.response import Response
from ....database.user_data_source import db as database

class UserRepository(database.Model):
    
    __tablename__ = "users"   
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=True)
    password = database.Column(database.String(200), nullable=True)
    email = database.Column(database.String(75), nullable=True)
    phone = database.Column(database.String(75), nullable=True)
    status_user = database.Column(database.Boolean, nullable=True)
    user_id = database.Column(database.String(100), nullable=True)
    data_created = database.Column(database.String(100), nullable=True)
    data_update = database.Column(database.String(100), nullable=True)
    user_type = database.Column(database.String(100), nullable=True)
             
    @classmethod
    def addUser(user : User) -> Response:
        return Response.error
    
    @classmethod
    def veriftyUserByEmail(self, user: User.email) -> Response:
        print(user)
        return False
    
    @classmethod
    def createUser(self, user: User) -> Response:        
        return False
    
    @classmethod
    def deleteUser(self, user: User) -> Response:        
        return False

