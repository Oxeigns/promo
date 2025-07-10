from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

START_BUTTONS = InlineKeyboardMarkup(
    [[InlineKeyboardButton("\u27A1 Menu", callback_data="menu")]]
)

def promo_buttons(link: str, group_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Join", url=link)],
        [InlineKeyboardButton("Done", callback_data=f"done:{group_id}")]
    ])
