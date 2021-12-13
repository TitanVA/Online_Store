from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .service import ProductFilter


class ProductListView(generics.ListAPIView):
    """Вывод списка продуктов"""
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ["title", "description"]

    def get_queryset(self):
        products = Product.objects.all()
        return products

class ProductDetailView(generics.RetrieveAPIView):
    """Вывод продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва продукту"""
    serializer_class = ReviewCreateSerializer


class CategoryListView(generics.ListAPIView):
    """Вывод списка категорий"""
    serializer_class = CategoryListSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ["name"]

    def get_queryset(self):
        categories = Category.objects.all()
        return categories


class CategoryCreateView(generics.CreateAPIView):
    """Добавление категории"""
    serializer_class = CategoryCreateSerializer

