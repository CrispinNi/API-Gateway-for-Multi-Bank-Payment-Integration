from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.auth import hash_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, password=hash_password(password), role="client")
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {"error": "Invalid credentials"}
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}