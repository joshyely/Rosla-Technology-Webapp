from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from . import passwords, jwt, schemas, exceptions
from app.domain.users import entities as user_entities
from app.core.config import settings

   
def authenticate_login(db: Session, email: str, password: str) -> schemas.Token:
    """_Service for authenticating a user from their email and password._

    Args:
        db (Session): _A Database Session_
        email (str): _Provided email_
        password (str): _Provided password_

    Raises:
        exceptions.InvalidCredentials: _Raised if the provided email doesn't exist or the password is incorrect_
        
    Returns:
        schemas.Token: _JWT Token_
    """
    user = db.query(user_entities.User).filter_by(email=email).first()
    if not user:
        raise exceptions.InvalidCredentials
    elif not passwords.verify_password(password, user.password_hash):
        raise exceptions.InvalidCredentials
    
    expiry_date = jwt.create_expiry_date(minutes=settings.JWT_EXPIRY_MINUTES)
    new_payload = jwt.create_payload(user, expiry_date)
    return jwt.create_token(
        new_payload,
        jwt_key=settings.JWT_KEY, 
        jwt_algorithm=settings.JWT_ALGORITHM
    )

def authenticate_from_id(db: Session, user_id: str, password: str) -> user_entities.User:
    user = db.query(user_entities.User).filter_by(id=user_id).first()
    if not user:
        raise exceptions.InvalidToken
    elif not passwords.verify_password(password, user.password_hash):
        raise exceptions.InvalidCredentials
    return user

