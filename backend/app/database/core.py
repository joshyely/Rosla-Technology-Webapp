from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator, Any
from contextlib import contextmanager

from app.core.config import settings
from app.core import log
from .base_models import Base, BaseWithID

logger = log.get_logger(__name__, level='DEBUG')

class Database:
    def __init__(self, db_url:str, check_same_thread:bool=False):
        logger.info('Initialising database connection..')
        self.engine = create_engine(url=db_url, connect_args={"check_same_thread": check_same_thread})
        self.Session = sessionmaker(bind=self.engine)
    
    def create_tables(self):
        logger.info('Creating non-existant tables..')
        Base.metadata.create_all(self.engine)
    
    def create_session(self) -> Generator[Session, None, None]:
        """Creates a new database session for FastAPI's dependancy injection.

        Yields:
            Generator[Session, None, None]
        """
        logger.debug('Creating session..')
        session = self.Session()
        try:
            yield session
        finally:
            session.close()
            logger.debug('Session closed.')
            
   
    @contextmanager
    def session_scope(self) -> Generator[Session, Any, None]:
        """Creates a new database session with a context manager for manual use.
        _(Will mainly be used for testing purposes)_
        
        Yields:
            Generator[Session, Any, None]: _description_
        """
        logger.debug('Creating session scope..')
        gen = self.create_session()
        session = next(gen)
        try:
            yield session
        finally:
            gen.close()
            logger.debug('Generator closed.')
    
    
db = Database(db_url=settings.DB_URL)