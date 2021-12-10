from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime
from urllib.request import urlopen
import json

# parse from the 'dc:date' to 'django timezone object type'
def date_parsing(s):
    return make_aware(datetime.strptime(s[:-6], '%Y-%m-%dT%H:%M:%S')) 

def name_extractor(s):
    dot_index = -1

    for i in range(len(s)):
        if s[i] == '.':
            dot_index = i
            break
    
    ns = s + "Z"
    res = ""

    last_upper = dot_index + 1
    for i in range(dot_index + 2, len(ns)):
        if ns[i].isupper():
            res += ns[last_upper:i]
            last_upper = i
            if ns[i] != 'Z':
                res += " "
    
    return res

API_KEY = '3d673da4a2bc38c165062f42db9fc7d0d02e884d101a6072450cb3e89e48f9f3'

API_URL = 'https://api-tokyochallenge.odpt.org/api/v4/odpt:TrainInformation?acl:consumerKey='

def get_url(odpt_type):
    return 'https://api-tokyochallenge.odpt.org/api/v4/odpt:{}?acl:consumerKey='.format(odpt_type) + API_KEY

def read_data(odpt_type):
    try:
        response = urlopen(get_url(odpt_type))
        response_data = json.loads(response.read())
        return response_data
        
    except:
        return []

def retreive_exact(data, criteria):
    for info in data:
        if criteria(info):
            return info