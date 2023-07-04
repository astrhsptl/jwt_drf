from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from services.authentication import UserAuthentication

from .serializers import UserPresentationSerializer, UserRegisterSerializer

class RegisterAPIView(GenericAPIView):
    '''This api relise sign up on jwt architecture. Return  name, surname, email, is_superuser, is_staff '''
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )
    presentation_serializer = UserPresentationSerializer

    def post(self, request) -> Response:
        authentication = UserAuthentication(request, self.serializer_class, self.presentation_serializer)
        return Response(*authentication.register())
    
# class Test(GenericAPIView):
#     '''This api relise sign up on jwt architecture. Return  name, surname, email, is_superuser, is_staff '''
#     permission_classes = (IsAuthenticated, )

#     def get(self, request) -> Response:
#         print(request.user)
#         return Response({'test': 'successful'})
    
