from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


