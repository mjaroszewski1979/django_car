from django.db import models
from django.db.models.functions import Lower

class Car(models.Model):
    producer = models.CharField(max_length=128)
    country_of_origin = models.CharField(max_length=128)
    year_of_production = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)

    class Meta:
        ordering = [Lower('producer')]

