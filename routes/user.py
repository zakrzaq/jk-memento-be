from fastapi import APIRouter, Depends, HTTPException
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


@router.post("/", response_model=schema.User, status_code=201)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)
