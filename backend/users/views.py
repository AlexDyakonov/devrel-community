from django.shortcuts import render
from rest_framework import generics
from .models import User, Specialization, Skill
from .serializers import UserSerializer, SpecializationSerializer, SkillSerializer


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