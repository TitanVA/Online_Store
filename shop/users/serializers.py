from rest_framework import serializers
from .models import *


class CustomerListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name")


class CustomerDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания покупателя"""

    class Meta:
        model = Customer
        fields = "__all__"
