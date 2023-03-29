from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class SuccessTemplateViewTest(TestCase):
    def test_view(self):
        path = reverse('orders:order-success')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Спасибо за заказ!')
        self.assertTemplateUsed(response, 'orders/success.html')


class CanceledTemplateViewTest(TestCase):
    def test_view(self):
        path = reverse('orders:order-canceled')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'orders/canceled.html')
