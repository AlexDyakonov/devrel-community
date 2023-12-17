from celery import shared_task
import asyncio
import logging
from utils.telethon.telegram_bot import get_telegram_data
from users.models import User
from analitics.models import Source, SourceUsers
import time


@shared_task
def get_telegram_data_task(telegram_url):
    try:
        users_data = asyncio.run(get_telegram_data(telegram_url))
        return users_data
    except Exception as e:
        logging.error(f"Error in count_telegram_stats: {e}")
        return []

@shared_task
def process_and_save_user_data(telegram_url):
    task_result = get_telegram_data_task.delay(telegram_url)

    while not task_result.ready():
        time.sleep(1) 

    users_data = task_result.result

    for user_data in users_data:
        user, _= User.objects.update_or_create(
            telegram_id=int(user_data['telegram_id']),
            email=user_data['email'],
            password=user_data['password'],
            telegram_url=user_data['telegram_url'],
            first_name=users_data['first_name'],
            last_name=user_data['last_name'],
        )
        
        SourceUsers.objects.update_or_create(user, Source.objects.get(url=telegram_url), user_data['message_count'])
