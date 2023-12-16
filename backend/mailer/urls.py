from django.urls import path
from .views import TestWorker

urlpatterns = [
    path('test-worker/', TestWorker.as_view(), name='test-celery-worker'),
]
