import tweepy

CONSUMER_KEY = "Nw0ZC1zhdYQhPvWNP5QpZ2lo6"
CONSUMER_SECRET = "nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs"
ACCESS_TOKEN = "1465916201155317760-6uKnzE1jguNUurjMYD9atglCO5ejLq"
ACCESS_TOKEN_SECRET = "8NvIuMxRU6WD8U1ZwDpFPT9nmoHSyPFBgMdTSwmvtfEvK"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error")

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
# Tung Vuong Thanh said Hello Tweepy
# Tung Vuong Thanh said RT @nodejs: Happy 26th Birthday, JavaScript 🥳
# Tokyo Train Delay said JR-East.ShonanShinjuku : The Shonan-Shinjuku line was delayed by some trains from the Yokosuka Line to the Utsunomi… https://t.co/IsTYJrw5QD
# Tokyo Train Delay said Tobu.TobuSkytree : At around 5:32, some trains between Oshiage Station and Kita-Senju Station were suspended due to… https://t.co/h56L1aX26y
# Tokyo Train Delay said TokyoMetro.Chiyoda : At around 16:16, the Metro-homway 41, 43, was suspended due to a railroad crossing between the… https://t.co/YolnuQVv9S

# user = api.get_user(screen_name="tonvt12345")
# print(user.name)
# print(user.location)
# for follower in user.followers():
#     print(follower.name)
# THANH TUNG VUONG

# Tung Vuong Thanh
# so to search by twitter name -> need kwargs: screen_name="tonvt12345"

# messages = api.get_direct_messages()
# for message in messages:
#     print(message)

# user = api.get_user(screen_name="tonvt12345")
# id = user.id_str
# print(id)
# 1465928035333713926

# send_message = api.send_direct_message(1465928035333713926, "This is message sent from bot")
# Great, success!

rep_options = [
    {
        "label": "Ok got it!",
        "description": "Description 1",
        "metadata": "external_id_1"
    },
    {
        "label": "I want more information!",
        "description": "Description 2",
        "metadata": "external_id_2"
    }
]
send_message = api.send_direct_message(1465928035333713926, "This is message sent from bot with options", quick_reply_options=rep_options)
# Great, success!!!!!!!!!