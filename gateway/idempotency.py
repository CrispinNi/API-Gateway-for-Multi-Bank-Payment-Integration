import redis
import json

r = redis.Redis(host="redis")

def check_key(key):

    data = r.get(key)

    if data:
        return json.loads(data)

def save_key(key, response):

    r.set(key, json.dumps(response), ex=86400)