from init_bot import init_bot
from init_db import init_db

# import db (check working db???) and add db initializing

if __name__ == '__main__':
    try:
        session = init_db()
        init_bot(session)
    except Exception:
        # TODO: закрыть базу данных, логирование уже есть
        pass
