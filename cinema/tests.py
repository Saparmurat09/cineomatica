from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.reverse import reverse
# from django.urls import reverse


class TestHomePage(APITestCase):
    def test_homepage(self):
        url = reverse('root')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestMovie():
    def test_get():
        pass