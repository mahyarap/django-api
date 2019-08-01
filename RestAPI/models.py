# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Weather(models.Model):
    date = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    temperature = models.ForeignKey('Temperature', on_delete=models.CASCADE)


class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)


class Temperature(models.Model):
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
