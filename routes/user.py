from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.dependencies import get_db
from schemas import user as schema
from crud import user as crud

router = APIRouter()


@router.get("/{user_id}", response_model=schema.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@router.get("/{email}", response_model=schema.User)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return crud.get_user_by_email(db, email)


@router.get("/", response_model=list[schema.User])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
