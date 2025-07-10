from .mongo import db

groups_col = db.groups

async def get_active_group():
    return await groups_col.find_one({"active": True})

async def increment_promo(group_id):
    await groups_col.update_one({"_id": group_id}, {"$inc": {"promo": 1}})

async def submit_group(owner_id: int, link: str, title: str, category: str = "general"):
    await groups_col.update_one(
        {"owner_id": owner_id},
        {"$set": {"owner_id": owner_id, "link": link, "active": True, "title": title, "category": category}},
        upsert=True
    )

async def get_group_by_owner(owner_id: int):
    return await groups_col.find_one({"owner_id": owner_id})
