from django.urls import path, include
from rest_framework import routers

from .views import (
    MovieView,
    CinemaView,
    RoomView,
    ContactView,
    AddressView,
    CreateSeatView,
    SessionView,
    PricingView,
    FeedbackView,
)

router = routers.SimpleRouter()

router.register('movie', MovieView)
router.register('cinema', CinemaView)
router.register('room', RoomView)
router.register('contact', ContactView)
router.register('address', AddressView)
router.register('session', SessionView)
router.register('pricing', PricingView)
router.register('feedback', FeedbackView)


urlpatterns = [
    path('', include(router.urls)),
    path('seat/', CreateSeatView.as_view({'get': 'list', 'post': 'create'}), name='seat'),
]
