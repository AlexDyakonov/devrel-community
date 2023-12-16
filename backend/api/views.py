from django.shortcuts import render
from rest_framework import generics
from .models import Event, FormFields
from .serializers import EventSerializer, FormFieldsSerializer
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