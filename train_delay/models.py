from django.db import models
from .util import date_parsing

# Create your models here.

class TrainInfo(models.Model):
    train_id = models.CharField(max_length=200)
    # date = models.DateTimeField()
    # valid = models.DateTimeField()
    railway = models.CharField(max_length=500)
    operator = models.CharField(max_length=200)
    information = models.CharField(max_length=2000)

    def update_train(self, data):
        self.train_id = data["@id"]
        # self.date = date_parsing(data["dc:date"])
        # self.valid = date_parsing(data["dct:valid"])
        self.railway = data["owl:sameAs"][22:]
        self.information = data["odpt:trainInformationText"]["ja"]
        self.operator = data["odpt:operator"][14:]
        self.save()

    