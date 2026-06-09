import json
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
            return {"failed":f"this task id {task_id} already exists , use a different one"}
    
    new_data=data_converter(task,task_id)
    data.append(new_data)

    try:
     with open("fake_db.json","w")as file:
        json.dump(data,file,indent=4)
    except:
        return "here is"
    return {"success":f"task with task id {task_id} is added "}
def delete_any_task(task_id):
    data=show_all_tasks()
    for i in data:
        
        if list((i).keys())[0]==str(task_id):
            data.remove(i)
            result={"success":f"task with task_id {task_id} is deleted"}
        else:
            result= {"failed":"task not found"}
       
       
    with open("fake_db.json","w")as file:
        json.dump(data,file,indent=4)
    return result
def show_any_task(task_id):
    data=show_all_tasks()
    
    for i in data:
        
        if list((i).keys())[0]==str(task_id):
            result= i
            return result
        
    result= {"failed":"task not found"}
    return result

def filter_tasks(priority):
    
        data=show_all_tasks()
        l=[]
        for i in data:
            print()
            if list(i.values())[0]["priority"]==str(priority):
                l.append(i)

        
        return l



