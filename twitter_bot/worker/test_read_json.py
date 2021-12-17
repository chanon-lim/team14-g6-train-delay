import json

PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH = 'twitter_bot/worker/all_train_line_status.json'

with open(PREVIOUS_TRAIN_OPERATION_STATUS_FILE_PATH, 'r') as fin:
    previous_train_operation_status_json = fin.read()
    previous_train_operation_status = json.loads(previous_train_operation_status_json)
print(previous_train_operation_status)

# !!!: Ok worked!!!!