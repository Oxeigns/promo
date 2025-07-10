from pyrogram import Client, filters
from pyrogram.types import Message
from utils.logger import logger
from database import get_user, get_group_by_owner


@Client.on_message(filters.private & filters.command("credits"))
async def credits_cmd(client: Client, message: Message):
    user = await get_user(message.from_user.id)
    credits = user.get("credits", 0) if user else 0
    logger.info("User %s checked credits", message.from_user.id)
    await message.reply_text(f"You have **{credits}** credits.")


@Client.on_message(filters.private & filters.command("mygroup"))
async def mygroup_cmd(client: Client, message: Message):
    group = await get_group_by_owner(message.from_user.id)
    if group:
        await message.reply_text(f"Your group: {group['link']}")
    else:
        await message.reply_text("You have not submitted a group.")


@Client.on_message(filters.private & filters.command("help"))
async def help_cmd(client: Client, message: Message):
    logger.info("User %s requested help", message.from_user.id)
    await message.reply_text(
        "Use /menu to access features and earn credits by joining groups."
    )
