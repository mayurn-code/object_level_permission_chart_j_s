from django.db import models
import datetime

class Tag_C8738A28CFF7(models.Model):
    date_time = models.DateTimeField()
    assets = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    temperature = models.FloatField(max_length=100)
    humidity = models.FloatField(max_length=100)
    # d = datetime(date_time)

    class Meta:
        db_table = "thingsally"

    