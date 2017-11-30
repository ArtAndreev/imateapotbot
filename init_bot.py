from telebot import TeleBot
from config import TOKEN

import logging.config
from database import request, users


def init_bot(session):
    bot = TeleBot(TOKEN)
    logging.config.fileConfig('logging.conf')
    bot_logger = logging.getLogger('TeleBot')

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        user_id = request.in_db_id(session, message.chat.id)
        if user_id:
            # user = request.get_user(session, message.chat.id)
            bot.send_message(message.chat.id,
                             'Привет, %s!\n'
                             'Что хочешь сделать?\n'
                             % message.chat.first_name)  # TODO: текущих заданий tasks от user
        else:
            bot.send_message(message.chat.id,
                             'Привет, %s!\nЯ вижу, ты тут в первый раз.\n'
                             'Пройди, пожалуйста, небольшую регистрацию.'
                             % message.chat.first_name)
            users.create_user(session, bot, message.chat.id)  # TODO: доделать регистрацию

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id,
                         'Бот для Telegram, предоставляющий возможность найти' 
                         'человека, который сможет помочь с проблемами в '
                         'обучении или с понимаем того или иного предмета.\n'
                         'Вот что я умею:\n'
                         '/help - получение информации о боте и командах;\n')

    #
    # TODO: клавиатура со всеми командами вместо печатания ручками
    #

    @bot.message_handler(commands=['info'])
    def send_help(message):
        bot.send_message(message.chat.id,
                         'Информация о тебе:\n'
                         'Шарю в: физика;'
                         'Помог: 0;'
                         'Карма: 0.')  # больше инфы

    @bot.message_handler(commands=['find_help'])  # найти помощь
    def send_help(message):
        bot.send_message(message.chat.id,
                         'Уже ищу тебе помощника... Предмет...')

    @bot.message_handler(commands=['do_help'])  #  помощь
    def send_help(message):
        bot.send_message(message.chat.id,
                         'ищу нуждающегося')

    # # testing messages
    # @bot.message_handler(func=lambda message: True)
    # def echo_all(message):
    #     bot.reply_to(message, message.text)

    bot.polling(none_stop=True)
