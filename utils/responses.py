from pydantic import BaseModel


class NoResult(BaseModel):
    message: str


no_result = {"message": "No result"}
