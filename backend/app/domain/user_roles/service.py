from sqlalchemy.orm import Session

from app.domain.users import ( 
    service as user_service,
    entities as user_entities,
)
from app.domain.roles import (
    service as roles_service,
    entities as role_entities,
)

from . import entities, schemas

def set_roles(db: Session, schema: schemas.RolesAssign) -> user_entities.User:
    user = user_service.get_user(db, id=schema.user_id)
    roles = roles_service.get_many_roles(
        db, 
        role_entities.Role.id.in_(schema.roles_id)
    )
    user.roles = roles
    return user_service.user_crud.update(db, user)