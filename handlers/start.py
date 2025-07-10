from pyrogram import Client, filters
from pyrogram.types import Message
from utils.logger import logger
from utils.buttons import START_BUTTONS
from database import ensure_user


@Client.on_message(filters.private & filters.command("start"))
async def start_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    await ensure_user(user_id)
    logger.info("User %s started bot", user_id)
    await message.reply_text(
        f"Hello {message.from_user.mention}! Welcome to the promo bot.",
        reply_markup=START_BUTTONS
    )
