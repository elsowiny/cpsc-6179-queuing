# this script will be ran separately from the main script
# and will communicate with the main script through the
# use of a queue. and event bus
# using http requests


import sys
import threading
import time
import requests


def heart_beat():
    count = 1
    while True:
        try:
            health = requests.get('http://localhost:8000/health')
            print(health.json(), count)
        except:
            print('error')
        count += 1
        time.sleep(5)


def run():
    thread = threading.Thread(target=heart_beat, args=(), daemon=True)
    thread.start()
    while True:
        time.sleep(1)
