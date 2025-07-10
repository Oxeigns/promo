from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.config import Config

MENU_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Promote Group", callback_data="promo"),
        InlineKeyboardButton("Submit Group", callback_data="submit")
    ],
    [
        InlineKeyboardButton("View Stats", callback_data="stats"),
        InlineKeyboardButton("Upgrade Plan", callback_data="upgrade")
    ],
    [
        InlineKeyboardButton("Support", url=Config.SUPPORT_GROUP),
        InlineKeyboardButton("Updates", url=Config.SUPPORT_CHANNEL)
    ]
])

@Client.on_callback_query(filters.regex("^menu$"))
async def menu_cb(client: Client, query: CallbackQuery):
    await query.message.edit(
        "\ud83d\udccc **Main Menu**",
        reply_markup=MENU_BUTTONS
    )
