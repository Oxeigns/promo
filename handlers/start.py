from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from os import getenv

from utils.logger import logger
from utils.buttons import menu_button
from database import ensure_user, add_referral

IMAGE_URL = getenv("IMAGE_URL")


@Client.on_message(filters.private & filters.command("start"))
async def start_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    await ensure_user(user_id)
    if len(message.command) > 1 and message.command[1].startswith("ref_"):
        inviter = int(message.command[1].split("_", 1)[1])
        if inviter != user_id:
            await add_referral(user_id, inviter)
    logger.info("User %s started bot", user_id)
    await message.reply_photo(
        IMAGE_URL,
        caption=(
            f"<b>Welcome {message.from_user.mention}!</b>\n\n"
            "Use the button below to open the menu."
        ),
        reply_markup=menu_button(),
        parse_mode=ParseMode.HTML,
    )
