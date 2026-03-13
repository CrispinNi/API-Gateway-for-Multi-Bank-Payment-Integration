import redis
from fastapi import HTTPException

r = redis.Redis(host="redis")

LIMIT = 10
WINDOW = 60

def check_rate(user_id):

    key = f"rate:{user_id}"

    count = r.get(key)

    if count and int(count) >= LIMIT:
        raise HTTPException(status_code=429)

    r.incr(key)
    r.expire(key, WINDOW)