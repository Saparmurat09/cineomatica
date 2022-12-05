from rest_framework import serializers
from .models import Movie, Cinema, Feedback, Room


class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        field = [
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
        field = [
            'name',
            'description',            
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        field = [
            'cinema',
            'phone',
            'email',

        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        field = [
            'cinema',
            'city',
            'district',
            'street',
            'number',
        ]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        field = [
            'cinema',
            'name',
            'description',  
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        field = [
            'cinema',
            'content',
            'rating',
        ]