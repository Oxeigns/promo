from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message
from utils.helpers import valid_group_link
from utils.logger import logger
from database import submit_group


@Client.on_callback_query(filters.regex("^submit$"))
async def submit_cb(client: Client, query: CallbackQuery):
    await query.message.edit("Send your group link.")
    client.set_parse_mode("markdown")
    client.data = {}
    client.data[query.from_user.id] = "awaiting_link"
    logger.info("Asked %s for group link", query.from_user.id)


@Client.on_message(filters.private & filters.text)
async def submit_link(client: Client, message: Message):
    state = getattr(client, "data", {}).get(message.from_user.id)
    if state == "awaiting_link" and valid_group_link(message.text):
        await submit_group(message.from_user.id, message.text, message.text)
        logger.info("User %s submitted group %s", message.from_user.id, message.text)
        await message.reply_text("Group submitted.")
        client.data.pop(message.from_user.id, None)
    elif state == "awaiting_link":
        await message.reply_text("Invalid link.")
