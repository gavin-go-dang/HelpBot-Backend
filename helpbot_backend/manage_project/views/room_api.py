from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Room
from ..serializers import RoomSerializers


class RoomAPI(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
