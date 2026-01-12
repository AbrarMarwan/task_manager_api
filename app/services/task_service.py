from app.models.task import Task

tasks_db = []

def get_all_tasks():
    return tasks_db

def add_task(task: Task):
    tasks_db.append(task)
    return task