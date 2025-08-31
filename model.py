from pydantic import BaseModel
from typing import List
class User(BaseModel):
    user_id: int
    name: str
    email: str
    phone: str
    wallet_balance: float=0.0
class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    type: str