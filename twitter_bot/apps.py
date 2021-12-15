from django.apps import AppConfig

class TwitterBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitter_bot'

    def ready(self):
        print("Run the worker")
        from twitter_bot.worker.post_delay_tweet import start_worker
        start_worker() 
