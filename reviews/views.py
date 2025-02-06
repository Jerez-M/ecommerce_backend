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
from .models import Review
from .serializers import ReviewSerializer, ReviewUpdateSerializer, ReviewRetrieveSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from products.models import Product
from accounts.models import User

# Create your views here.

class CreateReviewView(CreateAPIView):
    permission_classes = []
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": " Review created successfully",
                    "data": serializer.data,
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create  Review, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create  Review. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllReviews(ListAPIView):
    permission_classes = []
    serializer_class = ReviewRetrieveSerializer
    queryset = Review.objects.all()


class ReviewReadDestroyView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = ReviewRetrieveSerializer
    queryset = Review.objects.all()


class UpdateReviewView(UpdateAPIView):
    permission_classes = []
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer


class GetReviewsByUserId(GenericAPIView):
    permission_classes = []
    serializer_class = ReviewRetrieveSerializer
    queryset = Review.objects.all()

    def get(self, request, user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404)
        else:
            Reviews = Review.objects.filter(user_id=user_id)
            serializer = ReviewRetrieveSerializer(Reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class GetReviewsByProductId(GenericAPIView):
    permission_classes = []
    serializer_class = ReviewRetrieveSerializer
    queryset = Review.objects.all()

    def get(self, request, product_id):
        try:
            Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404)
        else:
            Reviews = Review.objects.filter(product_id=product_id)
            serializer = ReviewRetrieveSerializer(Reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
