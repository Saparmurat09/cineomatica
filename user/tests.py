from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.reverse import reverse

from .models import User, ClubCard

class RegisterLoginAuthTest(APITestCase):
    def test_register(self):
        url = reverse('register')

        data = {
            'email': 'user@mail.com',
            'name': 'Userbek',
            'surname': 'Useruulu',
            'phone': '+996700112233',
            'is_admin': False,
            'birth_date': '2002-12-12',
            'password': 'Peasant12',
            'password2': 'Peasant12'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(ClubCard.objects.count(), 1)

    def test_login(self):
        url = reverse('register')

        data = {
            'email': 'user@mail.com',
            'name': 'Userbek',
            'surname': 'Useruulu',
            'phone': '+996700112233',
            'is_admin': False,
            'birth_date': '2002-12-12',
            'password': 'Peasant12',
            'password2': 'Peasant12'
        }

        response = self.client.post(url, data)
        
        data = {
            'email': 'user@mail.com',
            'password': 'Peasant12'
        }

        url = reverse('login')

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())

    def test_auth(self):
        url = reverse('register')

        data = {
            'email': 'user@mail.com',
            'name': 'Userbek',
            'surname': 'Useruulu',
            'phone': '+996700112233',
            'is_admin': False,
            'birth_date': '2002-12-12',
            'password': 'Peasant12',
            'password2': 'Peasant12'
        }

        response = self.client.post(url, data)

        data = {
            'email': 'user@mail.com',
            'password': 'Peasant12'
        }

        url = reverse('login')

        response = self.client.post(url, data)

        access_token = response.json()['access']

        client = APIClient()
        
        user = User.objects.last()

        client.force_authenticate(user, token=access_token)

        url = reverse('')

        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
