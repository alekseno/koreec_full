import httpx
from secondary_func import create_task, del_task

def test_del_task_bad_format():
    response = create_task(
        content = "del negativ task",
        user_id = str,
        is_done = False
    )

    create_data = response.json()
    create_task_id = create_data['task']['task_id'][:8]

    del_response = del_task(create_task_id)
    del_data = del_response.json()

    assert del_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {del_response.status_code}"

    assert del_data['deleted_task_id'] == create_task_id





