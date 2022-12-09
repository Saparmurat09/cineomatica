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


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'url',
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


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'url',
            'name',
            'description',
        ]


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'url',
            'cinema',
            'phone',
            'email',
        ]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'url',
            'cinema',
            'city',
            'district',
            'street',
            'number',
        ]


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = [
            'url',
            'cinema',
            'name',
            'description',
        ]


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'url',
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
