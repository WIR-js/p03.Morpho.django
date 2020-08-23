from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    fistname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=datetime.now)
    activation = models.BooleanField(default=False)
    def __str__(self):
        return f'username: {self.username}\n' \
               f'firstname: {self.fistname}\n' \
               f'lastname: {self.lastname}\n' \
               f'email: {self.email}\n' \
               f'created at: {self.created_at}\n' \
               f'activation; {self.activation}'

class Device(models.Model):
    SENSOR = 'S'
    CONTROLLER = 'C'
    ACTUATOR = 'AC'
    APPLIANCE = 'AP'

    Types = [
        (SENSOR, 'sensor'),
        (CONTROLLER,'controller'),
        (ACTUATOR, 'actuator'),
        (APPLIANCE, 'appliance')
    ]
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    position = models.IntegerField()
    status = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=Types)
    def is_upperclass(self):
        return self.Types in {
            self.Types.SENSOR,
            self.Types.CONTROLLER,
            self.Types.ACTUATOR,
            self.Types.APPLIANCE,
        }


class Sensor(models.Model):
    data_type = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=datetime.now)


class UserDevice(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    device_id = models.ForeignKey('Device', on_delete=models.CASCADE)

