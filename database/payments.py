from .mongo import db

payments_col = db.payments

async def insert_payment(user_id: int, txn_id: str, amount: int = 0):
    await payments_col.insert_one({
        "user_id": user_id,
        "txn_id": txn_id,
        "amount": amount,
        "status": "pending"
    })


async def get_latest_payment(user_id: int):
    return await payments_col.find_one({"user_id": user_id}, sort=[("_id", -1)])


async def update_payment_status(txn_id: str, status: str):
    await payments_col.update_one({"txn_id": txn_id}, {"$set": {"status": status}})

