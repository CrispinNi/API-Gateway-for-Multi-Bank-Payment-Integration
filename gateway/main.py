from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.payments import router as payments_router
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(title="Multi-Bank Payment API Gateway")

app.include_router(auth_router, prefix="/auth")
app.include_router(payments_router)

Instrumentator().instrument(app).expose(app)

