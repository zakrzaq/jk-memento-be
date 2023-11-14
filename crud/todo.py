from sqlalchemy.orm import Session

from models.todo import Todo
from schemas.todo import TodoCreate


def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_active_todos_by_user_id(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).filter(Todo.is_active).all()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
