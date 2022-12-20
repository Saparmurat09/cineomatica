from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import (
    Movie,
    Cinema,
    Room,
    Feedback,
    Address,
    Contact,
    Seat,
    Session,
    Pricing,
    ScheduleDay,
)

from .serializers import (
    ListMovieSerializer,
    ListCinemaSerializer,
    ListRoomSerializer,
    ListFeedbackSerializer,
    ListAddressSerializer,
    ListContactSerializer,
    ListSessionSerializer,
    ListPricingSerializer,
    CreateMovieSerializer,
    CreateCinemaSerializer,
    CreateRoomSerializer,
    CreateFeedbackSerializer,
    CreateAddressSerializer,
    CreateContactSerializer,
    CreateSeatSerializer,
    CreateSessionSerializer,
    CreatePricingSerializer,
    SeatSerializer,
    ScheduleSerializer,
)


class MovieView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    class Meta:
        ordering = [
            '-year',
        ]

    def get_queryset(self):
        return Movie.objects.filter(status=1)

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateMovieSerializer
        return ListMovieSerializer

    @action(detail=False)
    def hidden(self, request):
        hidden_movies = Movie.objects.filter(status=3)

        page = self.paginate_queryset(hidden_movies)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hidden_movies, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def upcoming(self, request):
        hidden_movies = Movie.objects.filter(status=2)

        page = self.paginate_queryset(hidden_movies)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hidden_movies, many=True)
        return Response(serializer.data)


class CinemaView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Cinema.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateCinemaSerializer
        return ListCinemaSerializer


class RoomView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if 'cinema_pk' in self.kwargs:
            return Room.objects.filter(cinema=self.kwargs['cinema_pk'])
        return Room.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateRoomSerializer
        return ListRoomSerializer


class ContactView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Contact.objects.all()

    def get_queryset(self):
        if 'cinema_pk' in self.kwargs:
            return Contact.objects.filter(cinema=self.kwargs['cinema_pk'])
        return Contact.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateContactSerializer
        return ListContactSerializer


class AddressView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateAddressSerializer
        return ListAddressSerializer


class CreateSeatView(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        seats = serializer.validated_data['seats']

        room = Room.objects.get(id=room)

        data = Seat.objects.all().filter(room=room)
        data.delete()

        for i in range(len(seats)):
            row = i + 1
            for j in range(seats[i]):
                column = j + 1
                seat = Seat.objects.create(room=room, column=column, row=row)
                seat.save()

    def list(self, request):
        queryset = Seat.objects.all()
        serializer = SeatSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return Seat.objects.all()

    def get_serializer_class(self):
        return CreateSeatSerializer


class SessionView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    class Meta:
        ordering = ['date']

    def get_queryset(self):
        if 'movie_pk' in self.kwargs:
            return Session.objects.filter(movie=self.kwargs['movie_pk'])

        if 'room_pk' in self.kwargs:
            return Session.objects.filter(movie=self.kwargs['room_pk'])

        return Session.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateSessionSerializer
        return ListSessionSerializer


class PricingView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if 'session_pk' in self.kwargs:
            return Pricing.objects.filter(session=self.kwargs['session_pk'])
        return Pricing.objects.all()

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreatePricingSerializer
        return ListPricingSerializer


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()

    def get_queryset(self):
        if 'movie_pk' in self.kwargs:
            return Feedback.objects.filter(movie=self.kwargs['movie_pk'])

        return Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.method not in SAFE_METHODS:
            return CreateFeedbackSerializer
        return ListFeedbackSerializer


class ScheduleView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ScheduleSerializer
    allowed_methods = ['PUT', 'GET', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']

    def get_queryset(self):
        if 'cinema_pk' in self.kwargs:
            return ScheduleDay.objects.filter(cinema=self.kwargs['cinema_pk'])

        return ScheduleDay.objects.all()
