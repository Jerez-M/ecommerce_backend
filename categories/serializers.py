from .models import Category
from rest_framework.serializers import ModelSerializer
from accounts.serializers import MinimizedUserSerializer


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

        extra_kwargs = {
            "name": {"required": True},
        }


class CategoryRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class MinimizedCategoryRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryUpdateSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"