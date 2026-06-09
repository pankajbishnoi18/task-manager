from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional
import json
from memory import add_any_task,show_all_tasks,delete_any_task,show_any_task
app=FastAPI()
class Task(BaseModel):
    task:str
    priority:str
class TaskId(BaseModel):
    task_id:int

@app.get("/task/{task_id}")
def list_any_task(task_id:int):
    return show_any_task(task_id)


@app.get("/task")
def list_all_task():
    return show_all_tasks()

@app.post("/task/{task_id}")
def add_task(task:Task,task_id:int):
    task=task.model_dump()
    return add_any_task(task,task_id)
@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    return delete_any_task(task_id)
    



   

 