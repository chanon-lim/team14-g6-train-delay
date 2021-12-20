import threading
from train_delay.database_util import check_last_update
from train_delay.models import TrainInfo
import tweepy
import datetime
import json

PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH = 'twitter_bot/worker/all_train_line_status.json'

def delay_notify_worker():
    print("delay_notify_worker starts!")
    check_last_update()
    train_info = TrainInfo.objects.all()
    notify_info = [] # what will be posted in tweet
    with open(PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH, 'r') as fin:
        previous_train_operation_status_json = fin.read()
        previous_all_train_operation_status_data = json.loads(previous_train_operation_status_json)
    for trainline in train_info:
        current_operation_status = current_operation_state(trainline.information_ja)
        if current_operation_status == 'delay':
            previous_status = previous_all_train_operation_status_data[trainline.operator_ja][trainline.railway_ja]
            if previous_status != 'delay':
                notify_info.append((trainline.railway_ja, trainline.information_ja))
    if len(notify_info) != 0:
        for delay_train in notify_info:
            tweet_content = ''
            update_time = datetime.datetime.now().strftime("%H:%M")
            tweet_content += '[{0}]\n'.format(update_time)
            tweet_content += '{0} : {1}\n'.format(delay_train[0], delay_train[1])
            post_tweet(tweet_content)
    print("notify_info", notify_info)
    update_all_train_line_current_state(train_info)
    print("delay_notify_worker finishes!")

def current_operation_state(train_line_information):
    """Return 'delay' or 'normal' state based on current given trainline information"""
    normal_states = ['平常', '現在、１５分以上の遅延はありません']
    for state in normal_states:
        if state in train_line_information:
            return 'normal'
    return 'delay'

def update_all_train_line_current_state(train_info):
    """After check delay, update the JSON file"""
    train_line_status = dict()
    for train in train_info:
        print(train.operator_ja)
        current_train_operation_state = current_operation_state(train.information_ja)
        if train.operator_ja not in train_line_status:
            train_line_status[train.operator_ja] = {}
            train_line_status[train.operator_ja][train.railway_ja] = current_train_operation_state
        if (train.operator_ja in train_line_status) and (train.railway_ja not in train_line_status[train.operator_ja]):
            train_line_status[train.operator_ja][train.railway_ja] = current_train_operation_state

    train_line_status_json = json.dumps(train_line_status)

    # Writing to json file
    with open("twitter_bot/worker/all_train_line_status.json", "w") as fout:
        fout.write(train_line_status_json)

def generate_all_train_line_current_state():
    """Create JSON file state 'delay' or 'normal' of all train line"""
    check_last_update()
    train_info = TrainInfo.objects.all()
    train_line_status = dict()
    for train in train_info:
        print(train.operator_ja)
        current_train_operation_state = current_operation_state(train.information_ja)
        if train.operator_ja not in train_line_status:
            train_line_status[train.operator_ja] = {}
            train_line_status[train.operator_ja][train.railway_ja] = current_train_operation_state
        if (train.operator_ja in train_line_status) and (train.railway_ja not in train_line_status[train.operator_ja]):
            train_line_status[train.operator_ja][train.railway_ja] = current_train_operation_state

    train_line_status_json = json.dumps(train_line_status)

    # Writing to json file
    with open("twitter_bot/worker/all_train_line_status.json", "w") as fout:
        fout.write(train_line_status_json)

# will need to refactor, using the APIManager
def post_tweet(tweet_content):
    """Wrapper for tweepy post tweet API"""
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
    # Generate the current delay/normal state of all train line
    generate_all_train_line_current_state()
    set_interval(delay_notify_worker, 60*5)