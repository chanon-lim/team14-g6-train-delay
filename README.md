# Tokyo Train Delay

## Overview

Team 14 exercises for making train delay web applications, LINE bot, and Twitter bot. This application is the **upgrade version** of the previous version of the application submitted in [4th Open Data Challenge for Public Transportation in Tokyo](https://tokyochallenge.odpt.org/index.html). 

Submitted version (Special Prize) could be found here: https://github.com/chanon-mike/tokyo-train-delays

## Link
⚠️The API from the open data challenge cannot currently be used. As a result, the server is being shut down.⚠️
- Web App: https://train-delay-chien.herokuapp.com/
- Twitter Bot: https://twitter.com/g6_bot
- LINE Bot
  
![LINEQR](https://user-images.githubusercontent.com/85671768/148489924-081a7f8a-f8f1-404d-8670-4106b0693459.png)

## Presentation Slide

URL: https://drive.google.com/file/d/1H20a9v7KwEb7Z4fjw_jCsYDN_URRZPMf/view?usp=sharing

![slide](https://github.com/chanon-mike/train-delay-team14/assets/27944646/b73804fa-d0f6-4a28-9ddf-50af26a4a588)

# Images

## Web Application
![homepage](https://github.com/chanon-lim/team14-g6-train-delay/assets/85671768/8fa8c5fe-c967-4a0b-b2f8-17bd3ae2adca)
![delay_info](https://github.com/chanon-lim/team14-g6-train-delay/assets/85671768/659c5fe2-7207-47fd-888e-cf9824b640e0)
## Twitter
![Twitter Tweet](https://github.com/chanon-mike/train-delay-team14/assets/27944646/205eac77-d164-4c50-b72b-91e62f72bcb4)
![Twitter DM](https://github.com/chanon-mike/train-delay-team14/assets/27944646/3c47bf6a-2559-4af0-a317-72adc19b680e)
## LINE
![LINE bot](https://github.com/chanon-mike/train-delay-team14/assets/27944646/59ad7217-a513-4242-9e6a-84298fce9716)


# Installation 

## Requirements

```
pip install -r requirements.txt
```

## Change this in settings.py in the django server you use to host the bots

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
