import requests
from requests_oauthlib import OAuth1
import json

# TOKEN = r"AAAAAAAAAAAAAAAAAAAAAAcyWgEAAAAAm%2FXDPsHwcbcwn3OVW3EK%2Fo4bWG4%3D3otWkb6BdGdr0VLyGzAaGZC1qEux8mRMn2L1E7vEVQ8WviAjSo"
# r = requests.get("https://api.twitter.com/2/tweets/20?expansions=author_id", headers={'Authorization': 'Bearer '+TOKEN})

# print(r.json())

# this is code for testing send GET request to the webhooks
# param = {
#     'crc_token': 'foo'
# }

# url = "https://test-bot-g6.herokuapp.com/trainbot"
# r = requests.get(url, params=param)
# print(r.json())

# TOKEN = r"AAAAAAAAAAAAAAAAAAAAAAcyWgEAAAAAm%2FXDPsHwcbcwn3OVW3EK%2Fo4bWG4%3D3otWkb6BdGdr0VLyGzAaGZC1qEux8mRMn2L1E7vEVQ8WviAjSo"
# r = requests.get("https://api.twitter.com/1.1/account_activity/webhooks/1467832893456089092/subscriptions/all.json", headers={'Authorization': 'Bearer '+TOKEN})

# print(r)
# print(r.json())
# {'errors': [{'code': 34, 'message': 'Sorry, that page does not exist.'}]}

######################################
# url = "https://api.twitter.com/1.1/account_activity/webhooks/1467832893456089092/subscriptions/all.json"
# auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq", signature_type="auth_header")
# r = requests.post(url, auth=auths)
# print(r)
# print(r.json())

########################################
url = 'https://api.twitter.com/oauth/request_token?oauth_callback=https%3A%2F%2Ftest-bot-g6.herokuapp.com'
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6",resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type="auth_header")
r = requests.post(url, auth=auths)
print(r)
print(type(r))
print(r.status_code)
print(r.content)
print(r.text)