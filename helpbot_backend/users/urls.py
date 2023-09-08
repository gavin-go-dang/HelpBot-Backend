from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from helpbot_backend.users.views import CreateUserAPIView  # user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
    path("create/", CreateUserAPIView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
