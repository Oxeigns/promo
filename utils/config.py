import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH")
    MONGO_URL = os.getenv("MONGO_URL")
    OWNER_ID = int(os.getenv("OWNER_ID", 0))
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP")
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL")
    IMAGE_URL = os.getenv("IMAGE_URL")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    ENV = os.getenv("ENV", "development")
