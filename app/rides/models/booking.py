from django.db import models

from .trip import Trip
from .user import User

class Booking(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    trip = models.ForeignKey(Trip, related_name='bookings', on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    seats_reserved = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
