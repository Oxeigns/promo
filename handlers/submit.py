from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message
from utils.helpers import valid_group_link
from database.db import groups_col


@Client.on_callback_query(filters.regex("^submit$"))
async def submit_cb(client: Client, query: CallbackQuery):
    await query.message.edit("Send your group link.")
    client.set_parse_mode("markdown")
    client.data = {}
    client.data[query.from_user.id] = "awaiting_link"


@Client.on_message(filters.private & filters.text)
async def submit_link(client: Client, message: Message):
    state = getattr(client, "data", {}).get(message.from_user.id)
    if state == "awaiting_link" and valid_group_link(message.text):
        await groups_col.update_one(
            {"owner_id": message.from_user.id},
            {"$set": {"owner_id": message.from_user.id, "link": message.text, "active": True, "title": message.text, "category": "general"}},
            upsert=True
        )
        await message.reply_text("Group submitted.")
        client.data.pop(message.from_user.id, None)
    elif state == "awaiting_link":
        await message.reply_text("Invalid link.")
