# Triggers the challenge response check (CRC) for the given webhook's URL. If the check is successful, returns 204 and reenables the webhook by setting its status to valid.

import requests
from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/account_activity/webhooks/1467936948417605632.json"
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq", signature_type="auth_header", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK")
r = requests.put(url, auth=auths)
print(r)
print(r.text)