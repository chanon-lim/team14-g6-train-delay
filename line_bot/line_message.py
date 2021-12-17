from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL='https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN='fVxDRaj5HyhguClw4ZkbjWvGLn2uR216HpNYCad7o8KGZ7erMxXODrZex1gd9NzrywWxcw5HdGx538f1z2wWcDb6kYAGBMPcMi8E19tBHr2K0cqLsfRNNTEyoZu5GPLUnA9At0/69RsISPjv9vh7WwdB04t89/1O/w1cDnyilFU='
HEADER={
    'Content-Type' : 'application/json',
    'Authorization': 'Bearer '+ACCESS_TOKEN
}

class lineMessage():
    def __init__(self,messages):
        self.messages=messages

    def reply(self, reply_token):
        body = {
            'replyToken':reply_token,
            'messages':self.messages
        }
        print(body)
        req=urllib.request.Request(REPLY_ENDPOINT_URL,json.dumps(body).encode(),HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body=res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)