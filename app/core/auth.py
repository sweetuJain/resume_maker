from jose import jwt
from app.core.config import settings
from datetime import datetime, timedelta
secrent_key = settings.JWT_SECRET
algo = settings.JWT_ALGO

def create_access_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MIN)
    }
    return jwt.encode(payload, secrent_key, algorithm=algo)