# выводим приветствие и имя пользователя

import telebot
# Создаем экземпляр бота
token = '5641723319:AAFmfvLWAPUJjmMxtthg39AfNh79s_Ahxso'
bot = telebot.TeleBot(token)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)
