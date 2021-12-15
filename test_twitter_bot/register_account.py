from oauthlib.oauth1.rfc5849 import SIGNATURE_HMAC_SHA1, SIGNATURE_TYPE_AUTH_HEADER
import requests
from requests_oauthlib import OAuth1


url = "https://api.twitter.com/1.1/account_activity/all/bot2/subscriptions.json"
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6",  client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs",resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type=SIGNATURE_TYPE_AUTH_HEADER, signature_method=SIGNATURE_HMAC_SHA1)

r = requests.post(url, auth=auths)
print(r)
print(r.content)