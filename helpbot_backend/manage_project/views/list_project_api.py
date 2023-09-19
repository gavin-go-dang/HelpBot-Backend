from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Project
from ..serializers import ProjectSerializers


class ProjectListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
