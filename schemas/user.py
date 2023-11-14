from pydantic import BaseModel
from schemas.todo import Todo

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    todos: list[Todo]
    is_active: bool

    class Config:
        from_attributes = True
