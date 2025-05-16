from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING, List
from app.database import base_models
from app.domain.user_roles.entities import user_roles
from app.domain.users import entities as user_entities


class Role(base_models.BaseWithID):
    __tablename__ = 'roles'
    
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    datetime_created: Mapped[datetime] = mapped_column(default=datetime.now())
    users: Mapped[List['user_entities.User']] = relationship('User', secondary=user_roles, back_populates='roles')