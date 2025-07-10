from pyrogram import Client, filters
from pyrogram.types import Message
from utils.config import Config
from database.db import users_col


owner_filter = filters.user(Config.OWNER_ID)


@Client.on_message(filters.private & owner_filter & filters.command("approve"))
async def approve_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /approve <user_id>")
        return
    user_id = int(message.command[1])
    await users_col.update_one({"user_id": user_id}, {"$set": {"premium": True}})
    await message.reply_text("User approved.")


@Client.on_message(filters.private & owner_filter & filters.command("ban"))
async def ban_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /ban <user_id>")
        return
    user_id = int(message.command[1])
    await users_col.update_one({"user_id": user_id}, {"$set": {"banned": True}})
    await message.reply_text("User banned.")


@Client.on_message(filters.private & owner_filter & filters.command("broadcast"))
async def broadcast_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /broadcast <msg>")
        return
    text = " ".join(message.command[1:])
    async for user in users_col.find({}):
        try:
            await client.send_message(user["user_id"], text)
        except Exception:
            pass
    await message.reply_text("Broadcast sent.")


@Client.on_message(filters.private & owner_filter & filters.command("payments"))
async def payments_cmd(client: Client, message: Message):
    await message.reply_text("Payment logs not implemented.")
