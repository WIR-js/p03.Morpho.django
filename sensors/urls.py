from django.urls import path
from .APIs import DHT_api
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('temp/', DHT_api.values, name='DHT_value'),
]