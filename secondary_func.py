import httpx
from config import BASE_URL
from typing import Any #принимает любые значения

def create_task(
        content: Any,
        user_id: str,
        is_done: bool
):
    body = {
        "content": content,
        "user_id": user_id,
        "is_done": is_done
    }

    path = "/create-task"
    return httpx.put(BASE_URL + path, json = body)