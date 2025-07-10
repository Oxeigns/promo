import asyncio
from pyrogram import Client
from utils.config import Config
from utils.logger import logger
import handlers  # noqa: F401


async def main():
    app = Client(
        "promo-bot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins={"root": "handlers"},
    )
    async with app:
        logger.info("Bot started")
        await asyncio.Event().wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
