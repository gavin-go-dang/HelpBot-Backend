from django.urls import include, path
from rest_framework.routers import DefaultRouter

from helpbot_backend.manage_project.views import (
    AnswerAPI,
    CombinedInfoAPIView,
    ConversationAPI,
    GetRoomChat,
    MessageAPI,
    MessageConversation,
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
    path("conversations/<int:id>/", CombinedInfoAPIView.as_view(), name="conversation"),
    path("message-conversation/<int:id>/", MessageConversation.as_view(), name="message-conversation"),
    path("get-room-chat/<int:id>/", GetRoomChat.as_view(), name="get-room"),
]

router = DefaultRouter()
router.register("room", RoomAPI, basename="room")
router.register("project", ProjectAPI, basename="project")
router.register("answer", AnswerAPI, basename="answer")
router.register("question", QuestionAPI, basename="question")
router.register("message", MessageAPI, basename="message")
router.register("conversation", ConversationAPI, basename="message")

urlpatterns += [
    path("", include(router.urls)),
]
