from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly

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
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ContactView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
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
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class PricingView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
