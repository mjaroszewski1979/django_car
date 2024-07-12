# Import models module from django.db package for creating database models
from django.db import models
# Import AbstractUser class from django.contrib.auth.models for custom user models
from django.contrib.auth.models import AbstractUser
# Import Lower function from django.db.models.functions for case-insensitive operations
from django.db.models.functions import Lower


class User(AbstractUser):
    """
    Custom user model extending the AbstractUser class.
    Currently, no additional fields or methods are added.
    """
    pass

class Car(models.Model):
    """
    Model representing a car with various attributes such as producer,
    country of origin, year of production, users, and photo.
    """
    
    producer = models.CharField(max_length=128, unique=True)
    country_of_origin = models.CharField(max_length=128, blank=True, null=True)
    year_of_production = models.PositiveIntegerField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='cars', through='UserCars')
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)

    class Meta:
        """
        Meta class to specify model-level options.
        """
        
        ordering = [Lower('producer')]

class UserCars(models.Model):
    """
    Model representing the relationship between User and Car with an additional
    order attribute.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        """
        Meta class to specify model-level options.
        """
        
        ordering = ['order']

