from rest_framework import filters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from services.views_utils import StandardResultsSetPagination

from .backend import JWTAuthClass
from .models import User
from .serializers import UserPresentationSerializer, UserRegisterSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
    presentation_serializer = UserPresentationSerializer

    def post(self, request) -> Response:
        response, status_code = JWTAuthClass.register(
            request, self.serializer_class, self.presentation_serializer
        )
        return Response(response, status_code)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPresentationSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "username", "email"]
    tags = ["User"]


class SupportAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
    presentation_serializer = UserPresentationSerializer

    def get(self, request) -> Response:
        auth_class = JWTAuthClass()
        user, success = auth_class.authenticate(request)

        if success:
            return Response(self.presentation_serializer(user).data, 200)

        return Response({"detail": "Invalid data"}, 404)
