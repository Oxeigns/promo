from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from utils.logger import logger
from database import insert_payment, get_latest_payment


@Client.on_message(filters.private & filters.command("upgrade"))
async def upgrade_cmd(client: Client, message: Message):
    logger.info("User %s requested upgrade info", message.from_user.id)
    await message.reply_text(
        "Send the amount via UPI and reply with /paid <txn_id> to upgrade.",
        parse_mode=ParseMode.HTML,
    )


@Client.on_message(filters.private & filters.command("paid"))
async def paid_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /paid <txn_id>", parse_mode=ParseMode.HTML)
        return
    txn_id = message.command[1]
    await insert_payment(message.from_user.id, txn_id)
    logger.info("Payment from %s recorded with txn %s", message.from_user.id, txn_id)
    await message.reply_text(
        "Payment recorded. Wait for approval.", parse_mode=ParseMode.HTML
    )


@Client.on_message(filters.private & filters.command("payment_status"))
async def payment_status_cmd(client: Client, message: Message):
    payment = await get_latest_payment(message.from_user.id)
    if not payment:
        await message.reply_text(
            "<b>No payment found.</b>", parse_mode=ParseMode.HTML
        )
        return
    await message.reply_text(
        f"<b>Status:</b> {payment['status']}", parse_mode=ParseMode.HTML
    )

