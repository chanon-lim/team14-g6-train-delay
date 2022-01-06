from django.http import HttpResponse, JsonResponse
import base64
import hashlib
import hmac
import json
from django.views.decorators.csrf import csrf_exempt
from twitter_bot.dm_manager.event_manager import EventManager
from twitter_bot.dm_manager import CONSUMER_SECRET
from twitter_bot.dm_manager.twitter_event import TwitterEvent

# Create your views here.
# Test to use worker internal
def index(request):
    """Homepage of the chatbot"""
    print("The index method is called")
    import tweepy
    from datetime import datetime

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
    now = datetime.now()
    now_str = str(now)
    send_message = api.send_direct_message(1465928035333713926, f"{now_str}\nThis is message sent from internal worker")

    return HttpResponse("This is the home page of Twitter chat bot. You can learn more about our app at our website.")

def test_get_request(request):
    if request.method == 'GET':
        print('Request')
        print(request.GET)
        print('request token')
        print(request.GET['token'])
    return HttpResponse("Get test get request")

@csrf_exempt
def bot_event_manager(request):
    """Handling CRC events and message event when user send DM. Twitter performs CRC test hourly to check the service running or not. The GET method is for handling CRC test"""
    CONSUMER_SECRET = b"nuzgy6dN1SfLoO9czlsGxv5HcpNIxTfRss8eiRS8vS1KOAszBs"
    if request.method == 'GET':
        crc_token = request.GET['crc_token']
        crc_token = bytes(crc_token, 'utf-8')
        print('crc_token', crc_token)
        sha256_hash_digest = hmac.new(CONSUMER_SECRET, msg=crc_token, digestmod=hashlib.sha256).digest()
        decoded = base64.b64encode(sha256_hash_digest).decode("utf-8")
        data = {
            'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest).decode("utf-8")
        }
        response = JsonResponse(data)
        response.status_code = 200
        return response
    # This method run when user send message, Twitter webhook will send POST request to this method. The method has content type header: application/json; the body is a json object, type "bytes"
    if request.method == 'POST':
        # This part convert the json body -> python dict
        twitter_event = TwitterEvent(json.loads(request.body))
        # print(json.loads(request.body))
        twitter_event_manager = EventManager()
        twitter_event_manager.handle_event(twitter_event)
        return HttpResponse(status=200)


