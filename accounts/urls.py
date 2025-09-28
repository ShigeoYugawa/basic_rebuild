from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    registration_view,
    CustomLoginView,
    CustomLogoutView,
    welcome_view,
)

app_name = "accounts"

urlpatterns = [
    path("welcome/", welcome_view, name="welcome_view"),

    path("register/", registration_view, name="registration"),

    path("login/", CustomLoginView.as_view(), name="login"),

    path("logout/", CustomLogoutView.as_view(), name="logout"),
]