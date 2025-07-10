from pyrogram import Client, idle
from utils.config import Config
from utils.logger import logger
import handlers  # noqa: F401


app = Client(
    "promo-bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root": "handlers"},
)

async def main():
    logger.info("Bot started")
    await idle()


if __name__ == "__main__":
    app.run(main())
