from django.shortcuts import render
from rest_framework import generics
from .models import Event, FormFields
from .serializers import EventSerializer, FormFieldsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.exceptions import NotFound

# Create your views here.


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FormFieldsListCreateView(generics.ListCreateAPIView):
    queryset = FormFields.objects.all()
    serializer_class = FormFieldsSerializer

class FormFieldsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormFields.objects.all()
    serializer_class = FormFieldsSerializer

class UserByTokenAPIView(generics.RetrieveAPIView):
    def get(self, request, format=None):
        token_key = request.GET.get('token', None)

        if not token_key:
            return Response({"error": "Token is required"}, status=400)

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise NotFound("Token not found")

        user = token.user
        serializer = UserSerializer(user)

        return Response(serializer.data)