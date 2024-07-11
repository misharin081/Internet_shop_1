from django.http import JsonResponse
from rest_framework import status


class ApiResponse(JsonResponse):
    def __init__(self,
                 data: list,
                 status_code: status, **kwargs):
        content = {
            "status": status_code,
            "data": data,
        }
        super().__init__(content, status=status_code, **kwargs)


class SuccessGetResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_200_OK,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)


class BadGetResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_404_NOT_FOUND,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)

class SuccessPostResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_200_OK,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)

class BadPostResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_400_BAD_REQUEST,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)

class SuccessPutResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_201_CREATED,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)

class BadPutResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_400_BAD_REQUEST,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)


class SuccessPatchResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_202_ACCEPTED,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)


class BadPatchResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_400_BAD_REQUEST,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)

class SuccessDeleteResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_200_OK,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)


class BadDeleteResponse(ApiResponse):
    def __init__(self,
                 data: list = None,
                 status_code: status = status.HTTP_400_BAD_REQUEST,
                 **kwargs):
        super().__init__(data, status_code, **kwargs)




