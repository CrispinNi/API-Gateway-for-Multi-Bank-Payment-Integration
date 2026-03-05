import redis
from fastapi import HTTPException

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def rate_limit(client_id):

    key = f"rate:{client_id}"

    count = r.incr(key)

    if count == 1:
        r.expire(key, 60)

    if count > 100:
        raise HTTPException(429, "Rate limit exceeded")