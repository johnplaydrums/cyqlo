""" Models for our main app """

from django.db import models
from django.contrib.postgres.fields import ArrayField

#Data representation of a route
class Route(models.Model):
    """ Route model """
    route_name = models.CharField(max_length=50, null=False, blank=False)
    # duration of bike trip, in minutes
    duration = models.IntegerField(null=True, blank=False)
    # distance of bike trip
    distance = models.FloatField(null=True, blank=False)
    # difficult = {'beg', 'med', 'adv'}
    difficulty = models.CharField(max_length=3, null=True, blank=True)
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
