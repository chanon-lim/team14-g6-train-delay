# Wrapper for tweepy, call API to send DM
import tweepy
from tweepy import auth
from twitter_bot.dm_manager import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class APIManager(tweepy.API):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def __init__(self):
        super().__init__(self.auth)

