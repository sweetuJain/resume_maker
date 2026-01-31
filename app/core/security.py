# password + JWT
from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plan_password: str) -> str: 
    return pwd.hash(plan_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)

