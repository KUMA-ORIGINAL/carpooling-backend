from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    photo = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
