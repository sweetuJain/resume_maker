from fastapi import APIRouter, status
import logging
from app.services.user import UserService
from app.schemas.user import UserCreate, UserOut

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate):
    return UserService.register_user(payload)