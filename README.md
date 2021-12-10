# team14-g6-train-delay

Team 14 (Group 6) team exercise for making train delay web applciation.

# Requirements

```
pip install -r requirements.txt
```

# Change this in settings.py in the django server you use to host the bots

```
MONGODB_URI = "mongodb+srv://p:p@cluster0.hgt7v.mongodb.net/g6t14traindelay?retryWrites=true&w=majority"

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
