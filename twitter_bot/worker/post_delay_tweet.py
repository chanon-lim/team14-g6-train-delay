import threading
from train_delay.database_util import check_last_update
from train_delay.models import TrainInfo
import tweepy
import datetime
import json
from twitter_bot.dm_manager import bot_reply_manager
from twitter_bot.worker import NUMBER_OF_TRAINLINE
import pytz
from twitter_bot.dm_manager.bot_reply_manager import BotReplyManager

PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH = 'twitter_bot/worker/all_train_line_status.json'
TRAIN_OPERATION_STATUS_PROTOTYPE_FILE_PATH = "twitter_bot/worker/all_train_line_status_prototype.json"

bot_reply_manager = BotReplyManager()

# ugly, need refactor 
def delay_notify_worker():
    """Fetch the data from database server, check for delay, if there is delay -> post tweet + send DM to registered users"""
    # print("==================")
    # print(datetime.datetime.now())
    # print("Start delay notify worker!")
    database_updated_sucessfully = update_database()
    updated_time = datetime.datetime.now()
    train_info = TrainInfo.objects.all()
    notify_info_to_tweet = [] # what will be posted in tweet, list of tuple [(railway_ja, information_ja, operator_ja)]
    normal_info_DEV = [] # same with notify_info but reverse
    with open(PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH, 'r', encoding="utf-8") as fin:
        previous_train_operation_status_json = fin.read()
        previous_all_train_operation_status_data = json.loads(previous_train_operation_status_json)
        last_updated_time = previous_all_train_operation_status_data["updated_time"]
        last_updated_time = datetime.datetime.strptime(last_updated_time, '%Y-%m-%d %H:%M')
    if database_updated_sucessfully:
        # if last update is longer than 6 min -> cannot use old delay data to compare
        if (updated_time - last_updated_time) > datetime.timedelta(minutes=6):
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                if current_operation_status == 'delay':
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state(train_info, updated_time)
        else:
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                previous_status = previous_all_train_operation_status_data["status"][trainline.operator_ja][trainline.railway_ja]
                if current_operation_status == "delay" and previous_status != "delay":
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state(train_info, updated_time)
    else: # if not update successfully
        if (updated_time - last_updated_time) > datetime.timedelta(minutes=6):
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                if current_operation_status == 'delay':
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state_when_database_update_fail(train_info, updated_time)
        else:
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                previous_status = previous_all_train_operation_status_data["status"][trainline.operator_ja][trainline.railway_ja]
                if current_operation_status == "delay" and previous_status != "delay":
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state_when_database_update_fail(train_info, updated_time)
        
    # now post tweet and notify users through DM
    # print(notify_info_to_tweet)
    if len(notify_info_to_tweet) != 0:
        # send DM
        send_delay_data_and_dm_users_from(bot_reply_manager, delay_data=notify_info_to_tweet)
        
        # tweet
        for delay_train in notify_info_to_tweet:
            tweet_content = ''
            update_time = datetime.datetime.now(tz=pytz.timezone("Asia/Tokyo")).strftime("%H:%M")
            train_line_name = delay_train[0]
            delay_info = delay_train[1]
            # max number of character for tweet in Japanese
            if len(delay_info) >= 110:
                delay_info_split = delay_info.split("。")
                delay_info = delay_info_split[0]
            tweet_content += '[{0}]\n'.format(update_time)
            tweet_content += '{0} : {1}\n～～～\nBotの機能をしようするために、DMを送ってください。💬'.format(train_line_name, delay_info)
            post_tweet(tweet_content)   

    print("delay_notify_worker ends")

def DEV_delay_notify_worker():
    """Fetch the data from database server, check for delay, if there is delay -> post tweet + send DM to registered users"""
    print("==================")
    print(datetime.datetime.now())
    print("Start delay notify worker!")
    database_updated_sucessfully = update_database()
    updated_time = datetime.datetime.now()
    train_info = TrainInfo.objects.all()
    notify_info_to_tweet = [] # what will be posted in tweet, list of tuple [(railway_ja, information_ja, operator_ja)]
    normal_info_DEV = [] # same with notify_info but reverse
    with open(PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH, 'r', encoding="utf-8") as fin:
        previous_train_operation_status_json = fin.read()
        previous_all_train_operation_status_data = json.loads(previous_train_operation_status_json)
        last_updated_time = previous_all_train_operation_status_data["updated_time"]
        last_updated_time = datetime.datetime.strptime(last_updated_time, '%Y-%m-%d %H:%M')
    if database_updated_sucessfully:
        # if last update is longer than 6 min -> cannot use old delay data to compare
        if (updated_time - last_updated_time) > datetime.timedelta(minutes=6):
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                if current_operation_status == 'delay':
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state(train_info, updated_time)
        else:
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                previous_status = previous_all_train_operation_status_data["status"][trainline.operator_ja][trainline.railway_ja]
                if current_operation_status == "delay" and previous_status != "delay":
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state(train_info, updated_time)
    else: # if not update successfully
        if (updated_time - last_updated_time) > datetime.timedelta(minutes=6):
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                if current_operation_status == 'delay':
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state_when_database_update_fail(train_info, updated_time)
        else:
            for trainline in train_info:
                current_operation_status = current_operation_state(trainline.information_ja)
                previous_status = previous_all_train_operation_status_data["status"][trainline.operator_ja][trainline.railway_ja]
                if current_operation_status == "delay" and previous_status != "delay":
                    notify_info_to_tweet.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
                if current_operation_status == 'normal':
                    normal_info_DEV.append((trainline.railway_ja, trainline.information_ja, trainline.operator_ja))
            update_all_train_line_current_state_when_database_update_fail(train_info, updated_time)
        
    # now post tweet and notify users through DM
    print(notify_info_to_tweet)
    print(f"Normal operation info: {normal_info_DEV}")
    if len(normal_info_DEV) != 0:
        DEV_send_normal_data_and_dm_users_from(bot_reply_manager, normal_data=normal_info_DEV)

    if len(notify_info_to_tweet) != 0:
        # send DM
        # send_delay_data_and_dm_users_from(bot_reply_manager, delay_data=notify_info_to_tweet)
        
        # tweet
        for delay_train in notify_info_to_tweet:
            tweet_content = ''
            update_time = datetime.datetime.now(tz=pytz.timezone("Asia/Tokyo")).strftime("%H:%M")
            tweet_content += '[{0}]\n'.format(update_time)
            tweet_content += '{0} : {1}\n'.format(delay_train[0], delay_train[1])
            post_tweet(tweet_content)   

    print("delay_notify_worker ends")

def DEV_send_normal_data_and_dm_users_from(bot_reply_manager: BotReplyManager, normal_data):
    bot_reply_manager.DEV_NOTIFY_NORMAL_notify_trainline_normal_to_follower(normal_data)

def send_delay_data_and_dm_users_from(bot_reply_manager: BotReplyManager, delay_data):
    bot_reply_manager.NOTIFY_DELAY_notify_trainline_delay_to_follower(delay_data)

def update_database():
    """Update the database and return True if successful, False otherwise. Will try 3 times. Success is when the train num is 86"""
    print("Start update database")
    database_update_try = 0
    while database_update_try < 3:
        check_last_update()
        train_info = TrainInfo.objects.all()
        if len(train_info) == NUMBER_OF_TRAINLINE:
            print("Finish update database")
            return True
        database_update_try += 1
    print("Finish update database")
    return False

def current_operation_state(train_line_information):
    """Return 'delay' or 'normal' state based on current given trainline information"""
    normal_states = ['平常', '現在、１５分以上の遅延はありません']
    for state in normal_states:
        if state in train_line_information:
            return 'normal'
    return 'delay'

def update_all_train_line_current_state(train_info, updated_time):
    """After check delay, update the JSON file"""
    train_line_status = dict()

    updated_time = updated_time.strftime('%Y-%m-%d %H:%M')
    train_line_status["updated_time"] = updated_time

    train_line_status["status"] = dict()

    for train in train_info:
        current_train_operation_state = current_operation_state(train.information_ja)
        if train.operator_ja not in train_line_status["status"]:
            train_line_status["status"][train.operator_ja] = {}
            train_line_status["status"][train.operator_ja][train.railway_ja] = current_train_operation_state
        if (train.operator_ja in train_line_status["status"]) and (train.railway_ja not in train_line_status["status"][train.operator_ja]):
            train_line_status["status"][train.operator_ja][train.railway_ja] = current_train_operation_state

    train_line_status_json = json.dumps(train_line_status, ensure_ascii=False).encode("utf-8")

    # Writing to json file
    with open(PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH, "wb") as fout:
        fout.write(train_line_status_json)

def update_all_train_line_current_state_when_database_update_fail(train_info, updated_time):
    """Get the data prototype from JSON file and replace the fetched data to that and update the all_train_line_status.json"""
    with open(TRAIN_OPERATION_STATUS_PROTOTYPE_FILE_PATH, 'r', encoding='utf-8') as fin:
        train_line_status_json = fin.read()
        train_line_status = json.loads(train_line_status_json)
    
    # update the time
    updated_time = updated_time.strftime('%Y-%m-%d %H:%M')
    train_line_status["updated_time"] = updated_time

    for train in train_info:
        current_train_operation_state = current_operation_state(train.information_ja)
        train_line_status["status"][train.operator_ja][train.railway_ja] = current_train_operation_state

    train_line_status_json = json.dumps(train_line_status, ensure_ascii=False).encode("utf-8")

    # Writing to json file
    with open("twitter_bot/worker/all_train_line_status.json", "wb") as fout:
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

    api.update_status(tweet_content, attachment_url="https://twitter.com/messages/compose?recipient_id=1465916201155317760")


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
    initial_db_update_thread = threading.Thread(target=update_database, daemon=True)
    initial_db_update_thread.start()
    set_interval(delay_notify_worker, 60*5)