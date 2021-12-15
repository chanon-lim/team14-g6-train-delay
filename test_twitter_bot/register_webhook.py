import requests
from requests_oauthlib import OAuth1

# param = {
#     'token': 12345
# }

# url = "https://test-bot-g6.herokuapp.com/trainbot"
# r = requests.get(url, params=param)
# print(r.json())

# register for webhook, pray for success
# para = {
#     'url': "https://test-bot-g6.herokuapp.com/trainbot"
# }
# url = r"https://api.twitter.com/1.1/account_activity/all/dev/webhooks.json?url=https%3A%2F%2Ftest-bot-g6.herokuapp.com%2trainbot"
# url = "https://api.twitter.com/1.1/account_activity/all/dev/webhooks.json?url=https://test-bot-g6.herokuapp.com/trainbot"
# r = requests.post(url)
# print(r)
# print(r.json())

# This the code for registering webhooks
url = "https://api.twitter.com/1.1/account_activity/all/bot2/webhooks.json?url=https%3A%2F%2Fd686-14-248-13-145.ngrok.io%2Ftrainbot"
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq", signature_type="auth_header", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK")
r = requests.post(url, auth=auths)
print(r)
print(r.json())