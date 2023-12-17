from django.shortcuts import render
from rest_framework import generics
from .models import Event, FormFields
from .serializers import EventSerializer, FormFieldsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.models import User
from rest_framework import serializers
from rest_framework.views import APIView
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from utils.yagpt.yagpt import send_message
from django.shortcuts import get_object_or_404


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


class ParticipationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class ParticipateView(CreateAPIView):
    serializer_class = ParticipationSerializer

    @staticmethod
    def post(request, pk, *args, **kwargs):
        event: Event = get_object_or_404(Event, pk=pk)
        serializer = ParticipationSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, pk=serializer.validated_data.get('user_id'))
            event.participants.add(user)
            event.save()
            return Response()
        return status.HTTP_400_BAD_REQUEST

class EventFormDataAPIView(APIView):
    def get(self, request, event_id, format=None):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        form_fields = FormFields.objects.filter(event=event)
        data = [field.get_data() for field in form_fields]
        
        return Response(data)