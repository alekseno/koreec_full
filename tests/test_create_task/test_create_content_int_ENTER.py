import httpx
from secondary_func import create_task

def test_create_content_int_ENTER():
    response = create_task(
        content = "215465\n215454", #написать перенос строки
        user_id = str,
        is_done = False
    )
    data = response.json()
    print(data)

    assert response.status_code == httpx.codes.UNPROCESSABLE_ENTITY, "Ожидался код 422, пришел {response.status_code}"
    

    

    