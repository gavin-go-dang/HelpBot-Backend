from rest_framework import permissions, viewsets

from ..models import Room
from ..serializers import RoomSerializers


class RoomAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
