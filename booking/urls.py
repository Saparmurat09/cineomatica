from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TicketView, OrderView

router = SimpleRouter()

router.register('tickets', TicketView, basename='ticket')
router.register('orders', OrderView, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
