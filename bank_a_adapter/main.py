from fastapi import FastAPI
import requests
import redis

r = redis.Redis(host="redis", port=6379)

r.set("bank:A", "http://bank_a:8000")

app = FastAPI()

@app.post("/process-payment")
def process_payment(data: dict):

    # simulate bank API call
    response = {
        "bank": "BANK_A",
        "status": "approved",
        "transaction_id": "TX123456"
    }

    return response
