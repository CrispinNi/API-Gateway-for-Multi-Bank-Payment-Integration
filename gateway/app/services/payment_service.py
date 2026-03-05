from ..models import Payment
from ..database import SessionLocal
from ..kafka.producer import publish_payment_event

def process_payment(data):

    db = SessionLocal()

    payment = Payment(
        amount=data["amount"],
        currency=data["currency"],
        bank=data["bank"],
        status="PENDING"
    )

    db.add(payment)
    db.commit()

    publish_payment_event({
        "payment_id": payment.id,
        "amount": payment.amount
    })

    return {"payment_id": payment.id}