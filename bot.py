import telebot
from telebot import types

bot = telebot.TeleBot('')

class IsAdmin (telebot.custom_filters.SimpleCustomFilter):
    key = 'is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']

bot.add_custom_filter(IsAdmin())

@bot.message_handler(is_admin=True)

def admin_of_group(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, начальник!')

@bot.message_handler(content_types=['text'])

def get_message_group(message):
    if message.chat.id == "group":
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Ты отсталый?")

def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Нихуя, ты здороваться умеешь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Тебе только бог поможет")
    elif message.text == "хочешь чаю?":
        photo = open('./photo.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Ты отсталый?")

markup = types.ReplyKeyboardMarkup(row_width=2)
btn_1 = types.KeyboardButton('btn 1')
btn_2 = types.KeyboardButton('btn 2')
markup.add(btn_1, btn_2)

bot.polling(none_stop=True, interval=0)