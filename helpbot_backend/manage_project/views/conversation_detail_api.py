from django.db.models import Min
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation, Message


class CombinedInfoAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        conversation = Conversation.objects.filter(project__id=id).values("idx")
        data = (
            Message.objects.exclude(conversation="")
            .filter(conversation__in=conversation)
            .values("conversation")
            .distinct()
            .annotate(earliest_time=Min("created_at"))
        )
        return Response(data)
