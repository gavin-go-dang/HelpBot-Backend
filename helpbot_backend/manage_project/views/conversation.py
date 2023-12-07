from rest_framework import viewsets

from ..models import Conversation
from ..serializers import ConversationSerializers


class ConversationAPI(viewsets.ModelViewSet):
    serializer_class = ConversationSerializers
    queryset = Conversation.objects.all()
