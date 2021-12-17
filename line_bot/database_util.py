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

def refresh_database():
    wholedata = read_data()
    database = get_database()
    database.update({'last_update': datetime.now().timestamp()})

    TrainInfo.objects.all().delete()

    for data in wholedata:
        train_info = TrainInfo()
        train_info.update_train(data)

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