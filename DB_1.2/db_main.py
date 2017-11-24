from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, User, Student, Subject, Tutor, Task,Mode, Deal
import users
import request

engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def in_db_id(telega_id):  # 7
    user = session.query(User).filter(User.connection == telega_id).first()

    return user.id


def get_user(telega_id):  # 6
    user = session.query(User).filter(User.id == in_db_id(telega_id)).first()

    return user  # возвращает объект класса(рассмотреть его оторажения для пользователя


def get_my_requests(telega_id):  # 2
    requests = session.query(Tutor).filter(Tutor.user_id == in_db_id(telega_id)).all()

    return requests  # возвращает список из объектов класса


def get_my_all_deals(telega_id):  # 3
    deals = session.query(Deal, Tutor, User).all()
    result = []

    for row in deals:
        if row.User.id == in_db_id(telega_id):
           result.append(row)

    return result # возвращает список из объектов класса


def get_my_open_deals(telega_id):  # 5,4
    deals = session.query(Deal, Tutor, User).all()
    result = []

    for row in deals:
        if row.User.id == in_db_id(telega_id) and row.Deal.status == 'open':
            result.append(row)

    return result  # возвращает список из объектов класса если пустой, то сделок нет


def add_tutor(telega_id):
    task_price = input('что вы хотите за выполнение?: ')   # проработать тут связь с пользователем
    user = get_user(telega_id)
    new_subject, task_name, task_mode = request.get_request(session, Subject, Task, Mode)

    new_tutor = Tutor(subjects=new_subject,
                      users=user,
                      tasks=task_name,
                      mods=task_mode,
                      price=task_price,
                      knowledge=0,
                      interactions=0)

    session.add(new_tutor)
    session.commit()


def add_student(telega_id):
    user = get_user(telega_id)
    new_subject, task_name, task_mode = request.get_request(session, Subject, Task, Mode)

    new_student = Student(subjects=new_subject, users=user, tasks=task_name, mods=task_mode)

    session.add(new_student)
    session.commit()


def delete_offer(telega_id, task_name, subj_name, mode_name):  # 1
    user = get_user(telega_id)
    task = session.query(Task).filter(Task.name == task_name).first()
    subj = session.query(Subject).filter(Subject.name == subj_name).first()
    mode = session.query(Mode).filter(Mode.name == mode_name).first()

    session.query(Tutor).filter(Tutor.users == user,
                                Tutor.subjects == subj,
                                Tutor.tasks == task,
                                Tutor.mods == mode).delete()

    session.commit()


def delete_request(telega_id, task_name, subj_name, mode_name):  # 1
    user = get_user(telega_id)
    task = session.query(Task).filter(Task.name == task_name).first()
    subj = session.query(Subject).filter(Subject.name == subj_name).first()
    mode = session.query(Mode).filter(Mode.name == mode_name).first()

    session.query(Student).filter(Student.users == user,
                                  Student.subjects == subj,
                                  Student.tasks == task,
                                  Student.mods == mode).delete()

    session.commit()


def search(stud_or_tutor):
    if stud_or_tutor == 1:
        return request.search_student(session, Subject, Task, Mode, Student, User)
    else:
        return request.search_tutor(session, Subject, Task, Mode, Tutor, User)