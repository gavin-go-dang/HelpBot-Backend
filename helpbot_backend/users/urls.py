from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from helpbot_backend.users.views import ClerkCreateUser, CreateUser

app_name = "users"
urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/clerk-create/", ClerkCreateUser.as_view(), name="clerk-create"),
]


router = DefaultRouter()
router.register("create", CreateUser, basename="create")
# router.register("clerk-create", ClerkCreateUser, basename="clerk_create")
urlpatterns += router.urls
