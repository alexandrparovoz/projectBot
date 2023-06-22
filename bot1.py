import telebot


token = '5641723319:AAFmfvLWAPUJjmMxtthg39AfNh79s_Ahxso'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def helloMessage(message):  # реагирует на старт и приветствует юзера по имени
        mess = f'Hello,{message.from_user.first_name} {message.from_user.last_name}'
        bot.send_message(message.chat.id, mess)

@bot.message_handler(content_types=['text'])
def text(message):  # реагирует на любой текст и отвечает " Я тебя понимаю!"
    bot.send_message(message.chat.id, " Я тебя понимаю!")

@bot.message_handler(content_types=['text'])
def text(message):  # анализ текста пользователя и реакция на него
    if message.text == 'car':
        bot.send_message(message.chat.id, 'green')
    if message.text == 'flower':
        bot.send_message(message.chat.id, 'yellow')


bot.polling()