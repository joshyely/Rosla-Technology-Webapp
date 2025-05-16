from fastapi import status
from app.core.exceptions import ApiException

class InvalidToken(ApiException):
    def __init__(self, detail:str = 'Invalid or expired authentication token'):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=detail,
            error_code='INVALID_TOKEN'
        )
        
class InvalidCredentials(ApiException):
    def __init__(self, detail:str = 'Invalid Credentials'):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=detail,
            error_code='INVALID_CREDENTIALS'
        )
        
class AccountNotActive(ApiException):
    def __init__(self, detail:str = 'Account is not active'):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            error_code='ACCOUNT_NOT_ACTIVE'
        )
        
class InsufficientPermissions(ApiException):
    def __init__(self, detail:str = 'Account has insufficient permissions'):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            error_code='INSUFFICIENT_PERMISSIONS'
        )