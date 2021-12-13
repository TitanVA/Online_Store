from django_filters import rest_framework as filters

from shop.models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ["is_in_stock"]
