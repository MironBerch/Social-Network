from django.urls import resolve, reverse
from django.test import SimpleTestCase

from accounts.views import (
    SignupAPIView,
    SigninAPIView,
    SignoutAPIView,
    ProfileSettingsAPIView,
    ProfileAPIView,
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

    def test_profile_settings_api_view_is_resolved(self):
        """Test that ProfileSettingsAPIView url works correctly."""
        url = reverse('profile_settings')
        self.assertEquals(
            resolve(url).func.view_class, ProfileSettingsAPIView,
        )

    def test_profile_view_api_view_is_resolved(self):
        """Test that ProfileAPIViewurl works correctly."""
        url = reverse('profile_view', args=['a', ])
        self.assertEquals(
            resolve(url).func.view_class, ProfileAPIView,
        )
