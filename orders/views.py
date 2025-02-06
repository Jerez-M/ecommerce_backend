import random
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderItemUpdateSerializer, OrderItemRetrieveSerializer, OrderSerializer, OrderUpdateSerializer, OrderRetrieveSerializer
from products.models import Product
from accounts.models import User

# Create your views here.

class CreateOrderItemView(CreateAPIView):
    permission_classes = []
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": " OrderItem created successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create  OrderItem, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create  OrderItem. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllOrderItems(ListAPIView):
    permission_classes = []
    serializer_class = OrderItemRetrieveSerializer
    queryset = OrderItem.objects.all()


class OrderItemReadDestroyView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = OrderItemRetrieveSerializer
    queryset = OrderItem.objects.all()


class UpdateOrderItemView(UpdateAPIView):
    permission_classes = []
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemUpdateSerializer


class GetOrderItemsByProductId(GenericAPIView):
    permission_classes = []
    serializer_class = OrderItemRetrieveSerializer
    queryset = OrderItem.objects.all()

    def get(self, request, product_id):
        try:
            Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            OrderItems = OrderItem.objects.filter(product_id=product_id)
            serializer = OrderItemRetrieveSerializer(OrderItems, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


# Order Views
class CreateOrderView(CreateAPIView):
    permission_classes = []
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": " Order created successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create  Order, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create  Order. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllOrders(ListAPIView):
    permission_classes = []
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.all()


class OrderReadDestroyView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.all()


class UpdateOrderView(UpdateAPIView):
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer

class GetOrdersByUserId(GenericAPIView):
    permission_classes = []
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.all()

    def get(self, request, user_id):
        try:
            OrderItem.objects.get(pk=user_id)
        except Product.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            Orders = Order.objects.filter(user_id=user_id)
            serializer = OrderRetrieveSerializer(Orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetOrdersByOrderItemId(GenericAPIView):
    permission_classes = []
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.all()

    def get(self, request, order_item_id):
        try:
            OrderItem.objects.get(pk=order_item_id)
        except Product.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            Orders = Order.objects.filter(order_items=order_item_id)
            serializer = OrderRetrieveSerializer(Orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
