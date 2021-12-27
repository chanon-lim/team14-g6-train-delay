# use the ID from the create_welcome_msg.py to register the welcome msg

import requests
from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json"

headers = {'content-type': 'application/json'}
# the 'welcome_message_id' is from create_welcome_msg.py'
data = {
    "welcome_message_rule": {
        "welcome_message_id": "1468418199725109253"
    }
}
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type="auth_header")
r = requests.post(url, json=data, auth=auths)
print(r)
print(r.text)

# Success!!!!!
# <Response [200]>
# {"welcome_message_rule":{"id":"1468410174042157063","created_timestamp":"1638931241890","welcome_message_id":"1468404540643110916"}}

# Then I make new welcome msg with options, I delete the old rule first then I make new one
# <Response [200]>
# {"welcome_message_rule":{"id":"1468419365611573251","created_timestamp":"1638933433331","welcome_message_id":"1468418199725109253"}}