from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import User, ClubCard
from .serializers import UserSerializer, ClubCardSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class ClubCardView(generics.ListAPIView):

    def get(self, request):
        clubcard = ClubCard.objects.get(user=request.user)
        serializer = ClubCardSerializer(instance=clubcard)

        return Response(serializer.data, status=status.HTTP_200_OK)
