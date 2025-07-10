from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import payments_col


@Client.on_message(filters.private & filters.command("upgrade"))
async def upgrade_cmd(client: Client, message: Message):
    await message.reply_text(
        "Send the amount via UPI and reply with /paid <txn_id> to upgrade."
    )


@Client.on_message(filters.private & filters.command("paid"))
async def paid_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /paid <txn_id>")
        return
    txn_id = message.command[1]
    await payments_col.insert_one({
        "user_id": message.from_user.id,
        "txn_id": txn_id,
        "amount": 0,
        "status": "pending"
    })
    await message.reply_text("Payment recorded. Wait for approval.")
