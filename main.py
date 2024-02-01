from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Task(BaseModel):
    title: str
    is_completed: bool

class Task1(BaseModel):
    id: int

class Task2(BaseModel):
    title: str

tasks = []
taskCount = 1

def get_task_by_id(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail="There is no task at that id")

def get_task_by_id1(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
    

@app.post("/v1/tasks", status_code=201)
def create_task(data: Task2):
    global taskCount
    new_task = {"id": taskCount, "title": data.title, "is_completed": False}
    tasks.append(new_task)
    taskCount += 1
    return {"id": new_task["id"]}


@app.get('/v1/tasks', status_code=200)
async def get_all_tasks():
    return {'tasks': tasks}



@app.get('/v1/tasks/{task_id}', status_code=200)
async def get_task_by_id_endpoint(task_id: int):
    task = get_task_by_id(task_id)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail=f'There is no task at that id')



@app.put("/v1/tasks/{task_id}", status_code=204)
def edit(task_id:int,data:Task):
    task = get_task_by_id(task_id)
    task["title"] = data.title
    task["is_completed"] = data.is_completed




 



@app.post('/v1/tasks/bulk', status_code=201)
async def add_bulk_tasks(task_list: List[Task]):
    global taskCount
    try:
        added_tasks = []

        for task_data in task_list:
            task_id = taskCount  
            task = {'id': task_id, 'title': task_data.title, 'is_completed': task_data.is_completed}
            tasks.append(task)
            added_tasks.append({"id": taskCount})
            taskCount+=1

        return {'tasks': added_tasks}

    except Exception as e:
        error_message = f'Internal Server Error: {str(e)}'
        raise HTTPException(status_code=500, detail=error_message)
    




@app.delete('/v1/tasks/bulk', status_code=204)
async def delete_bulk(task_list: List[Task1]):
    try:
        task = get_task_by_id1(task_list[0].id)
        if task:
            tasks.remove(task)
        else:
            raise HTTPException(status_code=204, detail=None)

    except Exception as e:
        error_message = None
        raise HTTPException(status_code=204, detail=error_message)


@app.delete('/v1/tasks/{task_id}', status_code=204)
async def delete_task_by_id(task_id: int):
    try:
        task = get_task_by_id1(task_id)
        if task:
            tasks.remove(task)
        else:
            raise HTTPException(status_code=204, detail=None)

    except Exception as e:
        error_message = None
        raise HTTPException(status_code=204, detail=error_message)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


