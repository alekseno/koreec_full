import httpx
from secondary_func import create_task, get_task_id, del_task

def test_del_task_x2():
    response = create_task(
        content = "delete task x2",
        user_id = "str",
        is_done = False
    )

    create_data = response.json()
    create_task_id = create_data['task']['task_id']

    del_response = del_task(create_task_id)
    del_data = del_response.json()

    assert del_response.status_code == httpx.codes.OK, f" Ожидался код 200, пришел {del_response.status_code}"

    assert del_data['deleted_task_id'] == create_task_id

    del_x2_response = del_task(create_task_id)
    del_x2_data = del_x2_response.json()

    assert del_x2_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {del_x2_response.status_code}"

    assert del_x2_data['deleted_task_id'] == create_task_id

