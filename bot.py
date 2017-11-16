import config

import telebot
import logging
import logging.config

bot = telebot.TeleBot(config.TOKEN)

logging.config.fileConfig('logging.conf')
bot_logger = logging.getLogger('TeleBot')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Привет, %s!\nЧто хочешь сделать?' %message.chat.first_name)


# testing messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
