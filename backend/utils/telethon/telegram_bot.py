import os
from dotenv import load_dotenv
from telethon import TelegramClient
import logging

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)


api_id = int(os.getenv('TELETHON_API_ID'))
api_hash = os.getenv('TELETHON_API_HASH')

function_calls = {}


def log_first_call(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name not in function_calls:
            logging.info(
                """
                
                * g o a t s e x * g o a t s e x * g o a t s e x *
                g                                               g  
                o /     \             \            /    \       o
                a|       |             \          |      |      a
                t|       `.             |         |       :     t
                s`        |             |        \|       |     s
                e \       | /       /  \\\   --__ \\       :    e
                x  \      \/   _--~~          ~--__| \     |    x  
                *   \      \_-~                    ~-_\    |    *
                g    \_     \        _.--------.______\|   |    g
                o      \     \______// _ ___ _ (_(__>  \   |    o
                a       \   .  C ___)  ______ (_(____>  |  /    a
                t       /\ |   C ____)/      \ (_____>  |_/     t
                s      / /\|   C_____)       |  (___>   /  \    s
                e     |   (   _C_____)\______/  // _/ /     \   e
                x     |    \  |__   \\_________// (__/       |  x
                *    | \    \____)   `----   --'             |  *
                g    |  \_          ___\       /_          _/ | g
                o   |              /    |     |  \            | o
                a   |             |    /       \  \           | a
                t   |          / /    |         |  \           |t
                s   |         / /      \__/\___/    |          |s
                e  |           /        |    |       |         |e
                x  |          |         |    |       |         |x
                * g o a t s e x * g o a t s e x * g o a t s e x *
                """)
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