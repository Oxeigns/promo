from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from utils.logger import logger
from utils.config import Config
from database import get_user, get_group_by_owner


@Client.on_message(filters.private & filters.command("credits"))
async def credits_cmd(client: Client, message: Message):
    user = await get_user(message.from_user.id)
    credits = user.get("credits", 0) if user else 0
    logger.info("User %s checked credits", message.from_user.id)
    await message.reply_text(
        f"<b>You have {credits} credits.</b>", parse_mode=ParseMode.HTML
    )


@Client.on_message(filters.private & filters.command("mygroup"))
async def mygroup_cmd(client: Client, message: Message):
    group = await get_group_by_owner(message.from_user.id)
    if group:
        await message.reply_text(
            f"<b>Your group:</b> {group['link']}", parse_mode=ParseMode.HTML
        )
    else:
        await message.reply_text(
            "<b>You have not submitted a group.</b>", parse_mode=ParseMode.HTML
        )


@Client.on_message(filters.private & filters.command("help"))
async def help_cmd(client: Client, message: Message):
    logger.info("User %s requested help", message.from_user.id)
    await message.reply_text(
        "Use /menu to access features and earn credits by joining groups.",
        parse_mode=ParseMode.HTML,
    )


@Client.on_message(filters.private & filters.command("refer"))
async def refer_cmd(client: Client, message: Message):
    link = f"https://t.me/{Config.BOT_USERNAME}?start=ref_{message.from_user.id}"
    await message.reply_text(
        f"<b>Share this link to invite friends\n{link}</b>",
        parse_mode=ParseMode.HTML,
    )

