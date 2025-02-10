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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from reviews.models import Review

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


class ProductFilterView(GenericAPIView):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_queryset(self):
        queryset = Product.objects.all()
        
        # Filter by category
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # Filter by price range
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        # Filter by product status
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        # Filter by minimum rating
        min_rating = self.request.query_params.get('min_rating')
        if min_rating:
            filtered_products = []
            for product in queryset:
                reviews = Review.objects.filter(product=product)
                if reviews.exists():
                    avg_rating = sum(r.rating for r in reviews) / reviews.count()
                    if avg_rating >= float(min_rating):
                        filtered_products.append(product)
            queryset = filtered_products

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Apply ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)