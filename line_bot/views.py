from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creator
from line_bot.line_message import lineMessage

@csrf_exempt
def index(request):
    if request.method=='POST':
        request = json.loads(request.body.decode('utf-8'))
        events=request['events']
        for event in events:
            message=event['message']
            reply_token=event['replyToken']
            line_message=lineMessage(message_creator.create_single_text_message(message['text']))
            line_message.reply(reply_token)
        return HttpResponse('ok')