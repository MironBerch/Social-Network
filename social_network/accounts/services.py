from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from accounts.models import User, Profile


def get_user_by_request(request: Request) -> User:
    """
    Function which return user which send a request.
    """

    user = request.user
    return user


def get_user_profile(user: User) -> Profile:
    """
    Function which return user profile.
    """

    profile = get_object_or_404(Profile, user=user)
    return profile


def create_user_profile(user: User) -> None:
    """
    Function create user profile.
    """

    Profile.objects.create(user=user)
