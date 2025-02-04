from rest_framework.serializers import ModelSerializer
from ..models import User


class AuditTrailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
        ]


class UserProfPicSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "profile_picture",
        ]


class UserPermissionsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = []


class UserProfPicRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "profile_picture",
        ]
