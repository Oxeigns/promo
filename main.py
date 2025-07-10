from pyrogram import Client
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


if __name__ == "__main__":
    logger.info("Starting bot")
    app.run()
