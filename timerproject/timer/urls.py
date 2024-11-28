from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginViewSet.as_view(), name="login"),
]
