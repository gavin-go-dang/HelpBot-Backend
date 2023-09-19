from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Room
from ..serializers import RoomSerializers


class RoomListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)