
class Response :
    
    def __init__ (self, status, data, error):
        self.status: bool = status
        self.data = data
        self.error = error
    
    @classmethod
    def success(self, data):
        return Response(status= True, data=data)
    
    @classmethod
    def error(self, error):
        return Response(status= False, error=error)
        