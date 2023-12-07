from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Message
from ..serializers import MessageSerializers


class MessageConversation(APIView):
    def get(self, request, id, *args, **kwargs):
        messages = Message.objects.filter(conversation=id).order_by("id")
        serializer = MessageSerializers(messages, many=True)
        return Response(serializer.data)
