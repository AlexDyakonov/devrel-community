from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import bar
from django_celery_results.models import TaskResult


class TestWorker(APIView):
    def post(self, request, format=None):
        bar.delay()
        return Response("succeed")
