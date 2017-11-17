from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import select
import user
import study

Base = declarative_base()

engine = create_engine('sqlite:///tea_pot.db')
conn = engine.connect()


class Tutor(Base):
    __tablename__ = 'tutors'

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))
    task_id = Column(Integer, ForeignKey('task.id'))
    mode_id = Column(Integer, ForeignKey('mode.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    knowledge = Column(Integer)
    interactions = Column(Integer)
    price = Column(String(250))

    user = relationship(user.User)
    subject = relationship(study.Subject)
    task = relationship(study.Task)
    mode = relationship(study.Mode)

    def search_tutor(self,user_base):
        subject_name = int(input('Ведите номер предмета: '))  # тут надоотправлять пользователю
        # список доступных предметов
        task_name = int(input('выберете номер варианта: '))  # тоже и с режимом и с названием задания
        task_mode = int(input('выберете номер режима: '))
        knowledge_rating = int(input('какой процент знаний вас устроит?(от 0 до 100): '))
        select_tutor = select([self].where(self.subject_id == subject_name &
                                           self.mode_id == task_mode &
                                           self.task_id == task_name &
                                           self.knowledge >= knowledge_rating))

        for row in conn.execute(select_tutor):
            select_user = select([user_base].where(user_base.c.id == row.id))
            result = conn.execute(select_user)  # получили набор подходящих юзеров
            # далее его надо перекинуть студенту,плюс надо докинуть инфу о цене и знаниях
            # это лежит в row


Base.metadata.create_all(engine)