from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils.dependencies import get_db
from schemas import user as schema
from crud import user as crud
from utils.responses import no_result, NoResult

router = APIRouter()


@router.get("/{user_id}", response_model=schema.User | NoResult)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id) or no_result


@router.get("/", response_model=schema.User | list[schema.User] | NoResult)
async def get_user_by_email(email: str | None = None, db: Session = Depends(get_db)):
    if email:
        return crud.get_user_by_email(db, email) or no_result
    else:
        return crud.get_users(db) or no_result


@router.post("/", response_model=schema.User, status_code=201)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)
