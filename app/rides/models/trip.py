from django.db import models
from .user import User


class Trip(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    driver = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    available_seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')


class TripStop(models.Model):
    trip = models.ForeignKey(Trip, related_name='stops', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    arrival_time = models.DateTimeField()


class TripHistory(models.Model):
    trip = models.ForeignKey(Trip, related_name='history', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='trip_history', on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
