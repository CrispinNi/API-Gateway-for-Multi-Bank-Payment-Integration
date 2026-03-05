from fastapi import HTTPException
from app.redis_client import redis_client
import time

RATE_LIMIT = 10  # requests
WINDOW_SIZE = 60  # seconds

def check_rate_limit(user_id: str):
    key = f"rate_limit:{user_id}"
    current = redis_client.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    pipe = redis_client.pipeline()
    pipe.incr(key, 1)

    if not current:
        pipe.expire(key, WINDOW_SIZE)

    pipe.execute()