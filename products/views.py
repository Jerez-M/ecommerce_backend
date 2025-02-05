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
from .models import Product
from .serializers import ProductSerializer, ProductUpdateSerializer, ProductRetrieveSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from categories.models import Category

# Create your views here.

class CreateProductView(CreateAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": " Product created successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create  Product, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create  Product. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllProducts(ListAPIView):
    permission_classes = []
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


class ProductReadDestroyView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


class UpdateProductView(UpdateAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class GetProductsByCategoryId(GenericAPIView):
    permission_classes = []
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()

    def get(self, request, category_id):
        try:
            Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response("Category does not exist", status=status.HTTP_404)
        else:
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductRetrieveSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
