import requests
from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/destroy.json"

params = {'id': "1468410174042157063"}
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type="auth_header")
r = requests.delete(url, params=params, auth=auths)
print(r)
print(r.text)

# !!!: Success <Response [204]>