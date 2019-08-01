from rest_framework import serializers
from .models import Weather, Location


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'date', 'location', 'temperature']
     

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'lat', 'lon', 'city', 'state']
        
        
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'location', 'value', 'created_at']
