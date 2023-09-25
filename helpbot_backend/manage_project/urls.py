from django.urls import include, path
from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import ProjectAPI, RoomAPI

app_name = "manage_project"
urlpatterns = []

router = DefaultRouter()
router.register("room", RoomAPI, basename="room")
router.register("project", ProjectAPI, basename="project")

urlpatterns += [
    path("v1/", include(router.urls)),
]
