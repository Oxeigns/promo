from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from database.db import users_col, groups_col
from utils.logger import logger


@Client.on_callback_query(filters.regex(r"^done:(.*)"))
async def done_cb(client: Client, query: CallbackQuery):
    group_id = query.data.split(":", 1)[1]
    user_id = query.from_user.id
    await users_col.update_one(
        {"user_id": user_id},
        {"$inc": {"credits": 1}}
    )
    await groups_col.update_one({"_id": group_id}, {"$inc": {"promo": 1}})
    await query.answer("Credits added!", show_alert=True)
    await query.message.delete()
