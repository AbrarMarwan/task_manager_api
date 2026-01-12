from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.services.task_service import get_all_tasks, add_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks():
    return get_all_tasks()

@router.post("/")
def create_task(task: Task):
    if not task.title:
        raise HTTPException(status_code=400, detail="Title is required")
    return add_task(task)