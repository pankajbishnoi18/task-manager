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
    
    new_data=data_converter(task,task_id)
    data.append(new_data)

    try:
     with open("fake_db.json","w")as file:
        json.dump(data,file)
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
        json.dump(data,file)
    return result
def show_any_task(task_id):
    data=show_all_tasks()
    
    for i in data:
        
        if list((i).keys())[0]==str(task_id):
            result= i
        else:
            result= {"failed":"task not found"}
    return result

print(show_any_task(0))
# dic=show_task()[0]
# print(dic)
# value=list(dic.keys())
# print((value)[0])
