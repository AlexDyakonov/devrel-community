from rest_framework import serializers
from .models import CustomUser, Role, UserProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'middle_name', 'sex', 'birth_date', 'bio', 'avatar')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class UserProfileSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True) 

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'roles')