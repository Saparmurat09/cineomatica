from rest_framework import serializers
from .models import (
    Movie,
    Cinema,
    Feedback,
    Room,
    Contact,
    Address,
    Seat,
)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'poster',
            'duration',
            'year',
            'director',
            'genre',
            'language',
            'country',
            'status',
            'age_rating',
        ]


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'name',
            'description',
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'cinema',
            'phone',
            'email',

        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'cinema',
            'city',
            'district',
            'street',
            'number',
        ]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'cinema',
            'name',
            'description',
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'cinema',
            'content',
            'rating',
        ]


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = [
            'room',
            'row',
            'column',
        ]


class CreateSeatSerializer(serializers.Serializer):
    room = serializers.IntegerField(min_value=1)
    seats = serializers.ListField(child=serializers.IntegerField(min_value=1))
