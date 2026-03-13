import httpx
from secondary_func import create_task
 

def test_create_content_false():
    response = create_task(
        content = False,
        user_id = "string",
        is_done = False
    )

    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {response.status_code}"

    assert data['task']['content'] == ['content']
    print(data)
  
    