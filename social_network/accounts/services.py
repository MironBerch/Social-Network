from rest_framework.request import Request

from accounts.models import User, Profile
from accounts.exceptions import (
    AccountDoesNotExistException,
    ProfileDoesNotExistException,
)


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

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        raise ProfileDoesNotExistException()

    return profile


def get_user_by_username(username: str) -> User:
    """
    Function which return user by username.
    """

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise AccountDoesNotExistException()

    return user
