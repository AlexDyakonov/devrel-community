from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from bs4 import BeautifulSoup
from utils.telethon.telegram_bot import get_user_id, send_msg
import asyncio
import logging

@shared_task
def bar():
    return "Hello world!"


@shared_task
def send_mailing(emails: list, mail: dict):
    html_message = mail.get("html_message")
    soup = BeautifulSoup(html_message, 'html.parser')
    html_message = str(soup)
    print(html_message)
    
    send_mail(
        mail.get("subject"),
        mail.get("message"),
        settings.EMAIL_HOST_USER,
        emails,
        html_message=html_message,
    )


@shared_task
def send_tg_message(tg_ids: list, message: str):
    for tg_id in tg_ids:
        print("Попытка отправить сообщение пользователю:" + str(tg_id) + " с контентом *** " + message + " ***")
        try:
            asyncio.run(send_msg(tg_id, msg=message))
        except:
            print("Сообщение пользователю: " + str(tg_id) + " не доставлено")


@shared_task
def get_telegram_id(telegram_url):
    try:
        telegram_id = asyncio.run(get_user_id(telegram_url))
        return telegram_id
    except Exception as e:
        logging.error(f"Error in get_telegram_id: {e}")
        return None