import httpx
from secondary_func import create_task

def test_create_content_task_str():
    response = create_task(
        content = "task_None",
        user_id = str,
        is_done = False
    )

    data_response = response.json()
    create_task_id = data_response['task']['task_id']

    assert create_task_id == str(create_task_id), "is not str"