from pydantic import Field, EmailStr, field_validator
from pydantic.functional_validators import AfterValidator
from typing import Annotated, Optional, Sequence, List
from datetime import date
import re
from .enums import Gender

__DEFAULT_MAX_LENGTH:int = 10000

def validate_password(value:str) -> str:
    """Custom password validation to ensure it meets security criteria."""
    if not re.search(r"[a-z]", value):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", value):
        raise ValueError("Password must contain at least one number.")
    if not re.search(r"[@&£$%^&()\-]", value):
        raise ValueError("Password must contain at least one special character (@&£$%^&()-).")
    return value

# AfterValidator(validate_password)
PASSWORD_FIELD = Annotated[
    str, 
    Field(min_length=8, max_length=50, examples=['Password$123'], serialization_alias='password_hash'),
    AfterValidator(validate_password)
]
EMAIL_FIELD = Annotated[EmailStr, Field(max_length=50)]

ALPHA_FIELD = Annotated[str, Field(max_length=__DEFAULT_MAX_LENGTH, pattern='^[a-zA-Z]+$')]

NAME_FIELD = Annotated[ALPHA_FIELD, Field(max_length=50)]
FIRST_NAME_FIELD = Annotated[ALPHA_FIELD, Field(examples=['John'])]
LAST_NAME_FIELD = Annotated[ALPHA_FIELD, Field(examples=['Doe'])]

DOB_FIELD = Optional[date]
GENDER_FIELD = Annotated[Gender, Field(default=Gender.OTHER)]
PHONE_FIELD = Annotated[str, Field(max_length=17)]
ROLES_FIELD = Annotated[Sequence, Field(default={'user'})]
DATETIME_STR_FIELD = Annotated[
    str, 
    Field(
        pattern='/^((?:(\\d{4}-\\d{2}-\\d{2})T(\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?))(Z|[\\+-]\\d{2}:\\d{2})?)$/gm',
        examples=[
            '2018-01-10T06:14:00Z',
            '2016-01-19T15:21:32.59+02:00',
        ]
    )
]

ROLE_NAMES_FIELD = Annotated[List[str], Field(examples=[['role1', 'role2']])]

DESCRIPTION_FIELD = Annotated[str, Field(default='No Description.', max_length=10000)]