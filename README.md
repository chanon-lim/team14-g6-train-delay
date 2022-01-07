# team14-g6-train-delay

Team 14 (Group 6) team exercise for making train delay web applciation.

- Web App: https://train-delay-chien.herokuapp.com/
- Twitter Bot: https://twitter.com/g6_bot
- LINE Bot 

![LINEQR](https://user-images.githubusercontent.com/85671768/148489924-081a7f8a-f8f1-404d-8670-4106b0693459.png)

# Requirements

```
pip install -r requirements.txt
```

# Change this in settings.py in the django server you use to host the bots

```
MONGODB_URI = "mongodb+srv://p:p@cluster0.ldjyq.mongodb.net/t6g14traindelay?retryWrites=true&w=majority"

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "t6g14traindelay",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": MONGODB_URI,
        },
    },
}
```

Whenever do something with view, import `check_last_update()` from `train_delay.database_util` and call it.
