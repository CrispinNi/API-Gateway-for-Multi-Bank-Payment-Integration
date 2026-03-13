from fastapi import APIRouter, Header, Depends
from auth import verify_token
from rate_limiter import check_rate
from idempotency import check_key, save_key
from kafka_producer import send_payment_event
from schemas import PaymentCreate

router = APIRouter()

@router.post("/payments")
def create_payment(
        payment: PaymentCreate,
        idempotency_key: str = Header(...),
        user=Depends(verify_token)
):

    check_rate(user.id)

    existing = check_key(idempotency_key)

    if existing:
        return existing

    send_payment_event(payment.dict())

    response = {"status": "processing"}

    save_key(idempotency_key, response)

    return response