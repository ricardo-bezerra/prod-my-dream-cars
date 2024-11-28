from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cars.api import viewsets as carviewsets
from django.conf.urls.static import static
from django.conf import settings


route = routers.DefaultRouter()

route.register(r'car', carviewsets.CarViewset, basename='Car')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include(route.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
