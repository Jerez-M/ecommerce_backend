from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "username",
            "is_superuser",
            "is_staff",
            "is_active",
            "account_status",
            "user_permissions",
            "groups",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "phone_number": {"required": True},
        }

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "role",
            "username",
            "is_superuser",
            "is_staff",
            "is_active",
            "account_status",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["role"] = user.role
        token["user_permission"] = (
            f"{[perm.codename for perm in user.user_permissions.all()]}"
        )

        return token


class RetrieveUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "firstName",
            "lastName",
            "phone_number",
        ]
    
class PasswordVerifyAndChangeSerializer(serializers.Serializer):
        username = serializers.CharField(required=True)
        password = serializers.CharField(required=True)


class AuditTrailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
        ]


class RetrieveUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {"password": {"write_only": True}}


class MinimizedUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]

        extra_kwargs = {"password": {"write_only": True}}
