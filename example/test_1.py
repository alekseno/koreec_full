"""import httpx
import uuid
from config import BASE_URL

def test_check():
    user_id = str(uuid.uuid4())
    body = {
        "content": f"Content for {user_id}",
        "user_id": user_id,
        "task_id": "nvm",
        "is_done": False
    }
    
    response = httpx.put(
        url=BASE_URL + "/create-task",
        json=body
    )
    print(response.text)"""