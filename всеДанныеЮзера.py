# бот выводит все данные о пользователе

import telebot
import requests
import json

token = '5641723319:AAFmfvLWAPUJjmMxtthg39AfNh79s_Ahxso'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def helloMessage(message):
    mess = f'Hello,{message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, message)

bot.polling()