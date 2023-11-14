from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.dependencies import get_db
from crud import todo as crud
from schemas import todo as schema

router = APIRouter()


@router.get("/{id}", response_model=schema.Todo)
async def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_todo(db, id)

@router.get("/", response_model=list[schema.Todo])
async def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


@router.get("/", response_model=list[schema.Todo])
async def get_todos_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_active_todos_by_user_id(db, user_id)


@router.post("/", response_model=schema.Todo)
async def create_todo(
    todo: schema.TodoCreate, user_id: int, db: Session = Depends(get_db)
):
    return crud.create_todo(db, todo, user_id)
