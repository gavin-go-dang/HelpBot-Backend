from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Project
from ..serializers import ProjectSerializers


class ProjectAPI(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()
