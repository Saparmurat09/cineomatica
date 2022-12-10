from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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

router.register('movie', MovieView, basename='movie')
router.register('cinema', CinemaView, basename='cinema')
router.register('room', RoomView, basename='room')
router.register('contact', ContactView, basename='contact')
router.register('address', AddressView, basename='address')
router.register('session', SessionView, basename='session')
router.register('pricing', PricingView, basename='pricing')
router.register('feedback', FeedbackView, basename='feedback')


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movie': reverse('movie-list', request=request, format=format),
        'cinema': reverse('cinema-list', request=request, format=format),
        'room': reverse('room-list', request=request, format=format),
        'session': reverse('session-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='root'),
    path('', include(router.urls)),
    path('seat/', CreateSeatView.as_view({'get': 'list', 'post': 'create'}), name='seat'),
]
