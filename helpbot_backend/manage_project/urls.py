from django.urls import include, path
from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import (
    AnswerAPI,
    MessageAPI,
    MessageReceivedPerMonthAPI,
    MessageReceivedPerWeekAPI,
    ProjectAPI,
    QuestionAPI,
    RoomAPI,
)

app_name = "manage_project"
urlpatterns = [
    path("message-count/", MessageReceivedPerWeekAPI.as_view(), name="record_count_api"),
    path("message-count-per-month/", MessageReceivedPerMonthAPI.as_view(), name="record_count_per_month_api"),
]

router = DefaultRouter()
router.register("room", RoomAPI, basename="room")
router.register("project", ProjectAPI, basename="project")
router.register("answer", AnswerAPI, basename="answer")
router.register("question", QuestionAPI, basename="question")
router.register("message", MessageAPI, basename="message")

urlpatterns += [
    path("", include(router.urls)),
]
