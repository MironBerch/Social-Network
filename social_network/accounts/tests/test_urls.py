from django.urls import resolve, reverse
from django.test import SimpleTestCase

from accounts.views import (
    SignupAPIView,
    SigninAPIView,
    SignoutAPIView,
)


class AccountsUrlsTests(SimpleTestCase):

    def test_signup_api_view_is_resolved(self):
        """Test that SignupAPIView url works correctly."""
        url = reverse('signup')
        self.assertEquals(
            resolve(url).func.view_class, SignupAPIView,
        )

    def test_signin_api_view_is_resolved(self):
        """Test that SigninAPIView url works correctly."""
        url = reverse('signin')
        self.assertEquals(
            resolve(url).func.view_class, SigninAPIView,
        )

    def test_signout_api_view_is_resolved(self):
        """Test that SignoutAPIView url works correctly."""
        url = reverse('signout')
        self.assertEquals(
            resolve(url).func.view_class, SignoutAPIView,
        )
