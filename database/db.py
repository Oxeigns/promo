from motor.motor_asyncio import AsyncIOMotorClient
from utils.config import Config

client = AsyncIOMotorClient(Config.MONGO_URL)
db = client.promo_bot

users_col = db.users
groups_col = db.groups
credits_col = db.credits
payments_col = db.payments
