from fastapi import FastAPI, HTTPException
from model import User, Transaction
from data import users, transactions
from typing import List
app = FastAPI()
@app.get("/users", response_model=List[User])
def list_users():
    return users
@app.post("/wallet/{user_id}", response_model=User)
def update_wallet(user_id: int, amount: float):
    for user in users:
        if user["user_id"] == user_id:
            user["wallet_balance"] += amount

            # create new transaction
            new_transaction = {
                "transaction_id": len(transactions) + 1,
                "user_id": user_id,
                "amount": amount,
                "type": "credit" if amount > 0 else "debit"
            }
            transactions.append(new_transaction)
            return user


    raise HTTPException(status_code=404, detail="User not found")

@app.get("/transactions/{user_id}", response_model=List[Transaction])
def get_transactions(user_id: int):
    user_transactions = []
    for txn in transactions:
        if txn["user_id"] == user_id:
            user_transactions.append(txn)

    if len(user_transactions) == 0:
        raise HTTPException(status_code=404, detail="No transactions found for this user")

    return user_transactions