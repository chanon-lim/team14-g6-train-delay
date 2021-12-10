from .models import TrainInfo
from datetime import timedelta, datetime

import pyrebase
from .util import *

# Returns a database object

def get_database():
    config = {
        'apiKey': "AIzaSyCPwAwfC1iexLQg7DLXZf8ROReqE0xwx00",
        'authDomain': "traindelay-b6080.firebaseapp.com",
        'databaseURL': "https://traindelay-b6080-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "traindelay-b6080",
        'storageBucket': "traindelay-b6080.appspot.com",
        'messagingSenderId': "849776989542",
        'appId': "1:849776989542:web:f5e5ca04612ae855b464a7",
        'measurementId': "G-D33397WZD6"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    print(auth)
    database = firebase.database()
    return database

patch_data = {"Seibu":"西武鉄道各線", "Keisei":"京成線", "Keikyu":"京急線", "Keio":"京王線"}

def refresh_database():
    operator_data = read_data('Operator')
    railway_data = read_data('Railway')
    train_info_data = read_data('TrainInformation')

    database = get_database()
    database.update({'last_update': datetime.now().timestamp()})

    TrainInfo.objects.all().delete()

    for data in train_info_data:
        train_info = TrainInfo()
        operator_tag = data["odpt:operator"]
        operator = retreive_exact(operator_data, lambda x: x["owl:sameAs"] == operator_tag)
        railway_ja, railway_en = "", ""
        try:
            railway_tag = data["odpt:railway"]
            railway = retreive_exact(railway_data, lambda x: x["owl:sameAs"] == railway_tag)
            railway_ja = railway["odpt:railwayTitle"]["ja"]
            railway_en = railway["odpt:railwayTitle"]["en"]
        except:
            railway_en = name_extractor(data["owl:sameAs"][22:])
            railway_ja = patch_data[railway_en]
        side_data = {
            "operator_en": operator["odpt:operatorTitle"]["en"],
            "operator_ja": operator["odpt:operatorTitle"]["ja"],
            "railway_en": railway_en,
            "railway_ja": railway_ja,
        }
        train_info.update_train(data, side_data)

def check_last_update():
    database = get_database()
    last_stamp = database.child('last_update').get().val()
    last_datetime = datetime.fromtimestamp(last_stamp)
    current_datetime = datetime.now()

    # The interval is 2 minutes
    if current_datetime - last_datetime > timedelta(minutes=2):
        database.update({'last_update': current_datetime.timestamp()})
        refresh_database()
        return True
    
    else:
        return False

