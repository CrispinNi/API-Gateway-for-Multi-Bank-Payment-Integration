import redis
from fastapi import HTTPException

r = redis.Redis(host="redis", port=6379)

FAIL_LIMIT = 5
BLOCK_TIME = 60


def check_circuit(service):

    fails = r.get(f"fail:{service}")

    if fails and int(fails) >= FAIL_LIMIT:
        raise HTTPException(
            status_code=503,
            detail="Service temporarily unavailable"
        )


def record_failure(service):

    pipe = r.pipeline()

    pipe.incr(f"fail:{service}")
    pipe.expire(f"fail:{service}", BLOCK_TIME)

    pipe.execute()