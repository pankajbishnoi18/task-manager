import json
from fastapi import status,HTTPException
def show_all_tasks():
    with open("fake_db.json","r")as file:
        data =json.load(file)
    return data

def data_converter(task,task_id):
    converted_data={
        task_id:task
    }
    return converted_data
def  add_any_task(task,task_id):
    
    data=show_all_tasks()
    for i in data:
        if list((i).keys())[0]==str(task_id):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"this task id {task_id} already exists , use a different one")
            
    
    new_data=data_converter(task,task_id)
    data.append(new_data)

    
    with open("fake_db.json","w")as file:
        json.dump(data,file,indent=4)
    
    return {"success":f"task with task id {task_id} is added "}
def delete_any_task(task_id):
    data=show_all_tasks()
    for i in data:
        
        if list((i).keys())[0]==str(task_id):
            data.remove(i)
            result={"success":f"task with task_id {task_id} is deleted"}
            with open("fake_db.json","w")as file:
                json.dump(data,file,indent=4)
                return result
        
       
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such task id")
def show_any_task(task_id):
    data=show_all_tasks()
    
    for i in data:
        
        if list((i).keys())[0]==str(task_id):
            result= i
            return result
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such task id")

def filter_tasks(priority):
    
        data=show_all_tasks()
        l=[]
        for i in data:
            print()
            if list(i.values())[0]["priority"]==str(priority):
                l.append(i)

        
        return l



