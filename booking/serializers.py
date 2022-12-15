from rest_framework import serializers

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
