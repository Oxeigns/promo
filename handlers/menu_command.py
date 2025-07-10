from pyrogram import Client, filters
from pyrogram.types import Message
from utils.logger import logger
from utils.buttons import main_menu_buttons


@Client.on_message(filters.private & filters.command("menu"))
async def menu_cmd(client: Client, message: Message):
    logger.info("User %s requested menu via command", message.from_user.id)
    await message.reply_text(
        "<b>\ud83d\udccc Main Menu</b>",
        reply_markup=main_menu_buttons(),
        parse_mode="HTML",
    )
