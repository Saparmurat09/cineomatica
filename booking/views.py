from rest_framework import viewsets

from .models import Ticket, Order

from .serializers import TicketSerializer, OrderSerializer

class TicketView(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user

        return Ticket.objects.filter(user=user)

    def perform_create(self, serializer):
        order = Order.objects.create(user=self.request.user)
        serializer.save(user=self.request.user, order=order)



class OrderView(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        return Order.objects.filter(user=user)
