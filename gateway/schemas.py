from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class PaymentCreate(BaseModel):
    payment_id: str
    amount: float
    currency: str
    bank: str