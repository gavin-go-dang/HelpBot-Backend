from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import ProjectAPI, RoomAPI

app_name = "manage_project"
urlpatterns = []

router = DefaultRouter()
router.register("api/room", RoomAPI, basename="room")
router.register("api/project", ProjectAPI, basename="project")
urlpatterns += router.urls
