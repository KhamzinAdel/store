from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from products.serializers import ProductSerializer
from products.services import cashes_product


class ProductListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('price', 'season', 'gender', 'category')

    def get_queryset(self):
        queryset = Product.objects.all()
        products = cashes_product('products', queryset, 30)
        return products


class ProductDetailAPIView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)
