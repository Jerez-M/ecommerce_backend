from django.urls import path
from . import views

urlpatterns = [
    path("order-items/", views.CreateOrderItemView.as_view(), name="create_orderItems"),
    path(
        "order-items/<int:pk>/",
        views.OrderItemReadDestroyView.as_view(),
        name="get_OrderItems",
    ),
    path(
        "order-items/update/<int:pk>/",
        views.UpdateOrderItemView.as_view(),
        name="update_OrderItems",
    ),
    path(
        "order-items/get-all/", views.GetAllOrderItems.as_view(), name="all_OrderItems"
    ),
    path(
        "order-items/get-by-product-id/<int:product_id>/", views.GetOrderItemsByProductId.as_view(), name="a_OrderItems"
    ),

    path("", views.CreateOrderView.as_view(), name="create_orders"),
    path(
        "<int:pk>/",
        views.OrderReadDestroyView.as_view(),
        name="get_Orders",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateOrderView.as_view(),
        name="update_Orders",
    ),
    path(
        "get-all/", views.GetAllOrders.as_view(), name="all_Orders"
    ),
    path(
        "get-by-user-id/<int:user_id>/", views.GetOrdersByUserId.as_view(), name="user_OrderItems"
    ),
    path(
        "get-by-oder-item/<int:order_item_id>/", views.GetOrdersByOrderItemId.as_view(), name="item_OrderItems"
    ),
]
