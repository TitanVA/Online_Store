from abc import ABC

from rest_framework import serializers

from users.serializers import CustomerDetailSerializer, CustomerListSerializer
from .models import *


class FilterReviewSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ProductListSerializer(serializers.ModelSerializer):
    """Список продуктов"""

    class Meta:
        model = Product
        fields = ("category", "title")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)
    person_id = CustomerListSerializer(read_only=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = "id", "date_created", "person_id", "text", "children"


class ProductDetailSerializer(serializers.ModelSerializer):
    """Полный продукт"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = ("name", )


class CategoryCreateSerializer(serializers.ModelSerializer):
    """Создание категории"""

    class Meta:
        model = Category
        fields = "__all__"
