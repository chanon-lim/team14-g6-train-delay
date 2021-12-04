from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime
from urllib.request import urlopen
import json

# parse from the 'dc:date' to 'django timezone object type'
def date_parsing(s):
    return make_aware(datetime.strptime(s[:-6], '%Y-%m-%dT%H:%M:%S')) 

def read_data():
    API_URL = 'https://api-tokyochallenge.odpt.org/api/v4/odpt:TrainInformation?acl:consumerKey=3d673da4a2bc38c165062f42db9fc7d0d02e884d101a6072450cb3e89e48f9f3'

    try:
        response = urlopen(API_URL)
        response_data = json.loads(response.read())
        return response_data
        
    except:
        return []