from rest_framework import viewsets

from ..models import Room
from ..serializers import RoomSerializers


class RoomAPI(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
