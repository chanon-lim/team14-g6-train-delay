from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    # a record will have 3 columns, there is case trainline of different operator have same name
    # bad name
    user_twitter_id = models.CharField(max_length=200)
    followed_trainline_name = models.CharField(max_length=200)
    followed_operator_name = models.CharField(max_length=200)

    def __str__(self):
        return f"User ID: {self.user_twitter_id}"