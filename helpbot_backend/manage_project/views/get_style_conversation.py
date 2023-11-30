from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation


class StyleConversation(APIView):
    def get(self, request, id, *args, **kwargs):
        # breakpoint()
        style = Conversation.objects.get(idx=id).project.style_widget
        return Response(style)
