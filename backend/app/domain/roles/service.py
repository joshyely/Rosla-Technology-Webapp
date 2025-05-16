from sqlalchemy.orm import Session
from typing import List
from app.database.crud import BaseRepository
from . import entities, schemas, exceptions

roles_crud = BaseRepository(entity_cls=entities.Role)



def get_many_roles(db: Session, *filters, skip: int = 0, limit: int = 100, **kw_filters) -> List[entities.Role]:
    return roles_crud.get_many(db, *filters, skip=skip, limit=limit, **kw_filters)

def get_role(db: Session, *filters, **kw_filters) -> entities.Role:
    role = roles_crud.get_one(db, *filters, **kw_filters)
    if not role:
        raise exceptions.RoleNotExist
    return role

def create_role(db: Session, schema: schemas.RoleCreate) -> entities.Role:
    return roles_crud.create(db, schema=schema)

def update_role(db: Session, role_id: int, schema: schemas.RoleUpdate) -> entities.Role:
    role = get_role(db, id=role_id)
    return roles_crud.update_with_schema(db, role, schema)

def delete_role(db: Session, role_id: int) -> entities.Role:
    role = get_role(db, id=role_id)
    return roles_crud.delete(db, role)