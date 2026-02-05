from app.core.security import hash_password
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
from fastapi import HTTPException


class UserService:
    @staticmethod 
    def register_user(payload: UserCreate):
        try :
            data = payload.model_dump()
            data["password"] = hash_password(data["password"])
            return UserRepository.create_user(data)
        except Exception as e:
             raise HTTPException(status_code=400, detail=str(e))