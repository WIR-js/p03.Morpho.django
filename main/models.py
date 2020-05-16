from django.db import models
from datetime import datetime


class Home(models.Model):
    home_id = models.IntegerField(db_column='home_id' , primary_key=True)
    home_name = models.CharField(db_column='home_name' , max_length=200)
    home_location = models.CharField(db_column='location' , max_length=500)
    is_active = models.BooleanField(db_column='is_active', default= True)

class Resident(models.Model):
    
    ADMIN= 'Admin'
    MEMBER = 'Member'
    GUST = 'Gust'
    
    RESIDENT_ROLE = (
        (ADMIN, 'Admin'),
        (MEMBER, 'Member'),
        (GUST, 'Gust'))

    residnet_id = models.AutoField(db_column='resident_id',primary_key=True , editable=False )
    home_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    resident_name = models.CharField(db_column='resident_name' , max_length=100)
    resident_role = models.CharField(db_column="resident_role", choices=RESIDENT_ROLE ,max_length=10)
    resident_registered = models.DateTimeField(db_column='resident_registered', default=datetime.now)

    def str(self):
        return self.resident_name