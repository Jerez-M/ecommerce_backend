from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateReviewView.as_view(), name="create_reviews"),
    path(
        "<int:pk>/",
        views.ReviewReadDestroyView.as_view(),
        name="get_reviews",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateReviewView.as_view(),
        name="update_reviews",
    ),
    path(
        "get-all/", views.GetAllReviews.as_view(), name="all_Reviews"
    ),
    path(
        "get-by-user-id/<int:user_id>/", views.GetReviewsByUserId.as_view(), name="user_Reviews"
    ),
    path(
        "get-by-product-id/<int:product_id>/", views.GetReviewsByProductId.as_view(), name="product_Reviews"
    ),
]
