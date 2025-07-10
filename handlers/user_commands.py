from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import users_col, groups_col


@Client.on_message(filters.private & filters.command("credits"))
async def credits_cmd(client: Client, message: Message):
    user = await users_col.find_one({"user_id": message.from_user.id})
    credits = user.get("credits", 0) if user else 0
    await message.reply_text(f"You have **{credits}** credits.")


@Client.on_message(filters.private & filters.command("mygroup"))
async def mygroup_cmd(client: Client, message: Message):
    group = await groups_col.find_one({"owner_id": message.from_user.id})
    if group:
        await message.reply_text(f"Your group: {group['link']}")
    else:
        await message.reply_text("You have not submitted a group.")


@Client.on_message(filters.private & filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply_text(
        "Use /menu to access features and earn credits by joining groups."
    )
