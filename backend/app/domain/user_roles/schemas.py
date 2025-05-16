from pydantic import BaseModel
from typing import List

class RolesAssign(BaseModel):
    user_id: int
    roles_id: List[int]

class BulkRolesAssign(BaseModel):
    user_ids: List[int]
    role_ids: List[int]