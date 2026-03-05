import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def check_idempotency(key):

    if r.exists(key):
        return r.get(key)

    return None


def save_response(key, value):

    r.set(key, value, ex=3600)