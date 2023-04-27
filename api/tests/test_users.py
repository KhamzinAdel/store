import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class ContactTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='test_username',)

    def test_create(self):
        url = reverse('api:contact')
        data = {
                "first_name": "name",
                "last_name": "last_name",
                "email": "name.last_name@mail.ru",
                "content": "content_1"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
