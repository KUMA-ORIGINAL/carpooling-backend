from rest_framework import serializers

from rides.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'trip', 'passenger', 'seats_reserved', 'total_price', 'status']