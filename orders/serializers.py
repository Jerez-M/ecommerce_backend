from .models import OrderItem, Order
from rest_framework.serializers import ModelSerializer
from accounts.serializers import MinimizedUserSerializer
from products.serializers import MinimizedProductRetrieveSerializer

class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"

        extra_kwargs = {
            "name": {"product": True},
        }


class OrderItemRetrieveSerializer(ModelSerializer):
    product = MinimizedProductRetrieveSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class MinimizedOrderItemRetrieveSerializer(ModelSerializer):
    # product = MinimizedProductRetrieveSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemUpdateSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"


# Order Serializers

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

        extra_kwargs = {
            "name": {"user": True},
        }


class OrderRetrieveSerializer(ModelSerializer):
    # order_items = MinimizedOrderItemRetrieveSerializer()
    user = MinimizedUserSerializer()

    class Meta:
        model = Order
        fields = "__all__"


class MinimizedOrderRetrieveSerializer(ModelSerializer):
    product = MinimizedProductRetrieveSerializer()
    user = MinimizedUserSerializer()

    class Meta:
        model = Order
        exclude = ["created_at", "updated_at"]


class OrderUpdateSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"