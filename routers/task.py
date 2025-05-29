# routers/task.py

from fastapi import APIRouter
from typing import List
from schemas.task import Task

# Initialize a router instance for task-related endpoints
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Temporary mock data to simulate task list
mock_tasks = [
    {"id": 1, "title": "Study FastAPI", "is_done": False},
    {"id": 2, "title": "Write clean code", "is_done": True},
]

@router.get("/", response_model=List[Task])
async def get_tasks():
    """
    Retrieve a list of all tasks.
    This is a temporary mock implementation.
    """
    return mock_tasks
