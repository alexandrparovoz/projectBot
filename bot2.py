import telebot
import requests
import json

token = '5641723319:AAFmfvLWAPUJjmMxtthg39AfNh79s_Ahxso'
bot = telebot.TeleBot(token)

usd = False
eur = False
cny = False


@bot.message_handler(commands=['start'])
def helloMessage(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('USD')
    button1 = telebot.types.KeyboardButton('EUR')
    button2 = telebot.types.KeyboardButton('CNY')
    markup.add(button)
    markup.add(button1)
    markup.add(button2)


    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    global usd
    global eur
    global cny
    if message.text == 'USD':
        usd = True
    elif message.text == 'EUR':
        eur = True
    elif message.text == 'CNY':
        cny = True
    elif usd:
        c = getCourse('USD')
        print(c)
        fin = countCourse(c, message.text)
        bot.send_message(message.chat.id, fin)
        usd = False
    elif eur:
        c = getCourse('USD')
        print(c)
        fin = countCourse(c, message.text)
        bot.send_message(message.chat.id, fin)
        eur = False
    elif cny:
        c = getCourse('USD')
        print(c)
        fin = countCourse(c, message.text)
        bot.send_message(message.chat.id, fin)
        cny = False
    if message.text == 'USD' or message.text == 'EUR' or message.text == 'CNY':
        res = getCourse(message.text)
        bot.send_message(message.chat.id, res)
    else:
        bot.send_message(message.chat.id, 'Я так не умею!')
    # if message.text == 'машинка':
    #     bot.send_message(message.chat.id, 'Зеленая')
    # if message.text == 'цветок':
    #     bot.send_message(message.chat.id, 'Красный')

def getCourse(cur):
    response = requests.get('https://www.nbrb.by/api/exrates/rates/'+cur+'?parammode=2')
    data = json.loads(response.text)
    return data["Cur_OfficialRate"]

def countCourse(course, number):
    c = float(course)
    n = float(number)
    return c * n


bot.polling()