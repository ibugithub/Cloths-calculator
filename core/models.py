from django.db import models
from datetime import datetime
# Create your models here.

class ClothInfo(models.Model):
    GozLength = models.FloatField(null=True)
    GiraLength = models.FloatField(null=True)
    Rate = models.FloatField()

EventTypeChoise = (
    ("devit", "ডেবিট"),
    ("credit", "ক্রেডিট")
)


class ShopEvent(models.Model):
    তারিখ = models.DateTimeField(auto_now_add=True
    )
    পোশাক = models.CharField(max_length=500)
    রেট = models.FloatField(null=True)
    পরিমান = models.CharField(max_length=200, null=True)
    টাকা = models.FloatField()
    ধরন = models.CharField(max_length=40, choices= EventTypeChoise)
    