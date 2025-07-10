from pyrogram import Client, filters
from pyrogram.types import Message
from utils.logger import logger
from utils.buttons import MENU_BUTTONS


@Client.on_message(filters.private & filters.command("menu"))
async def menu_cmd(client: Client, message: Message):
    logger.info("User %s requested menu via command", message.from_user.id)
    await message.reply("\ud83d\udccc **Main Menu**", reply_markup=MENU_BUTTONS)
