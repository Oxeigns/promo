from .mongo import db

payments_col = db.payments

async def insert_payment(user_id: int, txn_id: str, amount: int = 0):
    await payments_col.insert_one({
        "user_id": user_id,
        "txn_id": txn_id,
        "amount": amount,
        "status": "pending"
    })
