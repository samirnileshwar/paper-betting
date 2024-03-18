from rest_framework.exceptions import APIException

class LineChangeException(APIException):
    status_code = 400
    default_detail = 'Line has changed. Try again.'
    default_code = 'line_change'