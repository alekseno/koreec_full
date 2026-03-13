import httpx
from config import BASE_URL

def test_create_task():

    body = {
        "content": "my test",
        "user_id": "string",
        "is_done": False
        }
     
    create_task_response = httpx.put(BASE_URL + "/create-task", json = body)
    data = create_task_response.json()

def test_update_task():
    pass