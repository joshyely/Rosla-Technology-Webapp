from __future__ import annotations
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List
from datetime import date
from app.database import base_models, info
from app.domain.common.enums import Gender
from app.domain.user_roles.entities import user_roles
# # Avoids circular imports by only importing if a type checking tool is used
# if TYPE_CHECKING:
from app.domain.roles import entities as role_entities


class User(base_models.BaseWithID):
    __tablename__ = 'users'
    
    
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    dob: Mapped[date] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(
        Enum(Gender, native_enum=False, values_callable=lambda e: [x.value for x in e]),
        default=Gender.OTHER
    )
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[date] = mapped_column(default=date.today())
    is_active: Mapped[bool] = mapped_column(default=False)
    
    roles: Mapped[List['role_entities.Role']] = relationship('Role', secondary=user_roles, back_populates='users')



    
