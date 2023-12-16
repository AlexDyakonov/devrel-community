from django.urls import path
from .views import TestWorker, MailingView

urlpatterns = [
    path('test-worker/', TestWorker.as_view(), name='test-celery-worker'),
    path('send-mailing/', MailingView.as_view(), name='send-mailing'),
]
