# Returns all URLs and their statuses for the given application. We mark a URL as invalid if it fails the daily validation check. In order to re-enable the URL, call the update endpoint.


import requests

url = "https://api.twitter.com/1.1/account_activity/all/webhooks.json"

TOKEN = "AAAAAAAAAAAAAAAAAAAAAAcyWgEAAAAATH71gyUDt41rc5p2MFUg4Trr648%3D8kvelUhmrD6yqrM9QGpEY4F7IFK6UA3TbFN4ZDF7jF8vl4dqS2"
r = requests.get(url, headers={'Authorization': 'Bearer '+TOKEN})
print(r)
print(r.text)
print(r.json)

# <Response [200]>
# {"environments":[{"environment_name":"bot2","webhooks":[{"id":"1468070567442280449","url":"https://test-bot-g6.herokuapp.com/trainbot","valid":true,"created_timestamp":"2021-12-07 04:11:13 +0000"}]}]}
# <bound method Response.json of <Response [200]>>