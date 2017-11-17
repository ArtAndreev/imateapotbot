from tables import User


def create_user(username):
    s_name = input('Как тебя зовут?: ')
    s_faculty = input('С какого ты факультета?: ')
    s_tutor = 0
    s_student = 0

    ans_for_student = input('Ты хочешь найти репетитора?(да/нет): ')
    ans_for_tutor = input('Ты хочешь кому-то помочь?(да/нет): ')

    if ans_for_tutor == 'да':
        s_tutor = 1

    if ans_for_student == 'да':
        s_student = 1

    s_user = User(name=s_name,
                  faculty=s_faculty,
                  karma=0,
                  student=s_student,
                  tutor=s_tutor,
                  interactions=0,
                  connection=username)
    return s_user


def change_karma(current_session, user_tab,user_id,rating):
    s_user = current_session.query(user_tab).filter(user_tab.id == user_id).first()
    s_user.interactions += 1
    s_user.karma = (s_user.karma + rating) / s_user.interactions
    return s_user  # внести в основной изменение в таблице
