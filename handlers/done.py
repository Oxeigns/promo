from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode
from utils.logger import logger
from database import (
    increment_credits,
    increment_promo,
    increment_join_count,
    get_group_by_owner,
    increment_referral_join,
)


@Client.on_callback_query(filters.regex(r"^done:(.*)"))
async def done_cb(client: Client, query: CallbackQuery):
    group_id = query.data.split(":", 1)[1]
    user_id = query.from_user.id
    await increment_credits(user_id)
    await increment_promo(group_id)
    if await increment_join_count(user_id):
        user_group = await get_group_by_owner(user_id)
        if user_group:
            await increment_promo(str(user_group["_id"]))
            await client.send_message(user_id, "<b>Your group has been boosted for joining 3 groups!</b>", parse_mode=ParseMode.HTML)
    inviter = await increment_referral_join(user_id)
    if inviter:
        await increment_credits(inviter)
    logger.info("User %s completed promo for group %s", user_id, group_id)
    await query.answer("Credits added!", show_alert=True)
    await query.message.delete()

