from django.urls import path
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)
from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
    path("verify-password/", views.VerifyPasswordView.as_view(), name="very_pwd"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change_pwd"),
]
