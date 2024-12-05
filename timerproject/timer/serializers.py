from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("invalid email")
        print("serializer validate")
        return value
