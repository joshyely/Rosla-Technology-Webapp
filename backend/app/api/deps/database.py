from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.core import db

DB_SESSION_DEP = Annotated[Session, Depends(db.create_session)]