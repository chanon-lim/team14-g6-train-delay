# team14-g6-train-delay
Team 14 (Group 6) team exercise for making train delay web applciation.

# Migrate & database initialization
Whenever you initialize the database, please do this.
```
python manage.py migrate
python manage.py shell

$ from train_delay.database_util import *
$ refresh_database()
```

Whenever do something with view, import `check_last_update()` from `train_delay.database_util` and call it.