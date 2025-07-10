from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.config import Config


def main_menu_buttons() -> InlineKeyboardMarkup:
    """Return the main menu inline keyboard."""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🚀 Promote Group", callback_data="promo"),
                InlineKeyboardButton("➕ Submit Group", callback_data="submit"),
            ],
            [
                InlineKeyboardButton("📊 Stats", callback_data="stats"),
                InlineKeyboardButton("💎 Upgrade Plan", callback_data="upgrade"),
            ],
            [
                InlineKeyboardButton("🛠 Support", url=Config.SUPPORT_GROUP),
                InlineKeyboardButton("📢 Updates", url=Config.SUPPORT_CHANNEL),
            ],
        ]
    )


def back_button() -> InlineKeyboardMarkup:
    """Return a back button keyboard."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Back", callback_data="back")]]
    )


def confirm_join_buttons(group_link: str, group_id: str) -> InlineKeyboardMarkup:
    """Buttons shown when a user must join a group."""
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Join", url=group_link)],
            [InlineKeyboardButton("Done", callback_data=f"done:{group_id}")],
        ]
    )


def menu_button() -> InlineKeyboardMarkup:
    """Button used on the /start message to open the menu."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("👉 Menu", callback_data="menu")]]
    )

