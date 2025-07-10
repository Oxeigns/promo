from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.menu import MENU_BUTTONS


@Client.on_message(filters.private & filters.command("menu"))
async def menu_cmd(client: Client, message: Message):
    await message.reply("\ud83d\udccc **Main Menu**", reply_markup=MENU_BUTTONS)
