from django.test import TestCase

from accounts.models import User
from accounts.services import (
    get_user_profile,
    get_user_by_username,
)


class AccountsServicesTests(TestCase):

    def setUp(self):
        User.objects.create_user(
            email='user@gmail.com',
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_get_user_profile(self):
        """Test that get_user_profile method works correctly."""
        self.assertTrue(
            User.objects.get(email='user@gmail.com'),
            get_user_profile(user=User.objects.get(email='user@gmail.com')),
        )

    def test_get_user_by_username(self):
        """Test that get_user_by_username method works correctly."""
        self.assertTrue(
            User.objects.get(email='user@gmail.com'),
            get_user_by_username(username='JohnDoe'),
        )
