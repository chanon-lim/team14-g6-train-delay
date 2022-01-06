from django.db import models
from .translator import translate
# Create your models here.

class TrainInfo(models.Model):
    train_id = models.CharField(max_length=200)
    railway_en = models.CharField(max_length=200, default="undefined")
    railway_ja = models.CharField(max_length=200, default="undefined")
    operator_en = models.CharField(max_length=200, default="undefined")
    operator_ja = models.CharField(max_length=200, default="undefined")
    information_ja = models.CharField(max_length=2000)
    information_en = models.CharField(max_length=2000)

    def update_train(self, data, side_data):
        self.train_id = data["@id"]
        self.railway_en = side_data["railway_en"]
        self.railway_ja = side_data["railway_ja"]
        self.operator_en = side_data["operator_en"]
        self.operator_ja = side_data["operator_ja"]
        info = data["odpt:trainInformationText"]["ja"]
        if ('平常' in info) or (info == '現在、１５分以上の遅延はありません。'):
            info = "平常運転"
        self.information_ja = info
        self.information_en = translate(info)
        self.save()

class LocalStorage(models.Model):
    last_update = models.DateTimeField(auto_now_add=True)