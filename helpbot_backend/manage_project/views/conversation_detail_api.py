# views.py
from django.db.models import Min
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Message, Room


class CombinedInfoAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        rooms = Room.objects.filter(project__id=id).values("id_synapse")
        data = (
            Message.objects.exclude(conversation="")
            .filter(room__in=rooms)
            .values("conversation")
            .distinct()
            .annotate(earliest_time=Min("created_at"))
        )
        return Response(data)
