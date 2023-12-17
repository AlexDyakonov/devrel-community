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
from rest_framework.parsers import JSONParser

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
    redirect = serializers.CharField(default="http://0.0.0.0/")


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        redirect = serializer.validated_data.get('redirect')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        send_token_email(user, redirect + "?token=" + token.key)
        return Response({'token': token.key})


class UploadUsers(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        users_data = request.data
        serializer = UserSerializer(data=users_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)