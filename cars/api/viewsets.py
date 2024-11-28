from rest_framework import viewsets
from cars.api import serializers
from cars import models

class CarViewset(viewsets.ModelViewSet):

    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()
