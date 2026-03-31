import httpx
import uuid
from config import BASE_URL
from typing import Any #принимает любые значения
import re

def create_task(
        content: Any,
        user_id: str,
        is_done: bool
) -> httpx.Response:
    user_id = str(uuid.uuid4())
    body = {
        "content": content,
        "user_id": user_id,
        "is_done": is_done
    }
     
    path = "/create-task"
    return httpx.put(BASE_URL + path, json = body)

def get_task_id(
    task_id: str
) -> httpx.Response:
   
    path = f"/get-task/{task_id}"
    return httpx.get(BASE_URL + path)
 
def get_user_id(
    user_id: str
 ) -> httpx.Response:
    
    path = f"/list-tasks/{user_id}"
    return httpx.get(BASE_URL + path)

def update_task(
        content: Any,
        user_id: str,
        task_id: str,
        is_done: bool
) -> httpx.Response:
    
    body = {
        "content": content,
        "user_id": user_id,
        "task_id": task_id,
        "is_done": is_done
    }
    
    path = f"/update-task"
    return httpx.put(BASE_URL + path, json = body)

def del_task(
        task_id: str
) -> httpx.Response:
    
    path = f"/delete-task/{task_id}"
    return httpx.delete(BASE_URL + path)

#регулярка для проверки формата поля task_id
def template_check_task_id(create_task_id):
    template = re.findall(r"task_[0-9a-z]{32}", create_task_id)
    result_temp = ' '.join(map(str, template))
    return result_temp
