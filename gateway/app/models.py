from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    bank_name = Column(String)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String, default="pending")
    reference = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())