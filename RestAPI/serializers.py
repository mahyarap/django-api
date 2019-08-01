import json

from django.db import IntegrityError, transaction
from rest_framework import serializers

from .models import Weather, Location


class LocationSerializer(serializers.ModelSerializer):
    lat = serializers.FloatField(error_messages={'invalid': 'Enter a number.'})
    lon = serializers.FloatField(error_messages={'invalid': 'Enter a number.'})

    class Meta:
        model = Location
        fields = ['lat', 'lon', 'city', 'state']
        

class WeatherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(error_messages={'invalid': 'Enter a whole number.'})
    date = serializers.DateField(error_messages={'invalid': 'Enter a valid date/time.'})
    location = LocationSerializer()
    temperature = serializers.ListField(child=serializers.FloatField())

    class Meta:
        model = Weather
        fields = ['id', 'date', 'location', 'temperature']

    def to_internal_value(self, data):
        location = LocationSerializer(data=data['location'])
        location.is_valid()
        errors = location.errors
        try:
            retval = super().to_internal_value(data)
        except serializers.ValidationError as exc:
            exc.detail.update(errors)
            raise
        return retval

    def to_representation(self, obj):
        if isinstance(obj.temperature, str):
            obj.temperature = json.loads(obj.temperature)
        return super().to_representation(obj)

    @transaction.atomic
    def create(self, validated_data):
        location = validated_data.pop('location')
        location, _ = Location.objects.get_or_create(**location)
        try:
            weather = Weather.objects.create(**validated_data, location=location)
        except IntegrityError:
            raise serializers.ValidationError({'id': ['Weather with this Id already exists.']})
        return weather
