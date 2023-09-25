from django.urls import include, path

urlpatterns = [
    path("users/", include("helpbot_backend.users.urls", namespace="users")),
    path("manage-project/", include("helpbot_backend.manage_project.urls", namespace="manage_project")),
]
