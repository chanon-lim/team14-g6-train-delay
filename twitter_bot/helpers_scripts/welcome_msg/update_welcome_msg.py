# will update the current welcome message

import requests
from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/direct_messages/welcome_messages/update.json"

headers = {'content-type': 'application/json'}

current_welcome_msg_id = "1468418199725109253"

params = {
    'id': current_welcome_msg_id
}

updated_data = {
    "message_data": {
            "text": "こんにちは！東京電車遅延情報のTwitterBotです。🚊🤖\nBotの機能を使用するために、QuickReplyオプションを使用してください。👇👇",
            "quick_reply": {
                "type": "options",
                "options": [
                    {
                        'label': '🌐 Webサイトに来る',
                        'description': 'もっと情報、ニュース...',
                        'metadata': 'visit_website'
                    },
                    {
                        'label': '🔎 路線の運行情報を見る',
                        'description': '東京で現在の86路線の運行情報',
                        'metadata': 'check_delay_info'
                    },
                    {
                        'label': '🔔 路線の運行情報をフォローする',
                        'description': 'フォローされた路線の遅延の時、DMを受信する',
                        'metadata': f'follow_delay#show_all_operator'
                    },
                    {
                        'label': '❌ 路線の運行情報をフォロー解除する',
                        'description': '路線の遅延通知の受信を停止する',
                        'metadata': 'unfollow_delay#show_all_following_trainline'
                    }
                ]
            }
        }
    }

auths = OAuth1(client_key="Nw0ZC1zhdYQhPvWNP5QpZ2lo6", client_secret="nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs", resource_owner_key="1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq",resource_owner_secret="8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK", signature_type="auth_header")
r = requests.put(url, json=updated_data, auth=auths, params=params)
print(r)
print(r.text)

# <Response [200]>
# {"welcome_message":{"id":"1468418199725109253","created_timestamp":"1638933155362","message_data":{"text":"Welcome, this is the train bot","entities":{"hashtags":[],"symbols":[],"user_mentions":[],"urls":[]},"quick_reply":{"type":"options","options":[{"label":"\ud83d\udcbb Visit our website","metadata":"visit_website","description":"Visit our train delay website for more details..."},{"label":"\ud83d\udd0e Check train delay status","metadata":"check_delay_info","description":"Get current delay info of 86 train lines in Tokyo"},{"label":"\ud83d\udd14 Follow train line status","metadata":"follow_delay_info","description":"Get notified when delay in a train line occur"}]}},"source_app_id":"22688263","name":"simple_welcome_message 03"},"apps":{"22688263":{"id":"22688263","name":"try_twitter_bot","url":"https:\/\/test-bot-g6.herokuapp.com"}}}