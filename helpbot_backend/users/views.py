from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClerkCreateUserSerializer, CreateUserSerializer, EmailSerializer

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class CreateUser(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class ClerkCreateUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data.get("data", {})
        # handle primary email
        email_data = data.get("email_addresses", [])
        email_serializer = EmailSerializer(data=email_data, many=True)
        if not email_serializer.is_valid():
            return Response(email_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email_addresses = email_serializer.validated_data

        data["email"] = dict(email_addresses[0])["email_address"]
        user_serializer = ClerkCreateUserSerializer(data=data)

        if user_serializer.is_valid():
            user_serializer.validated_data
            user_serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
