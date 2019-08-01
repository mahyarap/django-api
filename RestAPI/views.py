# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from . import serializers, models


class WeatherView(viewsets.ModelViewSet):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeahterSerializer
    