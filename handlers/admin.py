from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from utils.config import Config
from utils.logger import logger
from database import update_premium, ban_user, get_all_users


owner_filter = filters.user(Config.OWNER_ID)


@Client.on_message(filters.private & owner_filter & filters.command("approve"))
async def approve_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /approve <user_id>", parse_mode=ParseMode.HTML)
        return
    user_id = int(message.command[1])
    await update_premium(user_id, True)
    logger.info("User %s approved premium for %s", message.from_user.id, user_id)
    await message.reply_text("User approved.", parse_mode=ParseMode.HTML)


@Client.on_message(filters.private & owner_filter & filters.command("ban"))
async def ban_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /ban <user_id>", parse_mode=ParseMode.HTML)
        return
    user_id = int(message.command[1])
    await ban_user(user_id)
    logger.info("User %s banned user %s", message.from_user.id, user_id)
    await message.reply_text("User banned.", parse_mode=ParseMode.HTML)


@Client.on_message(filters.private & owner_filter & filters.command("broadcast"))
async def broadcast_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /broadcast <msg>", parse_mode=ParseMode.HTML)
        return
    text = " ".join(message.command[1:])
    async for user in get_all_users():
        try:
            await client.send_message(user["user_id"], text)
        except Exception:
            pass
    logger.info("Broadcast from %s sent to all users", message.from_user.id)
    await message.reply_text("Broadcast sent.", parse_mode=ParseMode.HTML)


@Client.on_message(filters.private & owner_filter & filters.command("payments"))
async def payments_cmd(client: Client, message: Message):
    logger.info("%s requested payment logs", message.from_user.id)
    await message.reply_text("Payment logs not implemented.", parse_mode=ParseMode.HTML)
