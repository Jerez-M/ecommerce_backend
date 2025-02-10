from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from products.models import Product, Category
from .models import OrderItem, Order
from decimal import Decimal

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),
            stock=10,
            category=self.category,
            status="Available"
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,
            price_at_purchase=Decimal("599.99")
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.product.name, "Smartphone")
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.price_at_purchase, Decimal("599.99"))

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),
            stock=10,
            category=self.category,
            status="Available"
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,
            price_at_purchase=Decimal("599.99")
        )
        self.order = Order.objects.create(
            user=self.user,
            status="Pending"
        )
        self.order.order_items.add(self.order_item)

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, "testuser")
        self.assertEqual(self.order.status, "Pending")
        self.assertEqual(self.order.order_items.count(), 1)
        self.assertEqual(self.order.order_items.first().product.name, "Smartphone")

class OrderItemViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),
            stock=10,
            category=self.category,
            status="Available"
        )
        self.order_item_data = {
            "product": self.product.id,
            "quantity": 2,
            "price_at_purchase": "599.99"
        }
        self.order_item = OrderItem.objects.create(
            product=self.product,
            quantity=1,
            price_at_purchase=Decimal("599.99")
        )

    def test_create_order_item(self):
        url = reverse("create_orderItems")
        response = self.client.post(url, self.order_item_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderItem.objects.count(), 2)

    def test_get_all_order_items(self):
        url = reverse("all_OrderItems")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_order_item_by_id(self):
        url = reverse("get_OrderItems", args=[self.order_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["product"]["id"], self.product.id)  # Check nested product ID

    def test_update_order_item(self):
        url = reverse("update_OrderItems", args=[self.order_item.id])
        updated_data = {
            "product": self.product.id,
            "quantity": 3,
            "price_at_purchase": "599.99"
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order_item.refresh_from_db()
        self.assertEqual(self.order_item.quantity, 3)

    def test_delete_order_item(self):
        url = reverse("get_OrderItems", args=[self.order_item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(OrderItem.objects.count(), 0)

    def test_get_order_items_by_product_id(self):
        url = reverse("a_OrderItems", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class OrderViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A smart phone",
            price=Decimal("599.99"),
            stock=10,
            category=self.category,
            status="Available"
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,
            price_at_purchase=Decimal("599.99")
        )
        self.order_data = {
            "user": self.user.id,
            "order_items": [self.order_item.id],
            "status": "Pending"
        }
        self.order = Order.objects.create(
            user=self.user,
            status="Pending"
        )
        self.order.order_items.add(self.order_item)

    def test_create_order(self):
        url = reverse("create_orders")
        response = self.client.post(url, self.order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_get_all_orders(self):
        url = reverse("all_Orders")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_order_by_id(self):
        url = reverse("get_Orders", args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"]["id"], self.user.id)  # Check nested user ID

    def test_update_order(self):
        url = reverse("update_Orders", args=[self.order.id])
        updated_data = {
            "user": self.user.id,
            "order_items": [self.order_item.id],
            "status": "Shipped"
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "Shipped")

    def test_delete_order(self):
        url = reverse("get_Orders", args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

    def test_get_orders_by_user_id(self):
        url = reverse("user_OrderItems", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_orders_by_order_item_id(self):
        url = reverse("item_OrderItems", args=[self.order_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)