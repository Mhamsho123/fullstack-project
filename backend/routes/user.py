from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserBase

from backend.database import get_db

router = APIRouter()


@router.get("/users", response_model=list[UserBase])
def get_all_users(db: Session = Depends(get_db)):
    data = db.get(User).all()

    if not data:
        raise HTTPException(status_code=404, detail="Couldnt find the ID")
    
    return data