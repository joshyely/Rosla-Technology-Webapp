from fastapi import APIRouter
from app.api.routes import (
    roles,
)


api_routes = APIRouter()

api_routes.include_router(roles.router)