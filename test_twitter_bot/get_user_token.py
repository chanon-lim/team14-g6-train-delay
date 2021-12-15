import requests

url = "https://api.twitter.com/oauth/access_token?oauth_verifier=I4QpRiJHc1mhCto8miH9K8cIJMB1aB6b&oauth_token=ZIaAGwAAAAABWjIHAAABfZDDWZE"
r = requests.post(url)
print(r)
print(r.content)
print(r.text)