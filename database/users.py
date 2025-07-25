from .mongo import db

users_col = db.users

async def ensure_user(user_id: int):
    user = await users_col.find_one({"user_id": user_id})
    if not user:
        user = {
            "user_id": user_id,
            "credits": 0,
            "premium": False,
            "joined_groups": [],
            "joined_count": 0,
            "banned": False,
        }
        await users_col.insert_one(user)
    return user

async def get_user(user_id: int):
    return await users_col.find_one({"user_id": user_id})

async def increment_credits(user_id: int, amount: int = 1):
    await users_col.update_one({"user_id": user_id}, {"$inc": {"credits": amount}})

async def update_premium(user_id: int, value: bool):
    await users_col.update_one({"user_id": user_id}, {"$set": {"premium": value}})

async def ban_user(user_id: int):
    await users_col.update_one({"user_id": user_id}, {"$set": {"banned": True}})

def get_all_users():
    return users_col.find({})


async def increment_join_count(user_id: int) -> bool:
    user = await users_col.find_one({"user_id": user_id})
    count = user.get("joined_count", 0) + 1
    if count >= 3:
        await users_col.update_one(
            {"user_id": user_id}, {"$set": {"joined_count": 0}}
        )
        return True
    await users_col.update_one(
        {"user_id": user_id}, {"$set": {"joined_count": count}}
    )
    return False
