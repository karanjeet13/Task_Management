from rest_framework.response import Response
from rest_framework import status
import json


class StandardResponse(Response):
    VALID_STATUS = ["success", "error", "created"]
    __response_data = {
        "status": "",
        "code": status.HTTP_200_OK,
        "data": {}
    }
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)
        self.set_data(data=data)

    def is_jsonable(self, data):
        try:
            json.dumps(data)
            return True
        except (TypeError, OverflowError):
            return False

    def set_status(self, status):
        if status not in self.VALID_STATUS:
            raise Exception("Invalid Status")
        self.__response_data["status"] = status
    
    def set_code(self, code):
        self.status_code = code
        self.__response_data["code"] = code
    
    def set_data(self, data):
        if self.is_jsonable(data):
            self.__response_data["data"] = data
            self.data = self.__response_data


class InvalidDataResponse(StandardResponse):
    def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        super(InvalidDataResponse, self).__init__(data, template_name, headers, exception, content_type)
        super(InvalidDataResponse, self).set_status("error")
        super(InvalidDataResponse, self).set_code(status.HTTP_400_BAD_REQUEST)
    

class CreatedResponse(StandardResponse):
    def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        super(CreatedResponse, self).__init__(data, template_name, headers, exception, content_type)
        super(CreatedResponse, self).set_status("created")
        super(CreatedResponse, self).set_code(status.HTTP_201_CREATED)


class SuccessResponse(StandardResponse):
    def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        super(SuccessResponse, self).__init__(data, template_name, headers, exception, content_type)
        super(SuccessResponse, self).set_status("success")
        super(SuccessResponse, self).set_code(status.HTTP_200_OK)


class UnauthorizedAccessResponse(StandardResponse):
     def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        super(UnauthorizedAccessResponse, self).__init__(data, template_name, headers, exception, content_type)
        super(UnauthorizedAccessResponse, self).set_status("error")
        super(UnauthorizedAccessResponse, self).set_code(status.HTTP_403_FORBIDDEN)
