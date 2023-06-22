# бот обмена валюты от Максима работает
import json
import telebot
import requests

token = '5641723319:AAFmfvLWAPUJjmMxtthg39AfNh79s_Ahxso'
bot = telebot.TeleBot(token)

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

usd = False
eur = False
cny = False

@bot.message_handler(content_types='text')
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
        fin = countCource(c, message.text)
        try:
            bot.send_message(message.chat.id, fin)
        except Exception:
            print('no message')
        usd = False
    elif eur:
        c = getCourse('EUR')
        print(c)
        fin = countCource(c, message.text)
        bot.send_message(message.chat.id, fin)
        eur = False
    elif cny:
        c = getCourse('CNY')
        print(c)
        fin = countCource(c, message.text)
        bot.send_message(message.chat.id, fin)
        cny = False


def getCourse(cur):
    data = ''
    try:
        response = requests.get('https://www.nbrb.by/api/exrates/rates/'+cur+'?parammode=2')
        data = json.loads(response.text)
    except Exception:
        data = {'Cur_OfficialRate' : 'error'}
    return data['Cur_OfficialRate']

def countCource(cource, number):
    c = float(cource)
    n = float(number)
    return c*n

bot.polling()