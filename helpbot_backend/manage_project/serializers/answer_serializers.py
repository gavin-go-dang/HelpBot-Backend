from rest_framework import serializers

from ..models import Answer


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
