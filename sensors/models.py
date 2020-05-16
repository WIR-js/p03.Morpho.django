from django.db import models
from main.models import Home
from datetime import datetime


class Sensor_device(models.Model):
    home_id = models.ForeignKey(Home, on_delete=models.CASCADE, default=0)
    sensor_id = models.IntegerField(db_column='sensor_id' , primary_key=True)
    Sensor_name = models.CharField(db_column='sensor_name' , max_length=200)
#    measure_date = models.DateTimeField(db_column='measure_date')
    position = models.CharField(db_column='position' , max_length=200)
    is_active = models.BooleanField(db_column='is_active', default= True)
    gpio = models.IntegerField(db_column='gpio')

class Sensor_vlaue(models.Model):
     sensor_id = models.ForeignKey(Sensor_device, on_delete=models.CASCADE)
     value =  models.IntegerField(db_column='value')
     measure_date = models.DateTimeField(db_column='measure_date', default=datetime.now)
