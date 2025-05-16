from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.domain.common import schema_fields

class Token(BaseModel):
    access_token:str
    token_type:Optional[str]
    
class Payload(BaseModel):
    sub: str
    exp: datetime|schema_fields.DATETIME_STR_FIELD
    
class Reauth(BaseModel):
    password: str