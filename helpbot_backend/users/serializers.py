from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "date_joined", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmailSerializer(serializers.Serializer):
    email_address = serializers.EmailField()


class ClerkCreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
