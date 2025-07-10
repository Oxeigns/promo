from .mongo import db

refs_col = db.referrals

async def add_referral(referred_id: int, inviter_id: int):
    await refs_col.update_one(
        {"referred_id": referred_id},
        {"$setOnInsert": {"referred_id": referred_id, "inviter_id": inviter_id, "join_count": 0}},
        upsert=True,
    )

async def get_referral(referred_id: int):
    return await refs_col.find_one({"referred_id": referred_id})

async def increment_referral_join(referred_id: int):
    ref = await refs_col.find_one({"referred_id": referred_id})
    if ref and ref.get("join_count", 0) < 5:
        await refs_col.update_one({"referred_id": referred_id}, {"$inc": {"join_count": 1}})
        return ref.get("inviter_id")
    return None

