from typing import Any
from random import randrange

from django.core.management.base import BaseCommand

from faker import Faker

from accounts.models import User, Profile
from posts.models import Post


faker = Faker()


def get_gender() -> str:
    gender: list = ['M', 'F']
    return gender[randrange(2)]


def create_fake_user_and_profile(
        email: str,
        username: str,
        first_name: str,
        last_name: str,
        password: str,
        gender: str,
        description: str,
) -> User:
    """
    Create `User` and `Profile` models use fake data.
    """

    user = User.objects.create_user(
        email=email,
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

    profile = Profile.objects.get(user=user)
    profile.gender = gender
    profile.description = description
    profile.save()

    return user


def create_fake_post(
    author: User,
    content: str,
):
    """
    Create fake `Post`.
    """

    Post.objects.create(
        author=author,
        content=content,
    )


class Command(BaseCommand):
    """
    Fake content command. Fills the database with fake data.
    """

    def handle(self, *args: Any, **options: Any) -> str | None:
        Faker.seed(0)
        for _ in range(100):
            gender = get_gender()
            if gender == 'M':
                first_name = faker.first_name_male()
                last_name = faker.last_name_male()
            else:
                first_name = faker.first_name_female()
                last_name = faker.last_name_female()

            user = create_fake_user_and_profile(
                email=faker.ascii_free_email(),
                username=faker.user_name(),
                first_name=first_name,
                last_name=last_name,
                password=faker.lexify(text='????????'),
                gender=gender,
                description=faker.paragraph()
            )
            create_fake_post(
                author=user,
                content=faker.paragraph()
            )
