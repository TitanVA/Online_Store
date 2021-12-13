from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *


class CustomerListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetailView(generics.RetrieveAPIView):
    """Вывод покупателя"""
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
