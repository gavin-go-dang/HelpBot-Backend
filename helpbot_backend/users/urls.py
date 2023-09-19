from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from helpbot_backend.users.views import CreateUserAPIView

app_name = "users"
urlpatterns = [
    path("create/", CreateUserAPIView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
