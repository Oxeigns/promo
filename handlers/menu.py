from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode
from utils.logger import logger
from utils.buttons import main_menu_buttons

@Client.on_callback_query(filters.regex("^menu$"))
async def menu_cb(client: Client, query: CallbackQuery):
    logger.info("User %s opened menu", query.from_user.id)
    await query.message.edit_text(
        "<b>\ud83d\udccc Main Menu</b>",
        reply_markup=main_menu_buttons(),
        parse_mode=ParseMode.HTML,
    )
