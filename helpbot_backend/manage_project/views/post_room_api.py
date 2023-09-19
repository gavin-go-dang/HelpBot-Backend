from rest_framework import permissions, viewsets

from ..serializers import RoomSerializers


class RoomPostApiView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomSerializers
