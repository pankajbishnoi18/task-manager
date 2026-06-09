from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional
import json
from memory import add_any_task,show_all_tasks,delete_any_task,show_any_task,filter_tasks
app=FastAPI()
class Task(BaseModel):
    task:str
    priority:str
class TaskId(BaseModel):
    task_id:int

@app.get("/task/{task_id}",status_code=status.HTTP_200_OK)
def list_any_task(task_id:int):
    return show_any_task(task_id)


@app.get("/task",status_code=status.HTTP_200_OK)
def list_all_task(priority:Optional[str]=None):
    #
    if priority:
        return filter_tasks(priority)
    else:
        return show_all_tasks()
@app.get("/tasks/priority_wise",status_code=status.HTTP_200_OK)  #/task/priority_wise?priority=high_to_low
def sorted_task():
    k=[]
    l=["very high","high","medium","low","very low"]
    for i in l:
        k+=filter_tasks(i)
    return k
      

@app.post("/task/{task_id}",status_code=status.HTTP_201_CREATED)
def add_task(task:Task,task_id:int):
    task=task.model_dump()
    return add_any_task(task,task_id)
@app.delete("/task/{task_id}",status_code=status.HTTP_200_OK)
def delete_task(task_id:int):
    return delete_any_task(task_id)

    



   

 