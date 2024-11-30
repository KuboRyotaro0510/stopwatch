from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response(
                {
                    "user": CustomUserSerializer(
                        user, context=self.get_serializer_context()
                    ).data
                }
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
