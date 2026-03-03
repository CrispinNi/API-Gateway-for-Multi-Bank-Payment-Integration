from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, payments

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multi-Bank Payment API Gateway")

app.include_router(auth.router, prefix="/auth")
app.include_router(payments.router, prefix="/payments")