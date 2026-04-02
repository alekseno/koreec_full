import httpx
from secondary_func import create_task

 

def test_create_content_false():
    response = create_task(
        content = False,
        user_id = str,
        is_done = False
    )

    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {response.status_code}"

    # проверка поля content==False
    assert data['task']['content'] == "False", "[content] is different"
    assert data['task']['is_done'] == False, "[is_done] is different"
       
    #print(data)
  
    