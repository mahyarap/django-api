# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Weather(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    temperature = models.TextField()


class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
