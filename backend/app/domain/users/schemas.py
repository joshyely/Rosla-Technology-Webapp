from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.domain.common.schema_fields import (
    ALPHA_FIELD,
    FIRST_NAME_FIELD,
    LAST_NAME_FIELD,
    DOB_FIELD,
    GENDER_FIELD,
    EMAIL_FIELD,
    PASSWORD_FIELD,
    PHONE_FIELD,
)
from app.domain.auth import schemas as auth_schemas


class UserOut(BaseModel):
    first_name: FIRST_NAME_FIELD
    last_name: LAST_NAME_FIELD
    dob: DOB_FIELD
    gender: GENDER_FIELD
    email: EMAIL_FIELD
    phone:Optional[str]

class UserCreate(BaseModel):
    first_name: FIRST_NAME_FIELD
    last_name: LAST_NAME_FIELD
    dob: DOB_FIELD
    gender: GENDER_FIELD
    email: EMAIL_FIELD
    phone:Optional[PHONE_FIELD]
    password: PASSWORD_FIELD
    
    model_config = ConfigDict(serialize_by_alias=True)
        
class UserConfirmRegister(BaseModel):
    message: str = 'User Registered'
    user: UserOut


class UserUpdatePassword(BaseModel):
    new_password: PASSWORD_FIELD
    
class UserUpdateEmail(BaseModel):
    new_email: EMAIL_FIELD
    
class UserUpdatePhone(BaseModel):
    new_phone: PHONE_FIELD

class UserDeleteAccount(BaseModel):
    pass

class UserUpdatePersonal(BaseModel):
    first_name: FIRST_NAME_FIELD
    last_name: LAST_NAME_FIELD
    new_dob: DOB_FIELD
    new_gender: GENDER_FIELD
    
    