from rest_framework import serializers
from .models import Weather, Location


class WeatherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Weather
        fields = ['date', 'location', 'temperature']
        
    def validate_id(self, value):
        raise
        if not isinstance(int, value):
            raise serializers.ValidationError('Enter a whole number.')
     

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'lat', 'lon', 'city', 'state']
        
        
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'location', 'value', 'created_at']
