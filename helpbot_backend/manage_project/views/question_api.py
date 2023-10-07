

from rest_framework import viewsets

from ..models import Question
from ..serializers import QuestionSerializers


class QuestionAPI(viewsets.ModelViewSet):
    serializer_class =QuestionSerializers
    queryset = Question.objects.all()
