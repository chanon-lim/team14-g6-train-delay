# Make new welcome msg content. After making successfully, will receive the welcome msg ID, use this ID to register the welcome msg

import requests
from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json"

headers = {'content-type': 'application/json'}
data = {
    "welcome_message": {
        "name": "simple_welcome_message 03",
        "message_data": {
            "text": "Welcome, this is the train bot",
            "quick_reply": {
                "type": "options",
                "options": [
                    {
                        'label': '🚋 Get latest train info',
                        'description': 'Get hot news',
                        'metadata': 'a'
                    },
                    {
                        'label': '❓ Learn more about our app',
                        'description': 'Go to our app website',
                        'metadata': 'b'
                    }
                ]
            }
        }
    }
}
auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type="auth_header")
r = requests.post(url, json=data, auth=auths)
print(r)
print(r.text)

# <Response [200]>
# {"welcome_message":{"id":"1468418199725109253","created_timestamp":"1638933155362","message_data":{"text":"Welcome, this is the train bot","entities":{"hashtags":[],"symbols":[],"user_mentions":[],"urls":[]},"quick_reply":{"type":"options","options":[{"label":"\ud83d\ude8b Get latest train info","metadata":"a","description":"Get hot news"},{"label":"\u2753 Learn more about our app","metadata":"b","description":"Go to our app website"}]}},"source_app_id":"22688263","name":"simple_welcome_message 03"},"apps":{"22688263":{"id":"22688263","name":"try_twitter_bot","url":"https:\/\/test-bot-g6.herokuapp.com"}}}