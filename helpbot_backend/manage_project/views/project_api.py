from rest_framework import viewsets

from ..models import Project
from ..serializers import ProjectSerializers


class ProjectAPI(viewsets.ModelViewSet):
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()
