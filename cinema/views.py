from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response

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
    
class SessionView(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class PricingView(ModelViewSet):
    permission_classes = []
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer