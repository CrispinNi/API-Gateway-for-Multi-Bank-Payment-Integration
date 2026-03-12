import redis
import json

r = redis.Redis(host="redis", port=6379)

def cache_payment(payment_id, data):
    r.set(payment_id, json.dumps(data), ex=300)
