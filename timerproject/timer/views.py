from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CustomUserSerializer


def CsrfView(request):
    return JsonResponse({"token": get_token(request)})


def PingView(request):
    return JsonResponse({"result": True})


class LoginView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            login(request, user)
            print("view validate")
            return Response(
                {
                    "user": CustomUserSerializer(
                        user, context=self.get_serializer_context()
                    ).data
                }
            )
        return Response(
            {"error": "エラーが発生しました"}, status=status.HTTP_401_UNAUTHORIZED
        )
