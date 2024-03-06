from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import RegisterAPIView, SupportAPIView, UserViewSet

router = SimpleRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("user/by/token", SupportAPIView.as_view(), name="lbt"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify_token/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router.urls
