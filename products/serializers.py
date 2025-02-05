from .models import Product
from rest_framework.serializers import ModelSerializer
from accounts.serializers import MinimizedUserSerializer
from categories.serializers import MinimizedCategoryRetrieveSerializer


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

        extra_kwargs = {
            "name": {"required": True},
        }


class ProductRetrieveSerializer(ModelSerializer):
    category = MinimizedCategoryRetrieveSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class MinimizedProductRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductUpdateSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"