import os
from dotenv import load_dotenv
from telethon import TelegramClient
import logging

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)


api_id = int(os.getenv('TELETHON_API_ID'))
api_hash = os.getenv('TELETHON_API_HASH')


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

async def send_msg(user_id, msg):
    try:
        client = TelegramClient('anon', api_id, api_hash)
        await client.start()
        await client.send_message(user_id, msg)
        await client.disconnect()
    except Exception as e:
        logging.error(f"Error in send_msg to user {user_id}: {e}")