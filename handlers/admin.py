from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from utils.config import Config
from utils.logger import logger
from database import (
    update_payment_status,
    approve_group,
    ban_group,
    get_all_users,
    payments_col,
)


owner_filter = filters.user(Config.OWNER_ID)


@Client.on_message(filters.private & owner_filter & filters.command("approve"))
async def approve_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /approve <group_id>", parse_mode=ParseMode.HTML)
        return
    group_id = message.command[1]
    await approve_group(group_id)
    logger.info("Group %s approved by %s", group_id, message.from_user.id)
    await message.reply_text("Group approved.", parse_mode=ParseMode.HTML)


@Client.on_message(filters.private & owner_filter & filters.command("ban"))
async def ban_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /ban <group_id>", parse_mode=ParseMode.HTML)
        return
    group_id = message.command[1]
    await ban_group(group_id)
    logger.info("Group %s banned by %s", group_id, message.from_user.id)
    await message.reply_text("Group banned.", parse_mode=ParseMode.HTML)


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


@Client.on_message(filters.private & owner_filter & filters.command("log"))
async def payments_cmd(client: Client, message: Message):
    logs = []
    async for pay in payments_col.find({}).sort("_id", -1).limit(5):
        logs.append(f"{pay['user_id']} - {pay['txn_id']} - {pay['status']}")
    text = "\n".join(logs) if logs else "No logs"
    await message.reply_text(text, parse_mode=ParseMode.HTML)

