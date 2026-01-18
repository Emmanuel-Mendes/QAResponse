class Response:
    def __init__(self, status: bool = False, data: None = "", error: str = ""):
        self.status = status
        self.data = data
        self.error = error

    @classmethod
    def success(self, data: any = ""):
        return Response(status=True, data=data)

    @classmethod
    def error(self, error: any = "", data: any = ""):
        return Response(status=False, error=error, data=data)
