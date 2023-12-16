import os
from dotenv import load_dotenv
from telethon import TelegramClient
import asyncio
import logging

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

class TelegramBotClient:
    def __init__(self):
        # api_id = int(os.getenv('TELETHON_API_ID'))
        # api_hash = os.getenv('TELETHON_API_HASH')
        # self.client = TelegramClient('anon', api_id, api_hash)
        pass

    async def get_user_id(self, user_name: str):
        try:
            user = await self.client.get_entity(user_name)
            return user.id
        except Exception as e:
            logging.error(f"Error in get_user_id: {e}")
            return None

    async def send_msg(self, user_id, msg):
        try:
            await self.client.send_message(user_id, msg)
        except Exception as e:
            logging.error(f"Error in send_msg to user {user_id}: {e}")

    async def run(self, func):
        async with self.client:
            await self.client.start()
            try:
                return await func(self)
            except Exception as e:
                logging.error(f"Error in run: {e}")

async def get_user_id(client, user_link):
    return await client.get_user_id(user_link)

def get_user_id_sync(client, user_link):
    return asyncio.run(client.run(lambda client=client, user_link=user_link: get_user_id(client, user_link)))