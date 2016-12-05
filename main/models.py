""" Models for our main app """

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.postgres.fields import ArrayField

#Data representation of a user
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    """ Cyqlo user model """

#Data representation of a route
class Route(models.Model):
    """ Route model """
    route_name = models.CharField(max_length=50, null=False, blank=False)
    # uses postgres interval format '# day hr:min:sec', for ex, 1 day is '1 day 00:00:00'
    duration = models.DurationField(null=False, blank=False)
    # [lat,lng]
    origin = ArrayField(models.FloatField(null=False, blank=False), size=2)
    # [lat,lng]
    destination = ArrayField(models.FloatField(null=False, blank=False), size=2)
    # [location1, location2, location3, ...]
    waypoints = ArrayField(models.CharField(max_length=256, null=False, blank=True))
    # route image
    image = models.CharField(max_length=50, null=True, blank=False)
    # template name
    template = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        #Route objects are represented by name
        return self.route_name
