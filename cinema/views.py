from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import (
   Movie,
   Cinema,
   Room,
   Feedback,
   Address,
   Contact, 
   Seat,
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
)

class MovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaView(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressView(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CreateSeatView(ModelViewSet):
    queryset = Seat.objects.all()

    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        seats = serializer.validated_data['seats'] 

        room = Room.objects.get(id=room)

        # TODO check for repeating seat row, columns

        for i in range(len(seats)):
            row = i + 1
            for j in range(seats[i]):
                column = j + 1
                seat = Seat.objects.create(room=room, column=column, row=row)
                seat.save()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SeatSerializer
        return CreateSeatSerializer