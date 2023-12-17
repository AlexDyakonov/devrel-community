from django.shortcuts import render
from rest_framework import generics
from .models import Event, FormFields
from .serializers import EventSerializer, FormFieldsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from utils.yagpt.yagpt import send_message


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


class AskGPTSerializer(serializers.Serializer):
    message = serializers.CharField()


class AskGPTView(CreateAPIView):
    serializer_class = AskGPTSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = AskGPTSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('message')
            print(text)
            return Response(send_message(text))
        return status.HTTP_400_BAD_REQUEST
