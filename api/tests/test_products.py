from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product, ProductCategory
from products.serializers import ProductSerializer, ProductCategorySerializer


class ProductCategoryTests(APITestCase):

    def setUp(self):
        self.product_category_1 = ProductCategory.objects.create(name='Одежда', description='Одежда-это')
        self.product_category_2 = ProductCategory.objects.create(name='Обувь', description='Обувь-это')

    def test_get(self):
        url = reverse('api:product_category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_get(self):
        url = reverse('api:product_category')
        response = self.client.get(url)
        serializer_data = ProductCategorySerializer([self.product_category_1, self.product_category_2], many=True).data
        self.assertEqual(serializer_data, response.data)


class ProductCategorySerializerTests(TestCase):

    def test_serializer(self):
        product_category_1 = ProductCategory.objects.create(name='Одежда', description='Одежда-это')
        product_category_2 = ProductCategory.objects.create(name='Обувь', description='Обувь-это')
        data = ProductCategorySerializer([product_category_1, product_category_2], many=True).data
        expected_data = [
            {
                'id': product_category_1.id,
                'name': 'Одежда',
            },
            {
                'id': product_category_2.id,
                'name': 'Обувь',
            }
        ]
        self.assertEqual(expected_data, data)


class ProductTests(APITestCase):

    def test_get(self):
        url = reverse('api:product-queryset-retrieve')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
