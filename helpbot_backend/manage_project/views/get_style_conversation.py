from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation
from ..serializers import ProjectSerializers


class StyleConversation(APIView):
    def get(self, request, id, *args, **kwargs):
        project = Conversation.objects.get(idx=id).project
        serializer = ProjectSerializers(project)
        return Response(serializer.data)
