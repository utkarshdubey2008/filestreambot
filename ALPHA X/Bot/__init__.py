# (c) Code-X-Mania
from pyrogram import Client
import pyromod.listen
from ..vars import Var

StreamBot = Client(
    session_name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
