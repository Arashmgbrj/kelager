import requests
from pynput.keyboard import Listener , Key
import time
def on_press(key):
   print(key)

with Listener(
        on_press=on_press) as listener:
    listener.join()




