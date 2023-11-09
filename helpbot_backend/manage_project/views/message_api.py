from rest_framework import viewsets

from ..models import Message
from ..serializers import AnswerSerializers


class MessageAPI(viewsets.ModelViewSet):
    serializer_class = AnswerSerializers
    queryset = Message.objects.all()
