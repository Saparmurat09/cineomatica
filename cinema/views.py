from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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
)

from .serializers import (
    MovieSerializer,
    CinemaSerializer,
    RoomSerializer,
    FeedbackSerializer,
    AddressSerializer,
    ContactSerializer,
    CreateSeatSerializer,
    SeatSerializer,
    SessionSerializer,
    PricingSerializer,
)

class MovieView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ContactView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


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

    serializer_class = SessionSerializer

    def get_queryset(self):
        if 'movie_pk' in self.kwargs:
            return Session.objects.filter(movie=self.kwargs['movie_pk'])
        return Session.objects.all()


class PricingView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class FeedbackView(viewsets.ModelViewSet):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        if 'movie_pk' in self.kwargs:
            return Feedback.objects.filter(movie=self.kwargs['movie_pk'])

        return Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if not self.request.method in SAFE_METHODS:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

