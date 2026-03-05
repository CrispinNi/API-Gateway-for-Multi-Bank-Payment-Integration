from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL
import time

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Database connected")
        break
    except Exception:
        print("Waiting for database...")
        time.sleep(3)

SessionLocal = sessionmaker(bind=engine)