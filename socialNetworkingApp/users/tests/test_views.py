# user/tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.login_url = reverse('login')  # Replace with your actual endpoint name
        self.signup_url = reverse('signup')  # Replace with your actual endpoint name

    def test_login(self):
        data = {'email': 'test@example.com', 'password': 'password'}
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Assuming your API returns a token

    def test_signup(self):
        data = {'email': 'newuser@example.com', 'password': 'password'}
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)  # Assuming your API returns the user ID
