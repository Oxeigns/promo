from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.config import Config
from utils.logger import logger
from database.db import users_col


@Client.on_message(filters.private & filters.command("start"))
async def start_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    user = await users_col.find_one({"user_id": user_id})
    if not user:
        await users_col.insert_one({"user_id": user_id, "credits": 0, "premium": False, "joined_groups": []})
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("\ud83d\udc49 Menu", callback_data="menu")
        ]
    ])
    await message.reply_text(
        f"Hello {message.from_user.mention}! Welcome to the promo bot.",
        reply_markup=buttons
    )
