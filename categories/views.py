import random
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer, CategoryUpdateSerializer, CategoryRetrieveSerializer


# Create your views here.

class CreateCategoryView(CreateAPIView):
    permission_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": " Category created successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create  category, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create  category. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllCategories(ListAPIView):
    permission_classes = []
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()


class CategoryReadDestroyView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()


class UpdateCategoryView(UpdateAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
