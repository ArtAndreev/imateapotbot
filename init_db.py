from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
import logging.config

# переместил запуск из бывшего db_main.py (__init__.py в либе)


def init_db():
    logging.config.fileConfig('logging.conf')
    db_logger = logging.getLogger('sqlalchemy.engine')  # дополнительное логирование в человекочитаемом виде

    engine = create_engine('sqlite:///database/tea_pot.db')
    # Base = declarative_base()
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    return DBSession()
