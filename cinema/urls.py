from django.urls import path, include
from rest_framework import routers

from .views import (
    MovieView,
    CinemaView,
    RoomView,
    ContactView,
    AddressView,
    CreateSeatView,
)

router = routers.SimpleRouter()

router.register('movie', MovieView)
router.register('cinema', CinemaView)
router.register('room', RoomView)
router.register('contact', ContactView)
router.register('address', AddressView)


urlpatterns = [
    path('', include(router.urls)),
    path('seat/', CreateSeatView.as_view({'get': 'list', 'post': 'create'}), name='seat'),
]
