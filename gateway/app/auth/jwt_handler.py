from jose import jwt
from ..config import JWT_SECRET

def verify_token(token: str):

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except:
        return None