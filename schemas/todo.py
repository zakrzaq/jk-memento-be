from typing import Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    parent_id: Optional[int]
    title: str
    description: str
    priority: Optional[int]


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
