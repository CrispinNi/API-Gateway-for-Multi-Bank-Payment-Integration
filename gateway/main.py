from fastapi import FastAPI, Depends
from auth import verify_token
from kafka_producer import send_payment_event
from redis_cache import cache_payment
from database import engine, Base
from routes.auth import router as auth_router

app = FastAPI(title="Multi-Bank Payment API Gateway")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth")


@app.post("/payments")
async def create_payment(payment: dict, user=Depends(verify_token)):

    payment_id = payment["payment_id"]

    cache_payment(payment_id, payment)

    send_payment_event(payment)

    return {
        "status": "processing",
        "payment_id": payment_id
    }