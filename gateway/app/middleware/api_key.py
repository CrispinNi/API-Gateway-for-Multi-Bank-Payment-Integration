from fastapi import Header, HTTPException

VALID_KEYS = ["bank_test_key"]

async def verify_api_key(x_api_key: str = Header(...)):

    if x_api_key not in VALID_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API key")