import config

import telebot
import logging
import logging.config

bot = telebot.TeleBot(config.TOKEN)

logging.config.fileConfig('logging.conf')
bot_logger = logging.getLogger('TeleBot')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Привет, %s!\nЧто хочешь сделать?' %message.chat.first_name)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Бот для Telegram, предоставляющий возможность '
                     'найти человека, который сможет помочь с проблемами в '
                     'обучении или с понимаем того или иного предмета.\n'
                     'Вот что я умею:\n'
                     '/help - получение информации о боте и командах;\n')


@bot.message_handler(commands=['info'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Информация о тебе:\n'
                     'Шарю в: физика;'
                     'Помог: 0;'
                     'Карма: 0.')  # больше инфы


@bot.message_handler(commands=['find'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Готов помочь тебе! Выбери предмет')  # в классе уже есть поиск?


# testing messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
