import httpx
import uuid
from config import BASE_URL
from typing import Any #принимает любые значения

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
