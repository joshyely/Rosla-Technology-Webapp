from sqlalchemy import Table, Column, ForeignKey
from app.database import base_models

user_roles = Table(
    'user_roles',
    base_models.Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True),
)
