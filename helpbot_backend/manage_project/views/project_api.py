from rest_framework import status, viewsets
from rest_framework.response import Response

from ..models import Project
from ..serializers import ProjectSerializers
from .convert import convert_flow_chart


class ProjectAPI(viewsets.ModelViewSet):
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()

    def update(self, request, *args, **kwargs):
        script = {}
        if "flow_chart" in request.data and request.data["flow_chart"]:
            script = convert_flow_chart(request.data["flow_chart"])
            request.data["script_QA"] = script
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
