# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets


class WeatherView(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]