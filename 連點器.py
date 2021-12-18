#東東連點器0.6版

import pyautogui
from pynput import keyboard
import threading

run = False
th = []


def n1():
    def on_release(key):
        global run
        try:
            if format(key.char) == '`':
                run = not(run)
        except AttributeError:
            pass
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

def n2():
    while True:
        if run:
            xloc, yloc = pyautogui.position()
            pyautogui.click(xloc, yloc, button='left', duration=0)

for i in range(5):
    tha = threading.Thread(target=n2)
    th.append(tha)

tha = threading.Thread(target=n1)
th.append(tha)

for i in th:
    i.start()
for i in th:
    i.join()