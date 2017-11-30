from . import Base, User, Student, Subject, Tutor, Task,Mode, Deal
# from . import request

#
#   TODO: разнести запросы и добавление в БД
#

def get_request(current_session, sub_tab, task_tab, mode_tab):
    new_subject_ans = int(input('Ведите номер предмета: '))  # тут надо отправлять пользователю
    # список доступных предметов
    task_name_ans = int(input('выберете номер варианта: '))  # тоже и с режимом и с названием задания
    task_mode_ans = int(input('выберете номер режима: '))

    name_subject = current_session.query(sub_tab).filter(sub_tab.id == new_subject_ans).one()
    task_name = current_session.query(task_tab).filter(task_tab.id == task_name_ans).one()
    task_mode = current_session.query(mode_tab).filter(mode_tab.id == task_mode_ans).one()
    return name_subject, task_name, task_mode


# def add_tutor(current_session, user, tutor_base, sub_tab, task_tab, mode_tab):  # добавляет предложение помочь
#     print('Добавьте новый предмет: ')   # проработать тут связь с пользователем
#     task_price = input('что вы хотите за выполнение?: ')   # проработать тут связь с пользователем
#
#     new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)
#
#     new_tutor = tutor_base(subjects=new_subject,
#                            users=user,
#                            tasks=task_name,
#                            mods=task_mode,
#                            price=task_price,
#                            knowledge=0,
#                            interactions=0)
#
#     return new_tutor

#
# def add_student(current_session, user, student_base, sub_tab, task_tab, mode_tab):  # добавляет запрос о помощи
#     print('Добавьте новый предмет: ')
#     new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)
#
#     new_student = student_base(subjects=new_subject, users=user, tasks=task_name, mods=task_mode)
#
#     return new_student


def search_student(current_session, sub_tab, task_tab, mode_tab, student_base, user_base):

    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)
    result = []
    students = current_session.query(student_base).\
        filter(student_base.subjects == new_subject,
               student_base.tasks == task_name,
               student_base.mods == task_mode).all()

    for row in students:
        select_user = current_session.query(user_base).filter(user_base.id == row.user_id).first()
        result.append(select_user)

        return result


def search_tutor(current_session, sub_tab, task_tab, mode_tab, tutor_base, user_base):

    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)
    result = []
    knowledge_rating = int(input('какой процент знаний вас устроит?(от 0 до 100): '))  # проработать тут связь с пользователем
    tutors = current_session.query(tutor_base).\
        filter(tutor_base.subjects == new_subject,
               tutor_base.mods == task_mode,
               tutor_base.tasks == task_name,
               tutor_base.knowledge >= knowledge_rating).all()

    for row in tutors:
        select_user = current_session.query(user_base).filter(user_base.id == row.user_id).first()
        result.append(select_user)

    return result


def change_knowledge(current_session, tutor_tab, request_id,rating):
    s_user = current_session.query(tutor_tab).filter(tutor_tab.id == request_id).first()

    s_user.interactions += 1
    s_user.knowledge = (s_user.knowledge + rating) / s_user.interactions

    current_session.add(s_user)
    current_session.commit()


def change_price(current_session, tutor_tab, tut_id,new_price):  # проработать тут связь с пользователем для получения новой цены
    request = current_session.query(tutor_tab).filter(tutor_tab.id == tut_id).first()
    request.price = new_price

    current_session.add(request)
    current_session.commit()

# requests from init_db.py


def in_db_id(session, telega_id):  # 7
    user = session.query(User).filter(User.connection == telega_id).first()
    if user is None:
        return None
    return user.id


def get_user(session, telega_id):  # 6
    user = session.query(User).filter(User.id == in_db_id(session, telega_id)).first()

    return user  # возвращает объект класса(рассмотреть его оторажения для пользователя


def get_my_requests(session, telega_id):  # 2
    requests = session.query(Tutor).filter(Tutor.user_id == in_db_id(telega_id)).all()

    return requests  # возвращает список из объектов класса


def get_my_all_deals(session, telega_id):  # 3
    deals = session.query(Deal, Tutor, User).all()
    result = []

    for row in deals:
        if row.User.id == in_db_id(session, telega_id):
           result.append(row)

    return result # возвращает список из объектов класса


def get_my_open_deals(session, telega_id):  # 5,4
    deals = session.query(Deal, Tutor, User).all()
    result = []

    for row in deals:
        if row.User.id == in_db_id(telega_id) and row.Deal.status == 'open':
            result.append(row)

    return result  # возвращает список из объектов класса если пустой, то сделок нет


def add_tutor(session, telega_id):
    task_price = input('что вы хотите за выполнение?: ')   # проработать тут связь с пользователем
    user = get_user(session, telega_id)
    new_subject, task_name, task_mode = get_request(session, Subject, Task, Mode)

    new_tutor = Tutor(subjects=new_subject,
                      users=user,
                      tasks=task_name,
                      mods=task_mode,
                      price=task_price,
                      knowledge=0,
                      interactions=0)

    session.add(new_tutor)
    session.commit()


def add_student(session, telega_id):
    user = get_user(telega_id)
    new_subject, task_name, task_mode = get_request(session, Subject, Task, Mode)

    new_student = Student(subjects=new_subject, users=user, tasks=task_name, mods=task_mode)

    session.add(new_student)
    session.commit()


def delete_offer(session, telega_id, task_name, subj_name, mode_name):  # 1
    user = get_user(telega_id)
    task = session.query(Task).filter(Task.name == task_name).first()
    subj = session.query(Subject).filter(Subject.name == subj_name).first()
    mode = session.query(Mode).filter(Mode.name == mode_name).first()

    session.query(Tutor).filter(Tutor.users == user,
                                Tutor.subjects == subj,
                                Tutor.tasks == task,
                                Tutor.mods == mode).delete()

    session.commit()


def delete_request(session, telega_id, task_name, subj_name, mode_name):  # 1
    user = get_user(session, telega_id)
    task = session.query(Task).filter(Task.name == task_name).first()
    subj = session.query(Subject).filter(Subject.name == subj_name).first()
    mode = session.query(Mode).filter(Mode.name == mode_name).first()

    session.query(Student).filter(Student.users == user,
                                  Student.subjects == subj,
                                  Student.tasks == task,
                                  Student.mods == mode).delete()

    session.commit()


def search(session, stud_or_tutor):
    if stud_or_tutor == 1:
        return search_student(session, Subject, Task, Mode, Student, User)
    else:
        return search_tutor(session, Subject, Task, Mode, Tutor, User)