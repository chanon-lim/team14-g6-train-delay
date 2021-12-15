# now register ngrok, but cannot see the post request when write message
# ahh, the reason is when you change the webhook url -> need to register user again

import requests

param = {
    'message': 'Hello world'
}

url = "https://d686-14-248-13-145.ngrok.io/trainbot"
r = requests.post(url, params=param)
print(r)
print(r.text)