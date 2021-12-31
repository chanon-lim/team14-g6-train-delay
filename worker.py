import requests
from time import sleep

print("Heroku worker run first time")

while True:
    sleep(5)
    try:
        url = "http://localhost:8001/trainbot/home"
        r = requests.get(url)
        print(r)
        print(r.status_code)
        print(r.text)
    except Exception as e:
        print(e)
    sleep(3*60)