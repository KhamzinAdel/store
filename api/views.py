from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from products.models import Product
from products.serializers import ProductSerializer


class ProductListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
