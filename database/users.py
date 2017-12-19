from . import User


def create_user(current_session, bot, username):  # пользователь может менять инфу добавишь
    bot.send_message(username, 'Как тебя зовут?')
    s_name = ''

    @bot.message_handler(func=lambda x: True)
    def set_name(message):
        nonlocal s_name
        s_name = message.text

    bot.send_message(username, 'С какого ты факультета?')
    s_faculty = input('С какого ты факультета?: ')
    s_tutor = 0
    s_student = 0

    bot.send_message(username, 'Ты хочешь найти репетитора? (Да/Нет)')
    ans_for_student = input('Ты хочешь найти репетитора?(да/нет): ')
    bot.send_message(username, 'Ты хочешь кому-то помогать? (Да/Нет)')  # сделаю тут клавиатуру да нет из двух столбцов
    ans_for_tutor = input('Ты хочешь кому-то помочь?(да/нет): ')

    if ans_for_tutor.lower() == 'да':  # не уверена что нам это надо, так как нигде не используется # надо заюзать lower
        s_tutor = 1

    if ans_for_student.lower() == 'да':  # аналогично
        s_student = 1

    s_user = User(name=s_name,
                  faculty=s_faculty,
                  karma=0,
                  student=s_student,
                  tutor=s_tutor,
                  interactions=0,
                  connection=username)  # id

    current_session.add(s_user)
    current_session.commit()


def change_karma(current_session, user_tab,user_id,rating):  # сразу вносит все изменения в таблицу
    s_user = current_session.query(user_tab).filter(user_tab.id == user_id).first()
    s_user.interactions += 1
    s_user.karma = (s_user.karma + rating) / s_user.interactions

    current_session.add(s_user)
    current_session.commit()

# теперь у нас id
# def change_connection(current_session, user_tab,user_id,new_username):
#     s_user = current_session.query(user_tab).filter(user_tab.id == user_id).first()
#     s_user.connection = new_username
#
#     current_session.add(s_user)
#     current_session.commit()
