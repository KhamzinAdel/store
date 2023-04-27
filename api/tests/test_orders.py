import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order
from orders.serializers import OrderListSerializer
from users.models import User


class OrderTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='test_username',)
        self.order_1 = Order.objects.create(first_name='Adel', address='Moscow', initiator=self.user)
        self.order_2 = Order.objects.create(first_name='Max', address='Kazan', initiator=self.user)

    def test_get(self):
        self.client.force_login(self.user)
        url = reverse('api:order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_get(self):
        self.client.force_login(self.user)
        url = reverse('api:order')
        response = self.client.get(url)
        serializer_data = OrderListSerializer([self.order_1, self.order_2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(Order.objects.all().count(), 2)
        url = reverse('api:order')
        data = {
                "first_name": "name",
                "last_name": "last_name",
                "email": "name.last_name@mail.ru",
                "address": "Kazan"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.all().count(), 3)
