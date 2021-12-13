from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view()),
    path("categories/create/", views.CategoryCreateView.as_view()),
    path("product/", views.ProductListView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
]
