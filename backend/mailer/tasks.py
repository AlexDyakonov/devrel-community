from celery import shared_task
from django.core.mail import send_mail
from .serializers import MailSerializer
from django.conf import settings


@shared_task
def bar():
    return "Hello world!"


@shared_task
def send_mailing(emails: list, mail: dict):
    print(emails)
    print(mail)
    send_mail(
        mail.get("subject"),
        mail.get("message"),
        settings.EMAIL_HOST_USER,
        emails,
        mail.get("html_message"),
    )
