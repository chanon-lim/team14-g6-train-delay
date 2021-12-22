import threading
from train_delay.database_util import check_last_update
from train_delay.models import TrainInfo
import tweepy
import datetime
import json

def current_operation_state(train_line_information):
    """Return 'delay' or 'normal' state based on current given trainline information"""
    normal_states = ['平常', '現在、１５分以上の遅延はありません']
    for state in normal_states:
        if state in train_line_information:
            return 'normal'
    return 'delay'

def generate_all_train_line_current_state():
    """Create JSON file state 'delay' or 'normal' of all train line"""
    check_last_update()
    train_info = TrainInfo.objects.all()
    train_line_status = dict()

    updated_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    train_line_status["updated_time"] = updated_time

    train_line_status["status"] = dict()

    for train in train_info:
        print(train.operator_ja)
        current_train_operation_state = current_operation_state(train.information_ja)
        if train.operator_ja not in train_line_status["status"]:
            train_line_status["status"][train.operator_ja] = {}
            train_line_status["status"][train.operator_ja][train.railway_ja] = current_train_operation_state
        if (train.operator_ja in train_line_status["status"]) and (train.railway_ja not in train_line_status["status"][train.operator_ja]):
            train_line_status["status"][train.operator_ja][train.railway_ja] = current_train_operation_state

    train_line_status_json = json.dumps(train_line_status, ensure_ascii=False).encode("utf-8")

    # Writing to json file
    with open("twitter_bot/worker/all_train_line_status.json", "wb") as fout:
        fout.write(train_line_status_json)

    if len(train_info) == 86:
        print("Ok syncing data ok")
    else:
        print("There is a problem")


generate_all_train_line_current_state()