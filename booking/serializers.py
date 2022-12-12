from rest_framework import serializers

from .models import Ticket, Order


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Ticket
        fields = [
            'url',
            'user',
            'order',
            'session',
            'seat',
            'category',
            'count',
        ]

        read_only_fields = ['user', 'order']    

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Order
        fields = [
            'url',
            'user',
            'time',
            'total_price',
        ]
        read_only_fields = ['order']
