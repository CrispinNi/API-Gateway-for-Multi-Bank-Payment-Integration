from fastapi import FastAPI
import requests

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
