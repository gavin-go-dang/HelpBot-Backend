from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from helpbot_backend.users.views import ClerkCreateUser, CreateUser

app_name = "users"
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("clerk-create/", ClerkCreateUser.as_view(), name="clerk-create"),
]


router = DefaultRouter()
router.register("v1/create", CreateUser, basename="create")
urlpatterns += router.urls
