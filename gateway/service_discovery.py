import redis

r = redis.Redis(host="redis", port=6379)

def get_bank_service(bank):

    service = r.get(f"bank:{bank}")

    if service:
        return service.decode()

    return None