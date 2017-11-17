from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# добавить сюда отдельно функцию на удаление пользователей


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

    def __init__(self):
        self.name = input('Как тебя зовут?: ')
        self.faculty = input('С какого ты факультета?: ')
        self.interactions = 0
        self.karma = 0
        self.tutor = 0
        self.student = 0

        ans_for_student = input('Ты хочешь найти репетитора?(да/нет): ')
        ans_for_tutor = input('Ты хочешь кому-то помочь?(да/нет): ')

        if ans_for_tutor == 'да':
            self.tutor = 1

        if ans_for_student == 'да':
            self.student = 1

    def add_student(self, current_session, student_base):
        print('Добавьте новый предмет: ')

        new_subject = int(input('Ведите номер предмета: '))  # тут надоотправлять пользователю
        # список доступных предметов
        task_name = int(input('выберете номер варианта: '))  # тоже и с режимом и с названием задания
        task_mode = int(input('выберете номер режима: '))

        new_student = student_base(subject=new_subject, user=self, task=task_name, mode=task_mode)

        current_session.add(new_student)
        current_session.commit()

    def add_tutor(self, current_session, tutor_base):
        print('Добавьте новый предмет: ')

        new_subject = int(input('Ведите номер предмета: '))  # тут надоотправлять пользователю
        # список доступных предметов
        task_name = int(input('выберете номер варианта: '))  # тоже и с режимом и с названием задания
        task_mode = int(input('выберете номер режима: '))
        task_price = input('что вы хотите за выполнение?: ')

        new_tutor = tutor_base(subject=new_subject,
                               user=self,
                               task=task_name,
                               mode=task_mode,
                               price=task_price,
                               knowledge=0,
                               interactions=0)
        # добавить в инит знания = 0 и взаимодействия = 0

        current_session.add(new_tutor)
        current_session.commit()

    def change_karma(self, rating):
        self.interactions += 1
        self.karma = (self.karma + rating) / self.interactions

    def change_student(self):  # использовать в паре с add_student
        self.student = 1

    def change_tutor(self):  # использовать в паре с add_tutor
        self.tutor = 1


engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.create_all(engine)