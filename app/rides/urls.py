from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, BookingViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

