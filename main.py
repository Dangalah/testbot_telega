import telebot
import random

from configs.config import token
from configs.main import main_menu
from telebot import types

bot = telebot.TeleBot(token=token)
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('/start')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sti = open('stick/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("random")
    markup.add(item1)

    bot.send_message(message.chat.id, "Ny zdorova molodoi, {0.first_name}!\nYa - <b>{1.first_name}</b>, gotov' o4ko))0)".format(message.from_user, bot.get_me()),
        parse_mode='html',
        reply_markup=markup)

@bot.message_handler(content_types=['text'])
def povtoryai(message):
    if message.chat.type == 'private':
        if message.text == 'random':
            bot.send_message(message.chat.id, str(random.randint(0,100)))

bot.polling(none_stop=True)