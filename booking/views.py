from rest_framework import viewsets

from .models import Ticket, Order

from .serializers import TicketSerializer, OrderSerializer

class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_admin:
            return Ticket.objects.filter(user=user)
        return Ticket.objects.all()

    def perform_create(self, serializer):
        order = Order.objects.create(user=self.request.user)
        serializer.save(user=self.request.user, order=order)



class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_admin:
            return Order.objects.filter(user=user)
        return Order.objects.all()
