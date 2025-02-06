from .models import Review
from rest_framework.serializers import ModelSerializer
from accounts.serializers import MinimizedUserSerializer
from products.serializers import MinimizedProductRetrieveSerializer
from accounts.models import User

class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

        extra_kwargs = {
            "name": {"product": True},
            "name": {"user": True},
            "name": {"rating": True},
        }


class ReviewRetrieveSerializer(ModelSerializer):
    user = MinimizedUserSerializer()
    product = MinimizedProductRetrieveSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class MinimizedReviewRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = ["id", "user", "rating"]


class ReviewUpdateSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"