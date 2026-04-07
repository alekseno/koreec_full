import httpx
from secondary_func import create_task

def test_create_task():
    response = create_task(
        content = "me 123",
        user_id = "string",
        is_done = False
    )
    
    assert response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {response.status_code}"
    
    data = response.json()
    assert data['task']['content'] == "me 123", "content не совпадает"
    assert data['task']['is_done'] == False, "is_done не совпадает"

 

    