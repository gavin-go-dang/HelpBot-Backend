from django.urls import include, path
from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import AnswerAPI, ProjectAPI, QuestionAPI, RoomAPI

app_name = "manage_project"
urlpatterns = []

router = DefaultRouter()
router.register("room", RoomAPI, basename="room")
router.register("project", ProjectAPI, basename="project")
router.register("answer", AnswerAPI, basename="answer")
router.register("question", QuestionAPI, basename="question")

urlpatterns += [
    path("", include(router.urls)),
]
