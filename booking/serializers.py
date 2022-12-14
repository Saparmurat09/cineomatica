from rest_framework import serializers

from .models import Ticket, Order, BookTicket


class ListTicketSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    row = serializers.ReadOnlyField(source='seat.row')
    column = serializers.ReadOnlyField(source='seat.column')
    room = serializers.ReadOnlyField(source='session.room.name')

    class Meta:
        model = Ticket
        fields = [
            'url',
            'order',
            'session',
            'room',
            'row',
            'column',
            'category',
            'user',
        ]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'order',
            'session',
            'seat',
            'category',
            'user',
        ]


class Seats(serializers.Serializer):
    row = serializers.IntegerField(required=True)
    column = serializers.IntegerField(required=True)
    category = serializers.IntegerField(required=True)


class BookTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTicket
        fields = [
            'row',
            'column',
            'category',
        ]


class CreateTicketSerializer(serializers.Serializer):
    session = serializers.IntegerField(required=True)
    seats = BookTicketSerializer(many=True)


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


class PayOrderSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    payment_method = serializers.CharField(max_length=16)

    def validate_payment_method(self, value):
        return len(value) == 16
