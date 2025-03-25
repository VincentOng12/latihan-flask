from werkzeug.exceptions import HTTPException
import json
from src.helpers.response_helper import format_error_response

class CustomErrorException(HTTPException):
    code = 400  # Default status code

    def __init__(self, description="Custom Bad Request", code=None, data=None):
        self.code = code or self.code  # Gunakan kode yang diberikan atau default (400)
        self.description = description
        self.data = data
        super().__init__(description)

    def get_response(self, environ=None):
        return format_error_response(
            code=self.code,
            message=self.description,
            data=self.data
        )
