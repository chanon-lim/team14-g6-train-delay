from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import base64
import hashlib
import hmac
import json
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
def index(request):
    """Homepage of the chatbot"""
    print("The index method is called")
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
    """Handling CRC events"""
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
        print("Request content type", request.content_type)
        print("Request content params", request.content_params)
        # This part convert the json body -> python dict
        try:
            data = json.loads(request.body)
            print(data)
            print("data type", type(data))
        except:
            print("cannot read using json.loads")
        return HttpResponse(status=200)


