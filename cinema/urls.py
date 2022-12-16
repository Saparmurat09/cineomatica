from django.urls import path, include

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_nested import routers

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

router.register('movies', MovieView, basename='movie')

movies_router = routers.NestedSimpleRouter(router, 'movies', lookup='movie')
movies_router.register('sessions', SessionView, basename='movies-sessions')

router.register('cinemas', CinemaView, basename='cinema')
router.register('contacts', ContactView, basename='contact')
router.register('addresses', AddressView, basename='address')

router.register('sessions', SessionView, basename='session')
sessions_router = routers.NestedSimpleRouter(
    router, 'sessions', lookup='session')
sessions_router.register('pricing', PricingView, basename='session-pricing')

cinemas_router = routers.NestedSimpleRouter(router, 'cinemas', lookup='cinema')
cinemas_router.register('rooms', RoomView, basename='cinemas-rooms')
cinemas_router.register('contact', ContactView, basename='cinemas-contact')
cinemas_router.register('address', AddressView, basename='cinemas-address')
cinemas_router.register('feedbacks', FeedbackView, basename='cinema-feedbacks')

router.register('rooms', RoomView, basename='room')
room_router = routers.NestedSimpleRouter(router, 'rooms', lookup='room')
room_router.register('sessions', SessionView, basename='rooms-sessions')

router.register('pricings', PricingView, basename='pricing')
router.register('feedbacks', FeedbackView, basename='feedback')


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('movie-list', request=request, format=format),
        'cinemas': reverse('cinema-list', request=request, format=format),
        'rooms': reverse('room-list', request=request, format=format),
        'sessions': reverse('session-list', request=request, format=format),
        'feedbacks': reverse('feedback-list', request=request, format=format),
        'pricings': reverse('pricing-list', request=request, format=format),
        'addresses': reverse('address-list', request=request, format=format),
        'contacts': reverse('contact-list', request=request, format=format),
        'tickets': reverse('ticket-list', request=request, format=format),
        'payment': reverse('payment', request=request, format=format),
        'purchases': reverse('purchases-list', request=request, format=format),
    })


urlpatterns = [
    path('', api_root, name='root'),
    path('', include(router.urls)),
    path('', include(movies_router.urls)),
    path('', include(cinemas_router.urls)),
    path('', include(sessions_router.urls)),
    path(
        'seat/',
        CreateSeatView.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='seat'
    ),
]
