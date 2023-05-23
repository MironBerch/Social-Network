from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import (
    IsUserProfileOwner,
    IsNotAuthenticated,
)
from accounts.serializers import (
    SignupSerializer,
    ProfileSerializer,
)
from accounts.services import (
    get_user_by_request,
    get_user_profile,
    get_user_by_username,
)


class SignupAPIView(APIView):
    """
    Signup API view.
    """

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(
                    json,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SigninAPIView(APIView):
    """
    Signin API view.
    """

    permission_classes = (IsNotAuthenticated,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(
            request=request,
            email=email,
            password=password,
        )

        if user is not None:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data={'message': 'Invalid email or password'}
            )


class SignoutAPIView(APIView):
    """
    Signout API view.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return redirect('signin')


class ProfileSettingsAPIView(APIView):
    """
    Profile setting API view.
    """

    permission_classes = (IsUserProfileOwner,)

    def get(self, request):
        profile = get_user_profile(
            user=get_user_by_request(request=request),
        )
        return Response(
            {
                'user': profile.user.username,
                'profile_image': profile.profile_image.url,
                'profile_banner': profile.profile_banner.url,
                'gender': profile.gender,
                'description': profile.description,
            }
        )

    def post(self, request):
        profile = get_user_profile(
            user=get_user_by_request(request=request),
        )
        serializer = ProfileSerializer(
            instance=profile,
            data=request.data,
        )
        if serializer.is_valid():
            profile = serializer.save()
            json = serializer.data
            return Response(
                json,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileAPIView(APIView):
    """
    Profile  API view.
    """

    permission_classes = (AllowAny,)

    def get(self, request, username):
        profile = get_user_profile(
            user=get_user_by_username(username=username),
        )

        return Response(
            {
                'username': profile.user.username,
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'profile_image': profile.profile_image.url,
                'profile_banner': profile.profile_banner.url,
                'gender': profile.gender,
                'description': profile.description,
            }
        )
