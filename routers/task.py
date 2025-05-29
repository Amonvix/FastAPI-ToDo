# routers/task.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from schemas.task import TaskCreate, TaskOut
from crud import task as crud_task

# Initialize router
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Dependency to get DB session in each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks from the database.
    """
    return crud_task.get_tasks(db)

@router.post("/", response_model=TaskOut, status_code=201)
def create_new_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task with given title and status.
    """
    return crud_task.create_task(db, task_data)
