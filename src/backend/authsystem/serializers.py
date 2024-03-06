from rest_framework import serializers

from .models import User


class UserPresentationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    class Meta:
        model = User
        exclude = ["password"]
    
class UserRegisterSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()


    password = serializers.CharField(max_length=256)
    
    class Meta:
        model = User
        fields = ("__all__")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data,)