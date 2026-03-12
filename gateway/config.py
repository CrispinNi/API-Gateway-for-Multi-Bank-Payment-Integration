import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/payments"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

# JWT Settings
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30