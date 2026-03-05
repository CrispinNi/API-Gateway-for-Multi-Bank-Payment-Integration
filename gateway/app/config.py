
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:admin@postgres:5432/payments"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

JWT_SECRET = "supersecret"