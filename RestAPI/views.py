# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, views, status

from . import serializers, models


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = models.Weather.objects.all().order_by('id')
        if 'lat' in self.request.query_params:
            queryset = queryset.filter(location__lat=self.request.query_params['lat'])
        if 'lon' in self.request.query_params:
            queryset = queryset.filter(location__lon=self.request.query_params['lon'])
        return queryset

    def list(self, request, *args, **kwargs):
        resp = super().list(request, *args, **kwargs)
        if not resp.data and self.request.query_params:
            resp.status_code = status.HTTP_404_NOT_FOUND
        return resp

    @list_route()
    def temperature(self, request):
        queryset = models.Weather.objects.all().order_by('-date')
        if 'start' in self.request.query_params:
            queryset = queryset.filter(date__gte=self.request.query_params['start'])
        if 'end' in self.request.query_params:
            queryset = queryset.filter(date__lte=self.request.query_params['end'])
        result = []
        for weather in queryset:
            result.append({
                'state': weather.location.state,
                'city': weather.location.city,
                'lowest': min(json.loads(weather.temperature)),
                'highest': max(json.loads(weather.temperature)),
            })
        return Response(result)


class EraseAPIView(views.APIView):
    def delete(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                weather = models.Weather.objects.get(pk=pk)
                weather.delete()
                return Response(status=status.HTTP_200_OK)
            except models.Weather.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = models.Weather.objects.all()
        if 'start' in self.request.query_params:
            queryset = queryset.filter(date__gte=self.request.query_params['start'])
        if 'end' in self.request.query_params:
            queryset = queryset.filter(date__lte=self.request.query_params['end'])
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
