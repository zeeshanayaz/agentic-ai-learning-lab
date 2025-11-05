from fastapi import FastAPI
from schema.task import Task

app = FastAPI(
    title="Todo App API",
    description="API for managing a Todo application",
    version="1.0.0",
)

tasks = []

@app.get("/")
def health_check():
    return {
        'status': True,
        'message': 'API is running successfully',
    }


@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


