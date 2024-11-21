from rest_framework import serializers

from rides.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'driver', 'origin', 'destination', 'departure_time', 'arrival_time', 'available_seats', 'price', 'description', 'status']