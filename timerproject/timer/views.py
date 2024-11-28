from django.contrib.auth import login
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CustomUser
from .serializers import LoginSerializer, UserSerializer


class LoginViewSet(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = CustomUser.objects.get(email=email)

            if user.check_password(password):
                login(request, user)
                return Response(
                    {
                        "user": UserSerializer(
                            user, context=self.get_serializer_context()
                        ).data
                    }
                )
            else:
                return Response(
                    {"error": "パスワードが間違っています。"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        except CustomUser.DoesNotExist:
            return Response(
                {"error": "ユーザーが存在しません。"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
