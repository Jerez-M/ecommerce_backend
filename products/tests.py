from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product
from categories.models import Category
from decimal import Decimal  # Import Decimal for price comparison

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),  # Use Decimal for price
            stock=10,
            category=self.category,
            status="Available"
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.description, "A smart phone")
        self.assertEqual(self.product.price, Decimal("599.99"))  # Compare with Decimal
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category.name, "Electronics")
        self.assertEqual(self.product.status, "Available")

    def test_product_status_update(self):
        self.product.stock = 0
        self.product.update_status()
        self.assertEqual(self.product.status, "Sold Out")

class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Electronics")
        self.product_data = {
            "name": "Laptop",
            "description": "A powerful laptop",
            "price": Decimal("999.99"),  # Use Decimal for price
            "stock": 5,
            "category": self.category.id,
            "status": "Available"
        }
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),  # Use Decimal for price
            stock=10,
            category=self.category,
            status="Available"
        )

    def test_create_product(self):
        url = reverse("create_products")
        response = self.client.post(url, self.product_data, format="multipart")  # Use multipart format
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_get_all_products(self):
        url = reverse("all_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_by_id(self):
        url = reverse("get_products", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Smartphone")

    def test_update_product(self):
        url = reverse("update_products", args=[self.product.id])
        updated_data = {
            "name": "Updated Smartphone",
            "description": "An updated smart phone",
            "price": Decimal("699.99"),  # Use Decimal for price
            "stock": 15,
            "category": self.category.id,
            "status": "Available"
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Smartphone")
        self.assertEqual(self.product.price, Decimal("699.99"))  # Compare with Decimal

    def test_delete_product(self):
        url = reverse("get_products", args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_get_products_by_category_id(self):
        url = reverse("a_products", args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_product_filter_view(self):
        url = reverse("product_search")
        response = self.client.get(url, {"category": self.category.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(url, {"price_min": 500, "price_max": 1000})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(url, {"status": "Available"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)