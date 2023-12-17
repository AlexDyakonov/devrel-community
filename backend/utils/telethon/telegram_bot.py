from telethon.errors import FloodWaitError, ChannelPrivateError, SessionPasswordNeededError
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.functions.channels import JoinChannelRequest
from dotenv import load_dotenv
from telethon import TelegramClient
import logging
import json
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)


api_id = int(os.getenv('TELETHON_API_ID'))
api_hash = os.getenv('TELETHON_API_HASH')

function_calls = {}


def log_first_call(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name not in function_calls:
            logging.info("*** TELETHON SERVICE STARTED ***")
            logging.info(function_name)
            function_calls[function_name] = True
        return func(*args, **kwargs)

    return wrapper


@log_first_call
async def get_user_id(user_name: str):
    try:
        client = TelegramClient('anon', api_id, api_hash)
        await client.start()
        user = await client.get_entity(user_name)
        await client.disconnect()
        return user.id
    except Exception as e:
        logging.error(f"Error in get_user_id: {e}")
        return None


@log_first_call
async def send_msg(user_id, msg):
    try:
        client = TelegramClient('anon', api_id, api_hash)
        await client.start()
        await client.send_message(user_id, msg)
        await client.disconnect()
    except Exception as e:
        logging.error(f"Error in send_msg to user {user_id}: {e}")

@log_first_call
async def join_telegram_group(group_url):
    client = TelegramClient('anon', api_id, api_hash)

    try:
        await client.start()
        await client(JoinChannelRequest(group_url))
        print(f"Successfully joined the group {group_url}")
    except ChannelPrivateError:
        print("The group is private and you might not have the permission to join.")
    except FloodWaitError as e:
        print(f"Too many requests. Need to wait for {e.seconds} seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.disconnect()

@log_first_call
async def get_telegram_data(telegram_url):
    client = TelegramClient('anon', api_id, api_hash)
    users_data = []

    try:
        
        await client.start()
        logging.info("Client started")
        await join_telegram_group(telegram_url)
        logging.info(telegram_url + " got. Successfully joined.")
        chat = await client.get_entity(telegram_url)

        logging.info("Entity data got.")
        
        async for user in client.iter_participants(chat, aggressive=True):
            logging.info(user.id)

            user_data = {
                "email": f"{user.id}@shampiniony.ru",
                "password": "rnd",
                "telegram_url": user.username,
                "telegram_id": user.id,
                "first_name": user.first_name or "",
                "last_name": user.last_name or "",
                "message_count": await client.get_participants(chat, filter=ChannelParticipantsRecent(), aggressive=True).total,
            }
            users_data.append(user_data)
            logging.info(user_data)


        await client.disconnect()
        return users_data

    except SessionPasswordNeededError:
        print("Your account is secured with two-factor authentication. Please enter your second factor authentication code.")
        await client.sign_in(password=input())
    except Exception as e:
        logging.error(f"Error in get_telegram_data: {e}")
        await client.disconnect()
        return []
