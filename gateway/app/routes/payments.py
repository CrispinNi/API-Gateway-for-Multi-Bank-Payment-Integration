from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction
from app.auth import get_current_user
from app.rate_limit import check_rate_limit
from app.redis_client import redis_client
from app.kafka_producer import send_payment_event
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_payment(
    bank_name: str,
    amount: float,
    currency: str,
    idempotency_key: str = Header(None),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Rate limiting
    check_rate_limit(str(current_user.id))

    if not idempotency_key:
        raise HTTPException(status_code=400, detail="Idempotency-Key header required")

    existing = redis_client.get(f"idempotency:{idempotency_key}")
    if existing:
        return {"message": "Duplicate request", "reference": existing}

    transaction = Transaction(
        user_id=current_user.id,
        bank_name=bank_name,
        amount=amount,
        currency=currency,
        reference=str(uuid.uuid4())
    )

    db.add(transaction)
    db.commit()

    redis_client.set(
        f"idempotency:{idempotency_key}",
        transaction.reference,
        ex=3600
    )
    
    send_payment_event({
        "reference": transaction.reference,
        "bank_name": bank_name,
        "amount": amount,
        "currency": currency
    })
    

    return {
        "message": "Payment initiated",
        "reference": transaction.reference
    }