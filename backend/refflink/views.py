from rest_framework import generics
from rest_framework.views import APIView
from .models import ReffLink
from .serializers import ReffLinkSerializer
from rest_framework.status import HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class ReffLinkListView(generics.ListCreateAPIView):
    queryset = ReffLink.objects.all()
    serializer_class = ReffLinkSerializer


class ReffLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReffLink.objects.all()
    serializer_class = ReffLinkSerializer


class ReffLinkRedirectView(APIView):
    @staticmethod
    def get(request, pk):
        if pk is None:
            return HTTP_404_NOT_FOUND
        refflink = get_object_or_404(ReffLink, pk=pk)
        refflink.count += 1
        refflink.save()
        return HttpResponseRedirect(redirect_to=refflink.link)
