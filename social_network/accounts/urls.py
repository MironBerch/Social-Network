from django.urls import path

from accounts.views import (
    SignupAPIView,
    SigninAPIView,
    SignoutAPIView,
    ProfileSettingsAPIView,
)


urlpatterns = [
    path(
        route='signup/',
        view=SignupAPIView.as_view(),
        name='signup',
    ),
    path(
        route='signin/',
        view=SigninAPIView.as_view(),
        name='signin',
    ),
    path(
        route='signout/',
        view=SignoutAPIView.as_view(),
        name='signout',
    ),
    path(
        route='profile/settings/',
        view=ProfileSettingsAPIView.as_view(),
        name='profile_settings',
    ),
]
