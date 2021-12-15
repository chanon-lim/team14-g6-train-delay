# return the subcription of user in the webhook

import requests

url = "https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json"

TOKEN = "AAAAAAAAAAAAAAAAAAAAAAcyWgEAAAAATH71gyUDt41rc5p2MFUg4Trr648%3D8kvelUhmrD6yqrM9QGpEY4F7IFK6UA3TbFN4ZDF7jF8vl4dqS2"
r = requests.get(url, headers={'Authorization': 'Bearer '+TOKEN})
print(r)
print(r.text)
