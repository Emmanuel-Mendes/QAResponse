"""
Response class
"""


class Response:
    """
    Docstring for Response
    """

    def __init__(self, status: bool = False, data: None = "", error: str = ""):
        self.status = status
        self.data = data
        self.error_data = error

    @classmethod
    def success(cls, data: any = ""):
        """
        Docstring for success

        :param cls: Description
        :param data: Description
        :type data: any
        """
        return Response(status=True, data=data)

    @classmethod
    def error(cls, error: str = ""):
        """
        Docstring for error

        :param cls: Description
        :param error: Description
        :type error: any
        :param data: Description
        :type data: any
        """
        return Response(status=False, error=error)
