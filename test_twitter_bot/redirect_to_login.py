import requests

# oauth_token=ZIaAGwAAAAABWjIHAAABfZDDWZE&oauth_token_secret=X0nmDhDFOsyWcJCugwFdUfHtDLwW5ggG

url = "https://api.twitter.com/oauth/authorize?oauth_token=ZIaAGwAAAAABWjIHAAABfZDDWZE"

r = requests.get(url)
print(r)
print(r.text)
print(r.content)

# after access above link in the browser -> will lead to authorize page -> then move to test-bot

# https://test-bot-g6.herokuapp.com/?oauth_token=ZIaAGwAAAAABWjIHAAABfZDDWZE&oauth_verifier=I4QpRiJHc1mhCto8miH9K8cIJMB1aB6b