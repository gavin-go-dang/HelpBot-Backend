from rest_framework import permissions, viewsets

from ..models import Project
from ..serializers import ProjectSerializers


class ProjectAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()
