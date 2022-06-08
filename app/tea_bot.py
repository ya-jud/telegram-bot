import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)
chat_id = -1001797149316

bot.send_message(chat_id, "Я ЖИВ")

@bot.message_handler(commands=['my_info'])
def get_user_info(message):
    markup = types.InlineKeyboardMarkup()
    get_user_id = types.InlineKeyboardButton(text="Мой ID", callback_data="get_id") # создаем кнопку
    get_user_username = types.InlineKeyboardButton(text="Мой ник", callback_data="get_username") # создаем кнопку
    get_user_first_name = types.InlineKeyboardButton(text="Моё имя", callback_data="get_first_name") # создаем кнопку
    markup.add(get_user_id, get_user_username, get_user_first_name) # кнопки делаем рабочими
    bot.send_message(message.chat.id, "Что именно хочешь знать?", reply_markup=markup) # добавляем к сообщению бота кнопки, которые указаны выше

@bot.callback_query_handler(func=lambda call: True)
def return_info(call):
    # if call.data == "get_id": 
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     item_id = types.KeyboardButton('ID')
    #     markup.add(item_id)
    #     bot.send_message(call.message.chat.id, "Тыкай", reply_markup=markup)
    if call.data == "get_id":
        bot.send_message(call.from_user.id, f"Твой ID: { call.from_user.id }")
    elif call.data == "get_username":
        bot.send_message(call.from_user.id, f"Твой ник: { call.from_user.username }")
    elif call.data == "get_first_name":
        bot.send_message(call.from_user.id, f"Твоё имя: { call.from_user.first_name }")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Нихуя, ты здороваться умеешь?")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Тебе только бог поможет")
    elif message.text == "/start":
        bot.send_message(message.chat.id, "хуярт")
    elif message.text.lower() == ("деремся" or "дерёмся"):
        bot.send_message(message.chat.id, "ОООО, СКРИНТЕ НАХУЙ")

bot.polling(none_stop=True, interval=0)