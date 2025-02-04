from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateCategoryView.as_view(), name="create_category"),
    path(
        "<int:pk>/",
        views.CategoryReadDestroyView.as_view(),
        name="get_category",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateCategoryView.as_view(),
        name="get_categories",
    ),
    path(
        "get-all/", views.GetAllCategories.as_view(), name="all_categories"
    ),
]
