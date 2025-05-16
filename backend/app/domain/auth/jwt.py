import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone

from . import schemas, exceptions



oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'/auth/login')

def create_token(payload: schemas.Payload, jwt_key: str, jwt_algorithm: str, token_type: str='bearer') -> schemas.Token:
    """_Creates a JWT token on a verfified login._

    Args:
        payload (Payload): Token payload containing data to be encoded.

    Returns:
        Token: Token Schema
    """
    payload_json = vars(payload)
    encoded = jwt.encode(payload_json, jwt_key, jwt_algorithm)
    return schemas.Token(
        access_token=encoded,
        token_type=token_type
    )


def create_expiry_date(minutes:int) -> datetime:
    """
    Args:
        minutes (int): How many minutes until the token expires

    Returns:
        datetime: Token expiry date
    """
    return datetime.now(timezone.utc) + timedelta(minutes=minutes)

def create_payload(user: dict, expiry_date: datetime) -> schemas.Payload:
    return schemas.Payload(
        sub=str(user['id']),
        exp=expiry_date
    )

    
def verify_token(token:str, jwt_key: str, jwt_algorithm: str) -> schemas.Payload:
    """_Uses JWT to verfify the token's signature using the a saved jwt key_
    
    Args:
        token (Annotated[str, Depends]): _Token string from request header_
    
    Raises:
        HTTPException: Raises 401 UNAUTHORIZED if the token's signature is invalid.

    Returns:
        schemas.Payload: _Payload containing token data_
    """
    try:
        payload_dict = jwt.decode(token, key=jwt_key, algorithms=[jwt_algorithm])
    except jwt.InvalidTokenError:
        raise exceptions.InvalidToken
    return schemas.Payload(**payload_dict)

