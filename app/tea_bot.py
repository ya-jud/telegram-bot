import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)
chat_id = -1001797149316


# class IsAdmin (telebot.custom_filters.SimpleCustomFilter):
#     key = 'is_admin'
#     @staticmethod
#     def check(message: telebot.types.Message):
#         return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']

# bot.add_custom_filter(IsAdmin())

# @bot.message_handler(is_admin=True)

# def admin_of_group(message):
#     bot.send_message(message.chat.id, 'Добро пожаловать, начальник!')


# @bot.message_handler(commands=['start'])
# def group_message(message):
#     bot.send_message(message.form_group.id, "хуярт")

markup = types.ReplyKeyboardMarkup()
btn = types.KeyboardButton('test button')
markup.row(btn)
bot.send_message(chat_id, "Choose one letter:")

@bot.message_handler(content_types=['text'])

# def default_test(message):
#     nick = message.from_user.username
#     bot.send_message(message.chat.id, f"@{nick}") выводит ник

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

# @bot.message_handler(commands=['button'])

# @bot.message_handler(content_types=['text'])
# def fight(message):
    

bot.polling(none_stop=True, interval=0)