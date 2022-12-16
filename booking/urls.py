from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    TicketView,
    OrderView,
    PurchasesView,
    PayOrderView,
)

router = SimpleRouter()

router.register('tickets', TicketView, basename='ticket')
router.register('orders', OrderView, basename='order')
router.register('purchases', PurchasesView, basename='purchases')

urlpatterns = [
    path('', include(router.urls)),
    path('payment/', PayOrderView.as_view(), name='payment'),
]
