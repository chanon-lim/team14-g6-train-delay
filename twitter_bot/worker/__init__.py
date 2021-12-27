# fixed number of trainline, used to check if there is error in syncing database or not
import json

NUMBER_OF_TRAINLINE = 86
ALL_TRAIN_LINE_FILE_PATH = "twitter_bot/worker/train_line.json"

def get_all_operators():
    """Return all train all operators in list"""
    with open(ALL_TRAIN_LINE_FILE_PATH, 'r', encoding="utf-8") as fin:
        all_train_line_json = fin.read()
        all_train_line_dict = json.loads(all_train_line_json)
        all_train_line = all_train_line_dict["train_line"]
        all_operators = []
        for train_line in all_train_line:
            # train_line have the form ["東武鉄道", "大師線"], the first one is operator, the second one is railway
            if train_line[0] not in all_operators:
                all_operators.append(train_line[0])
    # print("all_operators:", all_operators)
    # all_operators: ['東武鉄道', '東京都交通局', 'JR東日本', '横浜市交通局', '多摩都市モノレール', '仙台市交通局', '東京メトロ', '首都圏新都市鉄道', '京王電鉄', '東急電鉄', '東京臨海', '高速鉄道', '京急電鉄', '西武鉄道', '京成電鉄']
    return all_operators

def get_all_train_line():
    """Return dict of all train line of all operator, in form {'operator A': [trainline1, trainline2,...], ..."""
    with open(ALL_TRAIN_LINE_FILE_PATH, 'r', encoding="utf-8") as fin:
        all_train_line_json = fin.read()
        all_train_line_dict = json.loads(all_train_line_json)
        all_train_line = all_train_line_dict["train_line"]
        all_train_line_in_operator = {}
        for train_line in all_train_line:
            operator_name = train_line[0]
            train_line_name = train_line[1]
            if operator_name not in all_train_line_in_operator:
                all_train_line_in_operator[operator_name] = [train_line_name]
            if (operator_name in all_train_line_in_operator) and (train_line_name) not in all_train_line_in_operator[operator_name]:
                all_train_line_in_operator[operator_name].append(train_line_name)
    # print("all_train_line:", all_train_line_in_operator)
    # print("len JR trainline:", len(all_train_line_in_operator["JR東日本"]))
    # 37
    # all_train_line: {'東武鉄道': ['大師線', '伊勢崎線', '亀戸線', '鬼怒川線', '桐生線', '小泉線', '小泉線(東小泉-太田)', '日光線', '越生線', '佐野線', '東武スカイツリーライン', '東武スカイツリーライン(押上-曳舟)', '東武アーバンパークライン', '東上線', '宇都宮線'], '東京 都交通局': ['浅草線', '三田線', '新宿線', '大江戸線', '東京さくらトラム（都電荒川線）', '日暮里・舎人ライナー'], 'JR東日本': ['中央線快速', '中央・総武各駅停車', '八高線', '伊東 
    return all_train_line_in_operator


ALL_TRAIN_OPERATORS = get_all_operators() 
ALL_TRAIN_LINES = get_all_train_line()
