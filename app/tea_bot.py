import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)
chat_id = -1001797149316

@bot.message_handler(commands=['button'])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Нихуя, ты здороваться умеешь?")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Тебе только бог поможет")
        print(message)
    elif message.text == "/start":
        bot.send_message(message.chat.id, "хуярт")
    elif message.text == ("деремся" or "дерёмся" or "Дерёмся" or "Деремся"):
        bot.send_message(message.chat.id, "ОООО, СКРИНТЕ НАХУЙ")
        print(bot.get_chat(-1001797149316))

bot.polling(none_stop=True, interval=0)