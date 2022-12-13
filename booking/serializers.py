from rest_framework import serializers, validators

from .models import Ticket, Order, BookTicket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Ticket
        fields = [
            'url',
            'user',
            'order',
            'session',
            'seat',
            'category',
        ]

        read_only_fields = ['user', 'order']   

class Seats(serializers.Serializer):
    row = serializers.IntegerField(required=True)
    column = serializers.IntegerField(required=True)
    category = serializers.IntegerField(required=True)


class CreateTicketSerializer(serializers.Serializer):
    session = serializers.IntegerField(required=True)
    seats = Seats(many=True)


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
