from django.http import HttpResponse, JsonResponse
from sensors.models import Sensor_device, Sensor_vlaue
#from django.core import serializers

def values(request):
    data = list(Sensor_vlaue.objects.filter(sensor_id=1).values())
    return JsonResponse({'home_temprature':data})

def detail(request, id):
    data =list(Sensor_device.objects.filter(sensor_id = id).values())
    return JsonResponse({'sesnor':data})
#    data = serializers.serialize('json',Sensor_devcice.objects.filter(sensor_id = id))
#    return HttpResponse(data, content_type='application/json')
