from rest_framework import serializers

from rides.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'trip', 'reviewer', 'reviewee', 'rating', 'comment', 'created_at']
