from .core import db as db_conn
from app.core import log

logger = log.get_logger(__name__, level='DEBUG')

def run():
    logger.info('Running database setup..')

    db_conn.create_tables()

    # Database operations which require a database session
    with db_conn.session_scope() as session:
        pass

