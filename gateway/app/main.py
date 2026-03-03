from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, payments


app = FastAPI(title="Multi-Bank Payment API Gateway")

app.include_router(auth.router, prefix="/auth")
app.include_router(payments.router, prefix="/payments")
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)