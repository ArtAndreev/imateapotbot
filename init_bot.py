from telebot import TeleBot
from config import TOKEN

import logging.config
from database import request, users

# нужен тотальный рефакторинг:
# разделение интерфейсов запросов и выдачи сообщений
# нужно передавать в запросе инфу для поиска, а не спрашивать в нем ее

def init_bot(session):
    bot = TeleBot(TOKEN)
    logging.config.fileConfig('logging.conf')
    bot_logger = logging.getLogger('TeleBot')

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        chat_id = message.chat.id
        user_id = request.in_db_id(session, chat_id)
        if user_id:
            bot.send_message(chat_id,
                             'Привет, %s!\n'
                             'Что хочешь сделать?\n' % message.chat.first_name
                             + 'У тебя на данный момент '
                             + str(len(request.get_my_open_deals(session,
                                                                 chat_id)))
                             + ' сделок.')
        else:
            bot.send_message(chat_id,
                             'Привет, %s!\nЯ вижу, ты тут в первый раз.\n'
                             'Если ты не знаешь, чем я занимаюсь, почитай '
                             '/help\n'
                             'Чтобы Пройди, пожалуйста, небольшую регистрацию.'
                             % message.chat.first_name)
            users.create_user(session, bot, chat_id)  # TODO: доделать регистрацию

    @bot.message_handler(commands=['help'])
    def about_help(message):
        # побольше инфы: классовое разделение на репетиторов и студентов итп
        bot.send_message(message.chat.id,
                         'Бот для Telegram, предоставляющий возможность найти' 
                         'человека, который сможет помочь с проблемами в '
                         'обучении или с понимаем того или иного предмета.\n'
                         'Список доступных команд (после регистрации):\n'
                         '/info – информация о тебе;\n'
                         '/find_tutor – найти репетитора;\n'
                         '/find_student – найти студента, которому нужно помочь;\n'
                         '/my_requests – доска твоих криков о помощи;\n'
                         '/add_request – добавить просьбу помочь;\n'
                         '/add_offer – добавить предложение помочь.')

    #
    # TODO: клавиатура со всеми командами вместо печатания ручками
    #

    @bot.message_handler(commands=['info'])
    def get_info(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            bot.send_message(chat_id,
                             'Информация о тебе, мой друг:\n'
                             'Тебя зовут ' + user.name +
                             ';\nТвой факультет ' + user.faculty +
                             ';\nВсего сделок/запросов '
                             + str(user.interactions) +
                             ';\nТвоя карма ' + str(user.karma) + '.')
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')


    @bot.message_handler(commands=['find_tutor'])  # найти помощь
    def find_tutor(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            bot.send_message(chat_id,
                             'Уже ищу тебе помощника...')
            try:
                result = request.search(session, bot, chat_id, 0)
                tutor_list = ''
                for user in result:
                    tutor_list += user  # TODO: info list
                    tutor_list += '\n'
                bot.send_message(chat_id,
                                 'Вот те, кто готов тебе помочь:' + tutor_list)
            except AttributeError:
                bot.send_message(chat_id,
                                 'Ты ввел неверные данные. Попробуй '
                                 '/find_tutor снова.')
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')

    @bot.message_handler(commands=['find_student'])  #  помощь
    def find_student(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            bot.send_message(chat_id,
                             'Ищу нуждающегося...')
            try:
                result = request.search(session, bot, chat_id, 1)
                student_list = ''
                for user in result:
                    student_list += user  # TODO: info list
                    student_list += '\n'
                bot.send_message(chat_id,
                                 'Вот те, кто нуждается в тебе:' + student_list)
            except AttributeError:
                bot.send_message(chat_id,
                                 'Ты ввел неверные данные. Попробуй '
                                 '/find_student снова.')
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')

    @bot.message_handler(commands=['my_requests'])
    def my_requests(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            result = request.get_my_requests(session, chat_id)
            offer_list = ''
            if result:
                for request_ in result:
                    offer_list += request_
                    offer_list += '\n'
                    bot.send_message(chat_id,
                                     'Вот доска твоих запросов:' + offer_list)
            # обработать с случае их отсутствия
            else:
                bot.send_message(chat_id,
                                 'У тебя пока нет запросов. '
                                 'Ты можешь их добавить при помощи '
                                 '/add_request')
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')

    @bot.message_handler(commands=['add_request'])
    def add_request(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            # TODO: REQUEST
            request.add_student(session, bot, chat_id)
            pass
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')

    @bot.message_handler(commands=['add_offer'])
    def add_offer(message):
        chat_id = message.chat.id
        user = request.get_user(session, chat_id)
        if user:
            # TODO: OFFER
            request.add_tutor(session, bot, chat_id)
            pass
        else:
            bot.send_message(chat_id,
                             'Пройди сначала регистрацию! Воспользуйся /start')

    bot.polling(none_stop=True, timeout=10)
