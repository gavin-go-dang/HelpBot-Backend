
from rest_framework import viewsets

from ..models import Answer
from ..serializers import AnswerSerializers


class AnswerAPI(viewsets.ModelViewSet):
    serializer_class =AnswerSerializers
    queryset = Answer.objects.all()
