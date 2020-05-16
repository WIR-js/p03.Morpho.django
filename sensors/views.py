from django.http import HttpResponse, JsonResponse
from .models import Sensor_device
#from django.core import serializers

def index(request):
    data =list(Sensor_device.objects.all().values())
    return JsonResponse({'sesnors':data})

def detail(request, id):
    data =list(Sensor_device.objects.filter(sensor_id = id).values())
    return JsonResponse({'sesnor':data})
