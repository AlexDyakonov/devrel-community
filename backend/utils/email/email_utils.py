from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import activate

def send_token_email(user, confirmation_link):
    html_message = render_to_string('token_email.html', {'confirmation_link': confirmation_link})
    subject = ('Подтверждение регистрации')
    message = ('Для завершения регистрации, пожалуйста, перейдите по следующей ссылке:') + str(confirmation_link)
    send_mail(subject, message, settings.EMAIL_HOST_USER , [user.email], html_message=html_message)