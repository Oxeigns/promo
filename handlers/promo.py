from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode
from utils.logger import logger
from utils.buttons import confirm_join_buttons
from database import get_user, get_active_group


@Client.on_callback_query(filters.regex("^promo$"))
async def promo_cb(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    user = await get_user(user_id)
    if not user or user.get("credits", 0) <= 0:
        await query.answer("Not enough credits.", show_alert=True)
        return
    group = await get_active_group()
    if not group:
        await query.answer("No groups to show.", show_alert=True)
        return
    await query.message.edit_text(
        f"<b>Join {group['title']} and press Done to earn credits.</b>",
        reply_markup=confirm_join_buttons(group["link"], str(group["_id"])),
        parse_mode=ParseMode.HTML,
    )
    logger.info("Sent promo group %s to user %s", group.get('title'), user_id)
