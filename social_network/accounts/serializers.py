from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import User, Profile


class SignupSerializer(serializers.ModelSerializer):
    """
    Signup API view serializer.
    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=30,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=30,
    )
    password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
        )


class ProfileSerializer(serializers.ModelSerializer):
    """
    User profile serializer.
    """

    gender = serializers.ChoiceField(
        required=False,
        choices=Profile.GENDER_CHOICES,
    )

    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'profile_banner',
            'gender',
            'description',
        )


class PasswordSerializer(serializers.ModelSerializer):
    """
    Reset password serializer.
    """

    current_password = serializers.CharField(
        min_length=8,
        write_only=True,
    )
    password = serializers.CharField(
        min_length=8,
        write_only=True,
    )
    password2 = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            'current_password',
            'password',
            'password2',
        ]

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if (
            password and password2 and
            password != password2
        ):
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def validate_current_password(self, data):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(data):
            raise serializers.ValidationError('Incorrect password')
        return data


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer.
    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=30,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=30,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        )
