from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import users_col, groups_col


@Client.on_callback_query(filters.regex("^promo$"))
async def promo_cb(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    user = await users_col.find_one({"user_id": user_id})
    if not user or user.get("credits", 0) <= 0:
        await query.answer("Not enough credits.", show_alert=True)
        return
    group = await groups_col.find_one({"active": True})
    if not group:
        await query.answer("No groups to show.", show_alert=True)
        return
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join", url=group["link"])],
        [InlineKeyboardButton("Done", callback_data=f"done:{group['_id']}")]
    ])
    await query.message.edit(
        f"Join **{group['title']}** and press Done to earn credits.",
        reply_markup=buttons
    )
