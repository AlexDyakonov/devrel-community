from django.urls import path
from .views import TestWorker, MailingView, TgMessageView

urlpatterns = [
    path('test-worker/', TestWorker.as_view(), name='test-celery-worker'),
    path('send-mailing/', MailingView.as_view(), name='send-mailing'),
    path('send-tg-message/', TgMessageView.as_view(), name='send_tg_message'),
]
