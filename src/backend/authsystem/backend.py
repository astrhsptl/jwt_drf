import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from authsystem.models import User


class JWTAuthClass(BaseAuthentication):
    def authenticate(self, request, username=None, *args, **kwargs):
        headers = get_authorization_header(request)
        email = request.data.get("email")
        username = request.data.get("username")

        if headers:
            return self._auth_by_jwt(headers)
        elif email:
            password = request.data.get("password")
            return self._auth_by_email(email, password)
        elif username:
            password = request.data.get("password")
            return self._auth_by_username(username, password)

        return None, False

    @staticmethod
    def register(request, serializer, presentaiton_serializer=None, **kwargs):
        data = serializer(data=request.data)
        if data.is_valid():
            user = data.save()
            return {**dict(presentaiton_serializer(user).data)}, status.HTTP_200_OK

        return data.errors, status.HTTP_400_BAD_REQUEST

    def _auth_by_jwt(self, headers):
        auth_data = headers.decode("utf-8")
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            return None, False

        token = auth_token[1]

        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, "HS256")
            user = User.objects.get(pk=decoded["user_id"])
            return user, True
        except:
            return None, False

    def _auth_by_email(self, email, password):
        try:
            user = User.objects.get(email=email)
        except:
            return None, False

        if user.check_password(password):
            return user, True

        return None, False

    def _auth_by_username(self, username, password):
        try:
            user = User.objects.get(username=username)
        except:
            return None, False

        if user.check_password(password):
            return user, True
        return None, False
