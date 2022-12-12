from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TicketView, OrderView

router = SimpleRouter()

router.register('ticket', TicketView, basename='ticket')
router.register('order', OrderView, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
