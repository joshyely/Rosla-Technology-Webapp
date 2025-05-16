from fastapi import APIRouter, Depends
from app.domain.roles import schemas, service
from app.api.deps.database import DB_SESSION_DEP

router = APIRouter(
    prefix='/roles',
    tags=['roles'],
)

@router.post('/')
def create_role(db: DB_SESSION_DEP, schema: schemas.RoleCreate):
    return service.create_role(db, schema)
