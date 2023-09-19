from django.urls import path
from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import ProjectListApiView, RoomListApiView, RoomPostApiView

app_name = "manage_project"
urlpatterns = [
    path("api/project/list", ProjectListApiView.as_view(), name="list_project"),
    path("api/room/list", RoomListApiView.as_view(), name="list_project"),
]


router = DefaultRouter()
router.register("api/room/post", RoomPostApiView, basename="post")
urlpatterns += router.urls
