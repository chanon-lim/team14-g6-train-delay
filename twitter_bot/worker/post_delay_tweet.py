import threading
from train_delay.database_util import check_last_update
from train_delay.models import TrainInfo
import tweepy
import datetime

def check_delay():
    check_last_update()
    train_info = TrainInfo.objects.all()
    delay_info = []
    normal_states = ['平常', '現在、１５分以上の遅延はありません']
    for trainline in train_info:
        is_delay = True
        for normal_state in normal_states:
            if normal_state in trainline.information:
                is_delay = False
                break
        if is_delay:
            print(trainline.railway)
            print(trainline.information)
            delay_info.append((trainline.railway, trainline.information))
        print("==================================")
    if len(delay_info) != 0:
        tweet_content = ''
        for delay_train in delay_info:
            update_time = datetime.datetime.now().strftime("%H:%M")
            tweet_content += '[{0}]\n'.format(update_time)
            tweet_content += '{0} : {1}\n'.format(delay_train[0], delay_train[1])
            post_tweet(tweet_content)
            tweet_content = ''

def post_tweet(tweet_content):
    """Post tweet"""
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

    api.update_status(tweet_content)


def set_interval(func, sec):
    """This function execute 'func' every 'sec' seconds, like setInterval in JS"""
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.daemon = True
    t.start()
    return t

def print_test():
    """Print "test" to console in every 10 secs"""
    print("Hello!!!")

def start_worker():
    """Worker will check train info every 5 min"""
    set_interval(check_delay, 60*5)