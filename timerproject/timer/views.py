from django.contrib.auth import authenticate

# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework.viewsets import ModelViewSet

# from .models import CustomUser
# from .serializers import UserSerilaizer


# class UserViewSet(ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerilaizer


@api_view(["POST"])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)
    if user is not None:
        # ユーザーが存在する場合の処理
        return Response({"message": "ログイン成功"})
    else:
        # ユーザーが存在しない場合の処理
        return Response({"message": "ユーザーが存在しません"}, status=400)
