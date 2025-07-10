from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from utils.logger import logger
from utils.buttons import MENU_BUTTONS

@Client.on_callback_query(filters.regex("^menu$"))
async def menu_cb(client: Client, query: CallbackQuery):
    logger.info("User %s opened menu", query.from_user.id)
    await query.message.edit(
        "\ud83d\udccc **Main Menu**",
        reply_markup=MENU_BUTTONS
    )
