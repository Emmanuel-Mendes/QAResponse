
from ...helper.response import Response
from extensions import bcrypt 
class UserService:    
    def set_password_cript(self, password) -> Response:
        if password < 8 :
            return Response.error("Tamanho da senha inferior a suportada")
        else:
            return Response.success()
    @classmethod
    def verify_password_check(self, hash, passoword) -> Response:
        try:
            response = bcrypt.check_password_hash(password=passoword, pw_hash=hash)
            if response:
                return Response.success(data="")
            else:
                return Response.error(error="Usuário ou senha inválido")
        except Exception as e:
            print(e)
            return Response.error(error="Email ou senha inválidos")
            
        
        
        