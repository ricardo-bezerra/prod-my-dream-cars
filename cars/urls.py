from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cars.api import viewsets as carviewsets

route = routers.DefaultRouter()

route.register(r'car', carviewsets.CarViewset, basename='Car')


urlpatterns = [
    path('vehicles/', include(route.urls)),
]
