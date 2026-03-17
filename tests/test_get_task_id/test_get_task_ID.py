import httpx
from secondary_func import create_task, get_task_id

def test_get_task_id():
    response = create_task(
        content = "my test",
        user_id = str,
        is_done = False
    )
    
    data = response.json()
    task_id = data['task']['task_id']
    
    get_task_response = get_task_id(task_id)

    assert get_task_response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {get_task_response.status_code}"

    get_task_data = get_task_response.json()
    #assert get_task_data["content"] == body["content"]
    #assert get_task_data["user_id"] == body["user_id"]
    assert get_task_data["task_id"] == task_id, "the data is different"
    #print(get_task_data)
