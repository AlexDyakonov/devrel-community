from django.shortcuts import render
from rest_framework import generics, serializers
from .models import User, Specialization, Skill
from .serializers import UserSerializer, SpecializationSerializer, SkillSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from utils.email.email_utils import send_token_email


# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SpecializationList(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    backref = serializers.CharField(default="http://0.0.0.0/")


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        backref = serializer.validated_data.get('backref')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        send_token_email(user, backref + "?token=" + token.key)
        return Response({'token': token.key})
