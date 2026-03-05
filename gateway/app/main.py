from fastapi import FastAPI, Depends, Header
from .middleware.api_key import verify_api_key
from .middleware.rate_limit import rate_limit
from .middleware.idempotency import check_idempotency, save_response
from .services.payment_service import process_payment
from .auth.jwt_handler import verify_token

app = FastAPI()

@app.post("/payments")
async def create_payment(
    data: dict,
    authorization: str = Header(...),
    idempotency_key: str = Header(...),
    x_api_key: str = Depends(verify_api_key)
):

    token = authorization.split(" ")[1]

    user = verify_token(token)

    if not user:
        return {"error": "Invalid token"}

    rate_limit(user["client"])

    cached = check_idempotency(idempotency_key)

    if cached:
        return {"cached": cached}

    result = process_payment(data)

    save_response(idempotency_key, str(result))

    return result