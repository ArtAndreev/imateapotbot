from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# тут надо плдумать над тем, как будем заполнять списки в этих таблицах


class Subject(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Task(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Mode(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.create_all(engine)
