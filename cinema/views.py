from rest_framework.viewsets import ModelViewSet
from .models import (
   Movie,
   Cinema,
   Room,
   Feedback,
   Address,
   Contact, 
)

from .serializers import (
    MovieSerializer,
    CinemaSerializer,
    RoomSerializer,
    FeedbackSerializer,
    AddressSerializer,
    ContactSerializer,
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
    serializer_class = AddressSerializer()
