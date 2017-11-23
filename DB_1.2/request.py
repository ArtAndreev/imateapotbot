
def get_request(current_session, sub_tab, task_tab, mode_tab):
    new_subject_ans = int(input('Ведите номер предмета: '))  # тут надо отправлять пользователю
    # список доступных предметов
    task_name_ans = int(input('выберете номер варианта: '))  # тоже и с режимом и с названием задания
    task_mode_ans = int(input('выберете номер режима: '))

    name_subject = current_session.query(sub_tab).filter(sub_tab.id == new_subject_ans).one()
    task_name = current_session.query(task_tab).filter(task_tab.id == task_name_ans).one()
    task_mode = current_session.query(mode_tab).filter(mode_tab.id == task_mode_ans).one()
    return name_subject, task_name, task_mode


def add_tutor(current_session, user, tutor_base, sub_tab, task_tab, mode_tab):
    print('Добавьте новый предмет: ')   # проработать тут связь с пользователем
    task_price = input('что вы хотите за выполнение?: ')   # проработать тут связь с пользователем

    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)

    new_tutor = tutor_base(subjects=new_subject,
                           users=user,
                           tasks=task_name,
                           mods=task_mode,
                           price=task_price,
                           knowledge=0,
                           interactions=0)

    return new_tutor


def add_student(current_session, user, student_base, sub_tab, task_tab, mode_tab):
    print('Добавьте новый предмет: ')
    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)

    new_student = student_base(subjects=new_subject, users=user, tasks=task_name, mods=task_mode)

    return new_student


def search_student(current_session, sub_tab, task_tab, mode_tab, student_base, user_base):

    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)

    students = current_session.query(student_base).\
        filter(student_base.subjects == new_subject,
               student_base.tasks == task_name,
               student_base.mods == task_mode).all()

    for row in students:
        select_user = current_session.query(user_base).filter(user_base.id == row.user_id).first()
        # получили набор подходящих юзеров
        print(select_user)
        # далее его надо перекинуть репетитору


def search_tutor(current_session, sub_tab, task_tab, mode_tab, tutor_base, user_base):

    new_subject, task_name, task_mode = get_request(current_session, sub_tab, task_tab, mode_tab)

    knowledge_rating = int(input('какой процент знаний вас устроит?(от 0 до 100): '))  # проработать тут связь с пользователем
    tutors = current_session.query(tutor_base).\
        filter(tutor_base.subjects == new_subject,
               tutor_base.mods == task_mode,
               tutor_base.tasks == task_name,
               tutor_base.knowledge >= knowledge_rating).all()

    for row in tutors:
        select_user = current_session.query(user_base).filter(user_base.id == row.user_id).first()
        print(select_user)
        # получили набор подходящих юзеров
        # далее его надо перекинуть студенту,плюс надо докинуть инфу о цене и знаниях
        # это лежит в row


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