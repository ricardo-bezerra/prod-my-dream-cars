from django.db import models


def upload_image_car(instance, filename):
   return f"{instance.car_id}, {filename}"

# Django can not serialize lambda functions
# upload_image_car = lambda instance, filename: f"{instance.id_car}, {filename}"

# x = lambda a, b : a * b
# print(x(5, 6))


class Car(models.Model):
 
    car_id = models.AutoField(primary_key=True, editable=False)
    brand = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    fuel = models.CharField(max_length=15)
    type = models.CharField(max_length=15) 
    release_year = models.DateField()
    state = models.CharField(max_length=15)
    color = models.CharField(max_length=25, null=True)
    quilometers = models.IntegerField()
    publishing_company = models.CharField(max_length=55)
    create_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to=upload_image_car, blank=True, null=True)
