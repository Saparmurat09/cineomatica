from rest_framework import viewsets, status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import Ticket, Order

from .serializers import TicketSerializer, OrderSerializer, CreateTicketSerializer

class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_admin:
            return Ticket.objects.filter(user=user)
        return Ticket.objects.all()

    def create(self, request):
        user = request.user
        data = request.data
    
        # if not 'seats' in data or not 'session' in data:
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)
            # raise ValidationError('data')
        
        # order = Order.objects.create(user=user)
        # print(user)
        # print(data['seats'])

        return Response(data, status=status.HTTP_201_CREATED)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTicketSerializer
        
        return TicketSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_admin:
            return Order.objects.filter(user=user)
        return Order.objects.all()
