from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from helpbot_backend.users.views import CreateUser

app_name = "users"
urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


router = DefaultRouter()
router.register("create", CreateUser, basename="room")
urlpatterns += router.urls
