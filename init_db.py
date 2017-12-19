from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
import logging.config


def init_db():
    logging.config.fileConfig('logging.conf')
    db_logger = logging.getLogger('sqlalchemy.engine')  # дополнительное логирование в человекочитаемом виде

    engine = create_engine('sqlite:///database/tea_pot.db',
                           connect_args={'check_same_thread': False})  # FIXME
    # Base = declarative_base()
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    return DBSession()
