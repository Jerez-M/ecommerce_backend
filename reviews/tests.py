from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from products.models import Product, Category
from .models import Review

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=599.99,
            stock=10,
            category=self.category,
            status="Available"
        )
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=5,
            comment="Great product!"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.user.username, "testuser")
        self.assertEqual(self.review.product.name, "Smartphone")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great product!")

class ReviewViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=599.99,
            stock=10,
            category=self.category,
            status="Available"
        )
        # Ensure no review exists for this user and product
        Review.objects.filter(user=self.user, product=self.product).delete()
        
        self.review_data = {
            "user": self.user.id,
            "product": self.product.id,
            "rating": 5,
            "comment": "Great product!"
        }
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment="Good product!"
        )

    # def test_create_review(self):
    #     url = reverse("create_reviews")
    #     response = self.client.post(url, self.review_data, format="json")
        
    #     # Print the response data for debugging
    #     if response.status_code != status.HTTP_201_CREATED:
    #         print("Response data:", response.data)
        
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Review.objects.count(), 2)

    def test_get_all_reviews(self):
        url = reverse("all_Reviews")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_review_by_id(self):
        url = reverse("get_reviews", args=[self.review.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["comment"], "Good product!")

    def test_update_review(self):
        url = reverse("update_reviews", args=[self.review.id])
        updated_data = {
            "user": self.user.id,
            "product": self.product.id,
            "rating": 5,
            "comment": "Updated review!"
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.comment, "Updated review!")

    def test_delete_review(self):
        url = reverse("get_reviews", args=[self.review.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)

    def test_get_reviews_by_user_id(self):
        url = reverse("user_Reviews", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_reviews_by_product_id(self):
        url = reverse("product_Reviews", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)