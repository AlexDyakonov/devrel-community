from rest_framework import generics
from .models import Source, SourceUsers
from .serializers import SourceSerializer, SourceUsersSerializer
from .tasks import process_and_save_user_data

class SourceListView(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.type == 'tg':
            process_and_save_user_data(instance.url) #TODO database is locked, надо фиксить


class SourceUsersListView(generics.ListCreateAPIView):
    queryset = SourceUsers.objects.all()
    serializer_class = SourceUsersSerializer


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceUsers.objects.all()
    serializer_class = SourceUsersSerializer