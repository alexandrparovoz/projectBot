# пытаемся делать бота который показываетпогоду в мноюназначенных пяти городах

import telebot
import requests
import json

token = '5561124412:AAF-xvUlWdtu82A9ysl2GUbPQp-PcQQznX8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
# def helloMessage(message): #  реагирует на старт и приветствует юзера по имени
#     mess = f'Hello,{message.from_user.first_name} {message.from_user.last_name}'
#     bot.send_message(message.chat.id, mess)
def buttonWork(message):  # создаем кнoпки
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # в скобках размер кнопки для смартфона
    button1 = telebot.types.KeyboardButton('Минск')
    button2 = telebot.types.KeyboardButton('Москва')
    button3 = telebot.types.KeyboardButton('Киев')
    button4 = telebot.types.KeyboardButton('Сочи')
    button5 = telebot.types.KeyboardButton('Таллин')
    markup.add(button1)  # добавляем в  список кнопки
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)

    bot.send_message(message.chat.id, 'Hi', reply_markup=markup) #  прикрепляем кнопки к чату


@bot.message_handler(content_types='text')
# def connect(message):  # отвечает на любой текст юзера "Ты написал" + текст юзера
#     bot.send_message(message.chat.id, 'Ты написал: ' + message.text)
def text(message):
    if message.text == 'Минск':
        lat = 53,5359
        lon = 27,3400
    elif message.text == 'Москва':
        lat = 55,4424
        lon = 37,3636
    elif message.text == 'Киев':
        lat = 50,2701
        lon = 30,3102
    elif message.text == 'Сочи':
        lat = 43,3507
        lon = 39,4313
    elif message.text == 'Таллин':
        lat = 59,2601
        lon = 24,451
        res = '{0:.2}'.format(getWeather(message.text) - 273,15)
        bot.send_message(message.chat.id, 'Теmпература в городе сейчас: '+ res + ' градусов.')


def getWeather(lat, lon):
   # response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=cd27eae07fb1563bf37f9ba0231d463b')
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=cd27eae07fb1563bf37f9ba0231d463b')
    data = json.loads(response.text)
    return data['main']['temp']
    #print(response.text)
# @bot.message_handler()
# def text(message):
#     data = json.loads(requests.get('https://www.nbrb.by/api/exrates/rates/'+ message +'?parammode=2').text)    # получаю данные с сайта
#     bot.send_message(message.chat.id,data['Cur_OfficialRate'])    # вывожу информацию и выбираю какую вывожу информацию

bot.polling()