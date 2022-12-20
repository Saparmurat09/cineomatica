from rest_framework import serializers
from .models import (
    Movie,
    Cinema,
    Feedback,
    Room,
    Contact,
    Address,
    Seat,
    Session,
    Pricing,
    ScheduleDay,
)


class ListMovieSerializer(serializers.HyperlinkedModelSerializer):

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


class CreateMovieSerializer(serializers.ModelSerializer):

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


class ListCinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'url',
            'name',
            'description',
        ]


class CreateCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'name',
            'description',
        ]

    def create(self, validated_data):
        cinema = Cinema.objects.create(**validated_data)

        for i in range(1, 8):
            schedule = ScheduleDay.objects.create(cinema=cinema, day=i)
            schedule.save()

        return cinema


class ListContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'url',
            'cinema',
            'phone',
            'email',
        ]


class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'cinema',
            'phone',
            'email',
        ]


class ListAddressSerializer(serializers.HyperlinkedModelSerializer):
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


class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'cinema',
            'city',
            'district',
            'street',
            'number',
        ]


class ListRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = [
            'url',
            'cinema',
            'name',
            'description',
        ]


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'cinema',
            'name',
            'description',
        ]


class ListFeedbackSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Feedback
        fields = [
            'url',
            'cinema',
            'content',
            'rating',
            'user',
        ]
        read_only_fields = ['user']


class CreateFeedbackSerializer(serializers.ModelSerializer):
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
            'id',
            'room',
            'row',
            'column',
        ]

        read_only_fields = ['id']


class CreateSeatSerializer(serializers.Serializer):
    room = serializers.IntegerField(min_value=1)
    seats = serializers.ListField(child=serializers.IntegerField(min_value=1))


class ListPricingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pricing
        fields = [
            'url',
            'session',
            'children',
            'adult',
            'student',
        ]


class CreatePricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = [
            'session',
            'children',
            'adult',
            'student',
        ]


class ListSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = [
            'url',
            'movie',
            'room',
            'date',
            'start_time',
            'end_time',
        ]


class CreateSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'movie',
            'room',
            'date',
            'start_time',
            'end_time',
        ]


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ScheduleDay
        fields = [
            'url',
            'cinema',
            'day',
            'opening',
            'closing',
        ]
