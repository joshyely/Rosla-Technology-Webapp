from fastapi import status
from app.core.exceptions import ApiException

class RoleNotExist(ApiException):
    def __init__(self, role_name:str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Role {role_name} does not exist',
            error_code='ROLE_NOT_EXIST'
        )

class AllRolesExist(ApiException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'All roles already exist!',
            error_code='ALL_ROLES_EXIST'
        )