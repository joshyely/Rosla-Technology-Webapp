from fastapi import status
from app.core.exceptions import ApiException

class EmailExists(ApiException):
    def __init__(self, detail:str='User with that email already exists'):
        super().__init__(
            status_code=status.HTTP_226_IM_USED,
            detail=detail,
            error_code='EMAIL_EXISTS'
        )

class UserNotExist(ApiException):
    def __init__(self, detail:str='User does not exist'):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=detail,
            error_code='USER_NOT_EXIST'
        )


