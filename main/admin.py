from django.contrib import admin
from .models import User, Device, Sensor, UserDevice

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(UserDevice)
