from pydantic import BaseModel
from datetime import datetime


class BaseRole(BaseModel):
    name: str
    description: str

class RoleOut(BaseRole):
    id: int
    datetime_created: datetime

class RoleCreate(BaseRole):
    pass

class RoleDelete(BaseModel):
    pass

class RoleUpdate(BaseRole):
    pass