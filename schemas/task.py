# schemas/task.py

from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    is_done: Optional[bool] = False

class TaskCreate(TaskBase):
    """ Schema for creating a task (input) """
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        from_attributes = True  # Allows compatibility with ORM models (like SQLAlchemy)

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True  # atualizado para Pydantic v2
