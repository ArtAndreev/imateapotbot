from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

# тут надо плдумать над тем, как будем заполнять списки в этих таблицах
# и в каком виде выводить инфу об пользователях


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Mode(Base):
    __tablename__ = 'mods'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class User(Base):  # разобраться с connection, photo
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    faculty = Column(String(250), nullable=False)
    karma = Column(Integer)
    student = Column(Integer)
    tutor = Column(Integer)
    interactions = Column(Integer)
    connection = Column(String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Tutor(Base):
    __tablename__ = 'tutors'

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    task_id = Column(Integer, ForeignKey('tasks.id'))
    mode_id = Column(Integer, ForeignKey('mods.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    knowledge = Column(Integer)
    interactions = Column(Integer)
    price = Column(String(250))

    users = relationship(User)
    subjects = relationship(Subject)
    tasks = relationship(Task)
    mods = relationship(Mode)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    task_id = Column(Integer, ForeignKey('tasks.id'))
    mode_id = Column(Integer, ForeignKey('mods.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    users = relationship(User)
    subjects = relationship(Subject)
    tasks = relationship(Task)
    mods = relationship(Mode)


class Deal(Base):
    __tablename__ = 'conections'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey('tutors.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(20))
    student_karma = Column(Integer)
    tutor_karma = Column(Integer)
    knowledge_rating = Column(Integer)

    users = relationship(User)
    tutors = relationship(Tutor)

    def __init__(self):
        status = 'open'


engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.create_all(engine)
