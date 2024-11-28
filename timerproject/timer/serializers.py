from rest_framework import serializers

from .models import CustomUser


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "id"]
        read_only_fields = ["id"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
