from django.contrib import admin

from .models.booking import Booking
from .models.notification import Notification
from .models.review import Review
from .models.trip import Trip, TripStop, TripHistory
from .models.user import User, Role

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Trip)
admin.site.register(TripStop)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(TripHistory)
