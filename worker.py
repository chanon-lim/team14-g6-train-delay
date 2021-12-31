import requests
from time import sleep
import os

print("Heroku worker run first time")
HEROKU_PORT = os.environ.get('PORT')
print(f"========\n\nPORT: {HEROKU_PORT}\n=============")

while True:
    sleep(5)
    try:
        url = "http://g6-twitter-bot.herokuapp.com/trainbot/home"
        r = requests.get(url)
        print(r)
        print(r.status_code)
        print(r.text)
    except Exception as e:
        print(e)
    sleep(3*60)