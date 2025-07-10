from bson import ObjectId
from .mongo import db

groups_col = db.groups

async def get_active_group():
    return await groups_col.find_one({"active": True, "approved": True})

async def increment_promo(group_id):
    await groups_col.update_one({"_id": ObjectId(group_id)}, {"$inc": {"promo": 1}})

async def submit_group(owner_id: int, link: str, title: str, category: str = "general"):
    await groups_col.update_one(
        {"owner_id": owner_id},
        {
            "$set": {
                "owner_id": owner_id,
                "link": link,
                "active": False,
                "approved": False,
                "promo": 0,
                "title": title,
                "category": category,
            }
        },
        upsert=True
    )

async def get_group_by_owner(owner_id: int):
    return await groups_col.find_one({"owner_id": owner_id})


async def approve_group(group_id: str):
    await groups_col.update_one(
        {"_id": ObjectId(group_id)}, {"$set": {"approved": True, "active": True}}
    )


async def ban_group(group_id: str):
    await groups_col.update_one({"_id": ObjectId(group_id)}, {"$set": {"active": False}})

