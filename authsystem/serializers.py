from rest_framework import serializers

from .models import User


class UserPresentationSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    id = serializers.UUIDField()
    class Meta:
        model = User
        exclude = ["password"]
    
class UserRegisterSerializer(serializers.ModelSerializer):
    '''Register serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )
    class Meta:
        model = User
        fields = ("username", "email", "password")
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data,)