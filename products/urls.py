from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateProductView.as_view(), name="create_products"),
    path(
        "<int:pk>/",
        views.ProductReadDestroyView.as_view(),
        name="get_products",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateProductView.as_view(),
        name="update_products",
    ),
    path(
        "get-all/", views.GetAllProducts.as_view(), name="all_products"
    ),
    path(
        "get-by-category-id/<int:category_id>/", views.GetProductsByCategoryId.as_view(), name="a_products"
    ),
    path(
        "search/", views.ProductFilterView.as_view(), name="product_search"
    ),
]
