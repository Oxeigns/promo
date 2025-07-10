from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from utils.logger import logger
from database import increment_credits, increment_promo


@Client.on_callback_query(filters.regex(r"^done:(.*)"))
async def done_cb(client: Client, query: CallbackQuery):
    group_id = query.data.split(":", 1)[1]
    user_id = query.from_user.id
    await increment_credits(user_id)
    await increment_promo(group_id)
    logger.info("User %s completed promo for group %s", user_id, group_id)
    await query.answer("Credits added!", show_alert=True)
    await query.message.delete()
