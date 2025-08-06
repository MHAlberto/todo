from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str | None = None

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    completed: bool

class ToDoResponse(ToDoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
