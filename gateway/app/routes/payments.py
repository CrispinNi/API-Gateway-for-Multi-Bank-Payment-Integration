from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_payment(user_id: str, bank_name: str, amount: float, currency: str, db: Session = Depends(get_db)):
    transaction = Transaction(
        user_id=user_id,
        bank_name=bank_name,
        amount=amount,
        currency=currency,
        reference=str(uuid.uuid4())
    )
    db.add(transaction)
    db.commit()
    return {"message": "Payment initiated", "reference": transaction.reference}