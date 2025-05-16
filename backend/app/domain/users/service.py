from sqlalchemy.orm import Session, Query
from typing import List, Literal
from datetime import date
from . import entities, schemas, exceptions
from app.domain.auth import passwords
from app.database.crud import BaseRepository

user_crud = BaseRepository(entity_cls=entities.User)

def query_single_user(db: Session, *filters, **kw_filters) -> Query[entities.User]:
    user = user_crud.__query(db, *filters, **kw_filters)
    if not user.first():
        raise exceptions.UserNotExist
    return user
    
def email_exists(db: Session, email:str) -> bool:
    return user_crud.get_one(db, email=email) != None

def get_user(db: Session, *filters, **kw_filters) -> entities.User:
    user = user_crud.get_one(db, *filters, **kw_filters)
    if not user:
        raise exceptions.UserNotExist
    return user

def get_many_users(db: Session, *filters, skip: int = 0, limit: int = 100, **kw_filters) -> List[entities.User]:
    return user_crud.__query(db, *filters, skip=skip, limit=limit, **kw_filters).join(entities.User.roles).all()

def create_user(
    db: Session, 
    schema: schemas.UserCreate,
) -> entities.User:
    if email_exists(db, email=schema.email):
        raise exceptions.EmailExists
    
    schema.password = passwords.create_password_hash(schema.password)
    return user_crud.create(db, schema)

def delete_user(db: Session, user_id: int) -> int:
    user = get_user(db, id=user_id)
    return user_crud.delete(db, user)


def update_email(db: Session, user_id: int, schema: schemas.UserUpdateEmail) -> entities.User:
    user = get_user(db, id=user_id)
    if email_exists(db, schema.new_email):
        raise exceptions.EmailExists
    
    return user_crud.update_with_schema(db, user, schema)

def update_phone(db: Session, user_id: int, schema: schemas.UserUpdatePhone) -> entities.User:
    user = get_user(db, id=user_id)
    return user_crud.update_with_schema(db, user, schema)

def update_password(db: Session, user_id: int, schema: schemas.UserUpdatePassword) -> entities.User:
    user = get_user(db, id=user_id)
    user.password_hash = passwords.create_password_hash(schema.new_password)
    return user_crud.update(db, user)

def update_personal(
    db: Session, 
    user_id: int, 
    schema: schemas.UserUpdatePersonal
) -> entities.User:
    user = get_user(db, id=user_id)
    return user_crud.update_with_schema(db, user, schema)