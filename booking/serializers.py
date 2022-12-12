from rest_framework import serializers

from .models import Ticket, Order

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'user',
            'order',
            'session',
            'seat',
            'category',
            'count',
        ]

        read_only_fields = ['id', 'user', 'order']
    
    # def create(self, validated_data):

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'time',
            'total_price',
        ]
        read_only_fields = ['id', 'user', 'order']
