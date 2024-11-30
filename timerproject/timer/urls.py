from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path(r"token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(r"token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
