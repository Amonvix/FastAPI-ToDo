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
        orm_mode = True  # Allows compatibility with ORM models (like SQLAlchemy)
