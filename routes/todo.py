from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.dependencies import get_db
from crud import todo as crud
from schemas import todo as schema
from utils.responses import no_result, NoResult

router = APIRouter()


@router.get("/{id}", response_model=schema.Todo | NoResult)
async def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_todo(db, id) or no_result


@router.get("/", response_model=list[schema.Todo] | NoResult)
async def get_todos(user_id: int | None = None, db: Session = Depends(get_db)):
    if user_id:
        return crud.get_active_todos_by_user_id(db, user_id) or no_result
    else:
        return crud.get_todos(db) or no_result


@router.post("/", response_model=schema.TodoBase | str, status_code=201)
async def create_todo(
    todo: schema.TodoCreate | str, user_id: int, db: Session = Depends(get_db)
):
    return crud.create_todo(db, todo, user_id)
    # return todo
