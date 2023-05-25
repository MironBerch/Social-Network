from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User, Profile


class SignupAPIViewTests(APITestCase):
    url = reverse('signup')

    def test_signup(self):
        """Test that SignupAPIView works correctly."""
        data = {
            'email': 'email@gmail.com',
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'password': 'password',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)


class SigninAPIViewTests(APITestCase):
    url = reverse('signin')

    def setUp(self):
        User.objects.create_user(
            email='user@gmail.com',
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_signin_with_success_status_code(self):
        """Test that signin works with corect credentials."""
        credentials = {
            'email': 'user@gmail.com',
            'password': 'password',
        }
        response = self.client.post(self.url, credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_with_failure_status_code(self):
        """Test that signin works with uncorect credentials."""
        credentials = {
            'email': 'not@gmail.com',
            'password': 'password',
        }
        response = self.client.post(self.url, credentials)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SignoutAPIViewTests(APITestCase):
    url = reverse('signout')

    def test_signout_status_code(self):
        """Test that SignoutAPIView return correct status code."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProfileSettingsAPIViewTests(APITestCase):
    url = reverse('profile_settings')
    signin_url = reverse('signin')
    credentials = {'email': 'user@gmail.com', 'password': 'password'}

    def setUp(self):
        User.objects.create_user(
            email='user@gmail.com',
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_profile_settings_with_success_status_code(self):
        """Test that profile settings API view works with corect data."""
        self.client.post(self.signin_url, self.credentials)
        data = {
            'gender': 'F',
            'description': 'new_description',
        }
        response = self.client.post(self.url, data)
        profile = (
            Profile.objects.get(
                user=User.objects.get(email='user@gmail.com'),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(profile.gender, 'F')
        self.assertEqual(profile.description, 'new_description')


class ProfileAPIViewTests(APITestCase):
    unsuccess_url = reverse('profile_view', args=['None', ])
    success_url = reverse('profile_view', args=['JohnDoe', ])

    def setUp(self):
        User.objects.create_user(
            email='user@gmail.com',
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_profile_view_status_code(self):
        """Test that profile API view works with corect data."""
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_view_failure_status_code(self):
        """Test that profile API view works with uncorect data."""
        response = self.client.get(self.unsuccess_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
