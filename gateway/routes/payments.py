from fastapi import APIRouter, Header, Depends

from rate_limiter import check_rate
from idempotency import check_key, save_key
from kafka_producer import send_payment_event

router = APIRouter()

@router.post("/payments")
def create_payment(payment: dict,
                   idempotency_key: str = Header(...),
                   user=Depends()):

    check_rate(user["user_id"])

    existing = check_key(idempotency_key)

    if existing:
        return existing

    send_payment_event(payment)

    response = {"status": "processing"}

    save_key(idempotency_key, response)

    return response