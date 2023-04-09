from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

from products.models import Product, ProductCategory
from products.serializers import ProductCategorySerializer, ProductSerializer
from products.services import cashes_product


class ProductListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('price', 'season', 'gender', 'category')
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'price')

    def get_queryset(self):
        queryset = Product.objects.all().select_related('category')
        products = cashes_product('products', queryset, 30)
        return products


class ProductCategoryListAPIView(ListAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        queryset = ProductCategory.objects.values('id', 'name').order_by('id')
        categories = cashes_product('categories', queryset, 30)
        return categories
